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


class GitHubAccessTokenRequest(Model):
    """Get GitHub access token request definition.

    All required parameters must be populated in order to send to Azure.

    :param git_hub_access_code: Required. GitHub access code.
    :type git_hub_access_code: str
    :param git_hub_client_id: GitHub application client ID.
    :type git_hub_client_id: str
    :param git_hub_access_token_base_url: Required. GitHub access token base
     URL.
    :type git_hub_access_token_base_url: str
    """

    _validation = {
        'git_hub_access_code': {'required': True},
        'git_hub_access_token_base_url': {'required': True},
    }

    _attribute_map = {
        'git_hub_access_code': {'key': 'gitHubAccessCode', 'type': 'str'},
        'git_hub_client_id': {'key': 'gitHubClientId', 'type': 'str'},
        'git_hub_access_token_base_url': {'key': 'gitHubAccessTokenBaseUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GitHubAccessTokenRequest, self).__init__(**kwargs)
        self.git_hub_access_code = kwargs.get('git_hub_access_code', None)
        self.git_hub_client_id = kwargs.get('git_hub_client_id', None)
        self.git_hub_access_token_base_url = kwargs.get('git_hub_access_token_base_url', None)
