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

from .image_template_customizer import ImageTemplateCustomizer


class ImageTemplatePowerShellCustomizer(ImageTemplateCustomizer):
    """Runs the specified PowerShell on the VM (Windows). Corresponds to Packer
    powershell provisioner. Exactly one of 'script' or 'inline' can be
    specified.

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param script: The PowerShell script to be run for customizing. It can be
     a github link, SAS URI for Azure Storage, etc
    :type script: str
    :param inline: Array of PowerShell commands to execute
    :type inline: list[str]
    :param valid_exit_codes: Valid exit codes for the PowerShell script.
     [Default: 0]
    :type valid_exit_codes: list[int]
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'inline': {'key': 'inline', 'type': '[str]'},
        'valid_exit_codes': {'key': 'validExitCodes', 'type': '[int]'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplatePowerShellCustomizer, self).__init__(**kwargs)
        self.script = kwargs.get('script', None)
        self.inline = kwargs.get('inline', None)
        self.valid_exit_codes = kwargs.get('valid_exit_codes', None)
        self.type = 'PowerShell'