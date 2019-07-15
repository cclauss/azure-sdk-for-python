# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from __future__ import unicode_literals

import uuid
import logging
import time
from typing import Iterable, Union

from uamqp import constants, errors
from uamqp import compat
from uamqp import SendClient

from azure.eventhub.common import EventData, _BatchSendEventData
from azure.eventhub.error import EventHubError, ConnectError, \
    AuthenticationError, EventDataError, EventDataSendError, ConnectionLostError, _error_handler

log = logging.getLogger(__name__)


class EventHubProducer(object):
    """
    A producer responsible for transmitting EventData to a specific Event Hub,
     grouped together in batches. Depending on the options specified at creation, the producer may
     be created to allow event data to be automatically routed to an available partition or specific
     to a partition.

    """

    def __init__(self, client, target, partition=None, send_timeout=60, keep_alive=None, auto_reconnect=True):
        """
        Instantiate an EventHubProducer. EventHubProducer should be instantiated by calling the `create_producer` method
         in EventHubClient.

        :param client: The parent EventHubClient.
        :type client: ~azure.eventhub.client.EventHubClient.
        :param target: The URI of the EventHub to send to.
        :type target: str
        :param partition: The specific partition ID to send to. Default is None, in which case the service
         will assign to all partitions using round-robin.
        :type partition: str
        :param send_timeout: The timeout in seconds for an individual event to be sent from the time that it is
         queued. Default value is 60 seconds. If set to 0, there will be no timeout.
        :type send_timeout: float
        :param keep_alive: The time interval in seconds between pinging the connection to keep it alive during
         periods of inactivity. The default value is None, i.e. no keep alive pings.
        :type keep_alive: float
        :param auto_reconnect: Whether to automatically reconnect the producer if a retryable error occurs.
         Default value is `True`.
        :type auto_reconnect: bool
        """
        self.running = False
        self.client = client
        self.target = target
        self.partition = partition
        self.timeout = send_timeout
        self.redirected = None
        self.error = None
        self.keep_alive = keep_alive
        self.auto_reconnect = auto_reconnect
        self.retry_policy = errors.ErrorPolicy(max_retries=self.client.config.max_retries, on_error=_error_handler)
        self.reconnect_backoff = 1
        self.name = "EHProducer-{}".format(uuid.uuid4())
        self.unsent_events = None
        if partition:
            self.target += "/Partitions/" + partition
            self.name += "-partition{}".format(partition)
        self._handler = SendClient(
            self.target,
            auth=self.client.get_auth(),
            debug=self.client.config.network_tracing,
            msg_timeout=self.timeout,
            error_policy=self.retry_policy,
            keep_alive_interval=self.keep_alive,
            client_name=self.name,
            properties=self.client._create_properties(self.client.config.user_agent))  # pylint: disable=protected-access
        self._outcome = None
        self._condition = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close(exc_val)

    def _create_handler(self):
        self._handler = SendClient(
            self.target,
            auth=self.client.get_auth(),
            debug=self.client.config.network_tracing,
            msg_timeout=self.timeout,
            error_policy=self.retry_policy,
            keep_alive_interval=self.keep_alive,
            client_name=self.name,
            properties=self.client._create_properties(self.client.config.user_agent))  # pylint: disable=protected-access

    def _redirect(self, redirect):
        self.redirected = redirect
        self.running = False
        self.messages_iter = None
        self._close_connection()

    def _open(self):
        """
        Open the EventHubProducer using the supplied connection.
        If the handler has previously been redirected, the redirect
        context will be used to create a new handler before opening it.

        """
        # pylint: disable=protected-access
        if not self.running:
            if self.redirected:
                self.target = self.redirected.address
            self._create_handler()
            self._handler.open(connection=self.client._conn_manager.get_connection(
                self.client.address.hostname,
                self.client.get_auth()
            ))
            while not self._handler.client_ready():
                time.sleep(0.05)
            self.running = True

    def _close_handler(self):
        self._handler.close()  # close the link (sharing connection) or connection (not sharing)
        self.running = False

    def _close_connection(self):
        self._close_handler()
        self.client._conn_manager.close_connection()  # close the shared connection.

    def _handle_exception(self, exception, retry_count, max_retries):
        if isinstance(exception, KeyboardInterrupt):
            log.info("EventHubConsumer stops due to keyboard interrupt")
            self.close()
            raise
        elif isinstance(exception, (
                errors.MessageAccepted,
                errors.MessageAlreadySettled,
                errors.MessageModified,
                errors.MessageRejected,
                errors.MessageReleased,
                errors.MessageContentTooLarge)
                ):
            log.error("Event data error (%r)", exception)
            error = EventDataError(str(exception), exception)
            self.close(exception)
            raise error
        elif isinstance(exception, errors.MessageException):
            log.error("Event data send error (%r)", exception)
            error = EventDataSendError(str(exception), exception)
            self.close(exception)
            raise error
        elif retry_count >= max_retries:
            log.info("EventHubConsumer has an error and has exhausted retrying. (%r)", exception)
            if isinstance(exception, errors.AuthenticationException):
                log.info("EventHubConsumer authentication failed. Shutting down.")
                error = AuthenticationError(str(exception), exception)
            elif isinstance(exception, errors.LinkDetach):
                log.info("EventHubConsumer link detached. Shutting down.")
                error = ConnectionLostError(str(exception), exception)
            elif isinstance(exception, errors.ConnectionClose):
                log.info("EventHubConsumer connection closed. Shutting down.")
                error = ConnectionLostError(str(exception), exception)
            elif isinstance(exception, errors.MessageHandlerError):
                log.info("EventHubConsumer detached. Shutting down.")
                error = ConnectionLostError(str(exception), exception)
            elif isinstance(exception, errors.AMQPConnectionError):
                log.info("EventHubConsumer connection lost. Shutting down.")
                error_type = AuthenticationError if str(exception).startswith("Unable to open authentication session") \
                    else ConnectError
                error = error_type(str(exception), exception)
            elif isinstance(exception, compat.TimeoutException):
                log.info("EventHubConsumer timed out. Shutting down.")
                error = ConnectionLostError(str(exception), exception)
            else:
                log.error("Unexpected error occurred (%r). Shutting down.", exception)
                error = EventHubError("Receive failed: {}".format(exception), exception)
            self.close(exception=error)
            raise error
        else:
            log.info("EventHubConsumer has an exception (%r). Retrying...", exception)
            if isinstance(exception, errors.AuthenticationException):
                self._close_connection()
            elif isinstance(exception, errors.LinkRedirect):
                log.info("EventHubConsumer link redirected. Redirecting...")
                redirect = exception
                self._redirect(redirect)
            elif isinstance(exception, errors.LinkDetach):
                self._close_handler()
            elif isinstance(exception, errors.ConnectionClose):
                self._close_connection()
            elif isinstance(exception, errors.MessageHandlerError):
                self._close_handler()
            elif isinstance(exception, errors.AMQPConnectionError):
                self._close_connection()
            elif isinstance(exception, compat.TimeoutException):
                pass  # Timeout doesn't need to recreate link or exception
            else:
                self._close_connection()

    def _send_event_data(self):
        self._open()
        max_retries = self.client.config.max_retries
        retry_count = 0
        while True:
            try:
                if self.unsent_events:
                    self._handler.queue_message(*self.unsent_events)
                    self._handler.wait()
                    self.unsent_events = self._handler.pending_messages
                if self._outcome != constants.MessageSendResult.Ok:
                    _error(self._outcome, self._condition)
                return
            except Exception as exception:
                self._handle_exception(exception, retry_count, max_retries)
                retry_count += 1

    def _check_closed(self):
        if self.error:
            raise EventHubError("This producer has been closed. Please create a new producer to send event data.", self.error)

    @staticmethod
    def _set_partition_key(event_datas, partition_key):
        ed_iter = iter(event_datas)
        for ed in ed_iter:
            ed._set_partition_key(partition_key)
            yield ed

    def _on_outcome(self, outcome, condition):
        """
        Called when the outcome is received for a delivery.

        :param outcome: The outcome of the message delivery - success or failure.
        :type outcome: ~uamqp.constants.MessageSendResult
        :param condition: Detail information of the outcome.

        """
        self._outcome = outcome
        self._condition = condition

    def send(self, event_data, partition_key=None):
        # type:(Union[EventData, Iterable[EventData]], Union[str, bytes]) -> None
        """
        Sends an event data and blocks until acknowledgement is
        received or operation times out.

        :param event_data: The event to be sent. It can be an EventData object, or iterable of EventData objects
        :type event_data: ~azure.eventhub.common.EventData, Iterator, Generator, list
        :param partition_key: With the given partition_key, event data will land to
         a particular partition of the Event Hub decided by the service.
        :type partition_key: str
        :raises: ~azure.eventhub.AuthenticationError, ~azure.eventhub.ConnectError, ~azure.eventhub.ConnectionLostError,
                ~azure.eventhub.EventDataError, ~azure.eventhub.EventDataSendError, ~azure.eventhub.EventHubError

        :return: None
        :rtype: None

        Example:
            .. literalinclude:: ../examples/test_examples_eventhub.py
                :start-after: [START eventhub_client_sync_send]
                :end-before: [END eventhub_client_sync_send]
                :language: python
                :dedent: 4
                :caption: Sends an event data and blocks until acknowledgement is received or operation times out.

        """
        self._check_closed()
        if isinstance(event_data, EventData):
            if partition_key:
                event_data._set_partition_key(partition_key)
            wrapper_event_data = event_data
        else:
            event_data_with_pk = self._set_partition_key(event_data, partition_key)
            wrapper_event_data = _BatchSendEventData(
                event_data_with_pk,
                partition_key=partition_key) if partition_key else _BatchSendEventData(event_data)
        wrapper_event_data.message.on_send_complete = self._on_outcome
        self.unsent_events = [wrapper_event_data.message]
        self._send_event_data()

    def close(self, exception=None):
        # type:(Exception) -> None
        """
        Close down the handler. If the handler has already closed,
        this will be a no op. An optional exception can be passed in to
        indicate that the handler was shutdown due to error.

        :param exception: An optional exception if the handler is closing
         due to an error.
        :type exception: Exception

        Example:
            .. literalinclude:: ../examples/test_examples_eventhub.py
                :start-after: [START eventhub_client_sender_close]
                :end-before: [END eventhub_client_sender_close]
                :language: python
                :dedent: 4
                :caption: Close down the handler.

        """
        self.running = False
        if self.error:
            return
        if isinstance(exception, errors.LinkRedirect):
            self.redirected = exception
        elif isinstance(exception, EventHubError):
            self.error = exception
        elif exception:
            self.error = EventHubError(str(exception))
        else:
            self.error = EventHubError("This send handler is now closed.")
        self._handler.close()


def _error(outcome, condition):
    if outcome != constants.MessageSendResult.Ok:
        raise condition
