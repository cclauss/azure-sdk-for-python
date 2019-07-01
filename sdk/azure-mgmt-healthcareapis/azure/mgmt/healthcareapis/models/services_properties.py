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


class ServicesProperties(Model):
    """The properties of a service instance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Deleting', 'Succeeded', 'Creating', 'Accepted', 'Verifying', 'Updating',
     'Failed', 'Canceled', 'Deprovisioned'
    :vartype provisioning_state: str or
     ~azure.mgmt.healthcareapis.models.ProvisioningState
    :param access_policies: Required. The access policies of the service
     instance.
    :type access_policies:
     list[~azure.mgmt.healthcareapis.models.ServiceAccessPolicyEntry]
    :param cosmos_db_configuration: The settings for the Cosmos DB database
     backing the service.
    :type cosmos_db_configuration:
     ~azure.mgmt.healthcareapis.models.ServiceCosmosDbConfigurationInfo
    :param authentication_configuration: The authentication configuration for
     the service instance.
    :type authentication_configuration:
     ~azure.mgmt.healthcareapis.models.ServiceAuthenticationConfigurationInfo
    :param cors_configuration: The settings for the CORS configuration of the
     service instance.
    :type cors_configuration:
     ~azure.mgmt.healthcareapis.models.ServiceCorsConfigurationInfo
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'access_policies': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'access_policies': {'key': 'accessPolicies', 'type': '[ServiceAccessPolicyEntry]'},
        'cosmos_db_configuration': {'key': 'cosmosDbConfiguration', 'type': 'ServiceCosmosDbConfigurationInfo'},
        'authentication_configuration': {'key': 'authenticationConfiguration', 'type': 'ServiceAuthenticationConfigurationInfo'},
        'cors_configuration': {'key': 'corsConfiguration', 'type': 'ServiceCorsConfigurationInfo'},
    }

    def __init__(self, **kwargs):
        super(ServicesProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.access_policies = kwargs.get('access_policies', None)
        self.cosmos_db_configuration = kwargs.get('cosmos_db_configuration', None)
        self.authentication_configuration = kwargs.get('authentication_configuration', None)
        self.cors_configuration = kwargs.get('cors_configuration', None)
