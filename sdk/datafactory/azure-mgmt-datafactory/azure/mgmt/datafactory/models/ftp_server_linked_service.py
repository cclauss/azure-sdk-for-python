# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service import LinkedService


class FtpServerLinkedService(LinkedService):
    """A FTP server Linked Service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param host: Required. Host name of the FTP server. Type: string (or
     Expression with resultType string).
    :type host: object
    :param port: The TCP port number that the FTP server uses to listen for
     client connections. Default value is 21. Type: integer (or Expression with
     resultType integer), minimum: 0.
    :type port: object
    :param authentication_type: The authentication type to be used to connect
     to the FTP server. Possible values include: 'Basic', 'Anonymous'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.FtpAuthenticationType
    :param user_name: Username to logon the FTP server. Type: string (or
     Expression with resultType string).
    :type user_name: object
    :param password: Password to logon the FTP server.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    :param enable_ssl: If true, connect to the FTP server over SSL/TLS
     channel. Default value is true. Type: boolean (or Expression with
     resultType boolean).
    :type enable_ssl: object
    :param enable_server_certificate_validation: If true, validate the FTP
     server SSL certificate when connect over SSL/TLS channel. Default value is
     true. Type: boolean (or Expression with resultType boolean).
    :type enable_server_certificate_validation: object
    """

    _validation = {
        'type': {'required': True},
        'host': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'host': {'key': 'typeProperties.host', 'type': 'object'},
        'port': {'key': 'typeProperties.port', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'user_name': {'key': 'typeProperties.userName', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
        'enable_ssl': {'key': 'typeProperties.enableSsl', 'type': 'object'},
        'enable_server_certificate_validation': {'key': 'typeProperties.enableServerCertificateValidation', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(FtpServerLinkedService, self).__init__(**kwargs)
        self.host = kwargs.get('host', None)
        self.port = kwargs.get('port', None)
        self.authentication_type = kwargs.get('authentication_type', None)
        self.user_name = kwargs.get('user_name', None)
        self.password = kwargs.get('password', None)
        self.encrypted_credential = kwargs.get('encrypted_credential', None)
        self.enable_ssl = kwargs.get('enable_ssl', None)
        self.enable_server_certificate_validation = kwargs.get('enable_server_certificate_validation', None)
        self.type = 'FtpServer'