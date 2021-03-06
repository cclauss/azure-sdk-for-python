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


class Policy(Resource):
    """A Policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param description: The description of the policy.
    :type description: str
    :param status: The status of the policy. Possible values include:
     'Enabled', 'Disabled'
    :type status: str or ~azure.mgmt.devtestlabs.models.PolicyStatus
    :param fact_name: The fact name of the policy (e.g. LabVmCount, LabVmSize,
     MaxVmsAllowedPerLab, etc. Possible values include: 'UserOwnedLabVmCount',
     'UserOwnedLabPremiumVmCount', 'LabVmCount', 'LabPremiumVmCount',
     'LabVmSize', 'GalleryImage', 'UserOwnedLabVmCountInSubnet',
     'LabTargetCost', 'EnvironmentTemplate', 'ScheduleEditPermission'
    :type fact_name: str or ~azure.mgmt.devtestlabs.models.PolicyFactName
    :param fact_data: The fact data of the policy.
    :type fact_data: str
    :param threshold: The threshold of the policy (i.e. a number for
     MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy).
    :type threshold: str
    :param evaluator_type: The evaluator type of the policy (i.e.
     AllowedValuesPolicy, MaxValuePolicy). Possible values include:
     'AllowedValuesPolicy', 'MaxValuePolicy'
    :type evaluator_type: str or
     ~azure.mgmt.devtestlabs.models.PolicyEvaluatorType
    :ivar created_date: The creation date of the policy.
    :vartype created_date: datetime
    :ivar provisioning_state: The provisioning status of the resource.
    :vartype provisioning_state: str
    :ivar unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :vartype unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_date': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'unique_identifier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'fact_name': {'key': 'properties.factName', 'type': 'str'},
        'fact_data': {'key': 'properties.factData', 'type': 'str'},
        'threshold': {'key': 'properties.threshold', 'type': 'str'},
        'evaluator_type': {'key': 'properties.evaluatorType', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, description: str=None, status=None, fact_name=None, fact_data: str=None, threshold: str=None, evaluator_type=None, **kwargs) -> None:
        super(Policy, self).__init__(location=location, tags=tags, **kwargs)
        self.description = description
        self.status = status
        self.fact_name = fact_name
        self.fact_data = fact_data
        self.threshold = threshold
        self.evaluator_type = evaluator_type
        self.created_date = None
        self.provisioning_state = None
        self.unique_identifier = None
