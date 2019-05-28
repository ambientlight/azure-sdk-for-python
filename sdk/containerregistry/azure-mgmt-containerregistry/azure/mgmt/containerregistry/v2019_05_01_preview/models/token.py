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

from .proxy_resource import ProxyResource


class Token(ProxyResource):
    """An object that represents a token for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar creation_date: The creation date of scope map.
    :vartype creation_date: datetime
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Failed',
     'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.ProvisioningState
    :param scope_map_id: The resource ID of the scope map to which the token
     will be associated with.
    :type scope_map_id: str
    :param object_id: The user/group/application object ID for which the token
     has to be created.
    :type object_id: str
    :param credentials: The credentials that can be used for authenticating
     the token.
    :type credentials:
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.TokenCredentialsProperties
    :param status: The status of the token example enabled or disabled.
     Possible values include: 'enabled', 'disabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.Status
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'creation_date': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'scope_map_id': {'key': 'properties.scopeMapId', 'type': 'str'},
        'object_id': {'key': 'properties.objectId', 'type': 'str'},
        'credentials': {'key': 'properties.credentials', 'type': 'TokenCredentialsProperties'},
        'status': {'key': 'properties.status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Token, self).__init__(**kwargs)
        self.creation_date = None
        self.provisioning_state = None
        self.scope_map_id = kwargs.get('scope_map_id', None)
        self.object_id = kwargs.get('object_id', None)
        self.credentials = kwargs.get('credentials', None)
        self.status = kwargs.get('status', None)
