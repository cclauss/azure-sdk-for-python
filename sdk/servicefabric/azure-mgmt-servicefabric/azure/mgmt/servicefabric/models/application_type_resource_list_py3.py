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

from msrest.serialization import Model


class ApplicationTypeResourceList(Model):
    """The list of application type names.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param value:
    :type value:
     list[~azure.mgmt.servicefabric.models.ApplicationTypeResource]
    :ivar next_link: URL to get the next set of application type list results
     if there are any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ApplicationTypeResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(ApplicationTypeResourceList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None
