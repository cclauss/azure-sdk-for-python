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

from .resource_py3 import Resource


class Export(Resource):
    """A export resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :param format: The format of the export being delivered. Possible values
     include: 'Csv'
    :type format: str or ~azure.mgmt.costmanagement.models.FormatType
    :param delivery_info: Required. Has delivery information for the export.
    :type delivery_info: ~azure.mgmt.costmanagement.models.ExportDeliveryInfo
    :param definition: Required. Has definition for the export.
    :type definition: ~azure.mgmt.costmanagement.models.QueryDefinition
    :param schedule: Has schedule information for the export.
    :type schedule: ~azure.mgmt.costmanagement.models.ExportSchedule
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'delivery_info': {'required': True},
        'definition': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'format': {'key': 'properties.format', 'type': 'str'},
        'delivery_info': {'key': 'properties.deliveryInfo', 'type': 'ExportDeliveryInfo'},
        'definition': {'key': 'properties.definition', 'type': 'QueryDefinition'},
        'schedule': {'key': 'properties.schedule', 'type': 'ExportSchedule'},
    }

    def __init__(self, *, delivery_info, definition, format=None, schedule=None, **kwargs) -> None:
        super(Export, self).__init__(**kwargs)
        self.format = format
        self.delivery_info = delivery_info
        self.definition = definition
        self.schedule = schedule