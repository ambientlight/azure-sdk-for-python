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


class RegistryPolicies(Model):
    """An object that represents policies for a container registry.

    :param quarantine_policy: An object that represents quarantine policy for
     a container registry.
    :type quarantine_policy:
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.QuarantinePolicy
    :param trust_policy: An object that represents content trust policy for a
     container registry.
    :type trust_policy:
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.TrustPolicy
    """

    _attribute_map = {
        'quarantine_policy': {'key': 'quarantinePolicy', 'type': 'QuarantinePolicy'},
        'trust_policy': {'key': 'trustPolicy', 'type': 'TrustPolicy'},
    }

    def __init__(self, *, quarantine_policy=None, trust_policy=None, **kwargs) -> None:
        super(RegistryPolicies, self).__init__(**kwargs)
        self.quarantine_policy = quarantine_policy
        self.trust_policy = trust_policy
