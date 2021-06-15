# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CheckAccessDecision(msrest.serialization.Model):
    """Check access response details.

    :param access_decision: Access Decision.
    :type access_decision: str
    :param action_id: Action Id.
    :type action_id: str
    :param role_assignment: Role Assignment response details.
    :type role_assignment: ~azure.synapse.accesscontrol.models.RoleAssignmentDetails
    """

    _attribute_map = {
        "access_decision": {"key": "accessDecision", "type": "str"},
        "action_id": {"key": "actionId", "type": "str"},
        "role_assignment": {"key": "roleAssignment", "type": "RoleAssignmentDetails"},
    }

    def __init__(self, **kwargs):
        super(CheckAccessDecision, self).__init__(**kwargs)
        self.access_decision = kwargs.get("access_decision", None)
        self.action_id = kwargs.get("action_id", None)
        self.role_assignment = kwargs.get("role_assignment", None)


class CheckPrincipalAccessRequest(msrest.serialization.Model):
    """Check access request details.

    All required parameters must be populated in order to send to Azure.

    :param subject: Required. Subject details.
    :type subject: ~azure.synapse.accesscontrol.models.SubjectInfo
    :param actions: Required. List of actions.
    :type actions: list[~azure.synapse.accesscontrol.models.RequiredAction]
    :param scope: Required. Scope at which the check access is done.
    :type scope: str
    """

    _validation = {
        "subject": {"required": True},
        "actions": {"required": True},
        "scope": {"required": True},
    }

    _attribute_map = {
        "subject": {"key": "subject", "type": "SubjectInfo"},
        "actions": {"key": "actions", "type": "[RequiredAction]"},
        "scope": {"key": "scope", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(CheckPrincipalAccessRequest, self).__init__(**kwargs)
        self.subject = kwargs["subject"]
        self.actions = kwargs["actions"]
        self.scope = kwargs["scope"]


class CheckPrincipalAccessResponse(msrest.serialization.Model):
    """Check access response details.

    :param access_decisions: To check if the current user, group, or service principal has
     permission to read artifacts in the specified workspace.
    :type access_decisions: list[~azure.synapse.accesscontrol.models.CheckAccessDecision]
    """

    _attribute_map = {
        "access_decisions": {"key": "accessDecisions", "type": "[CheckAccessDecision]"},
    }

    def __init__(self, **kwargs):
        super(CheckPrincipalAccessResponse, self).__init__(**kwargs)
        self.access_decisions = kwargs.get("access_decisions", None)


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorContract(msrest.serialization.Model):
    """Contains details when the response code indicates an error.

    :param error: The error details.
    :type error: ~azure.synapse.accesscontrol.models.ErrorResponse
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorResponse"},
    }

    def __init__(self, **kwargs):
        super(ErrorContract, self).__init__(**kwargs)
        self.error = kwargs.get("error", None)


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.synapse.accesscontrol.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.synapse.accesscontrol.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorResponse]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class RequiredAction(msrest.serialization.Model):
    """Action Info.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Action Id.
    :type id: str
    :param is_data_action: Required. Is a data action or not.
    :type is_data_action: bool
    """

    _validation = {
        "id": {"required": True},
        "is_data_action": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "is_data_action": {"key": "isDataAction", "type": "bool"},
    }

    def __init__(self, **kwargs):
        super(RequiredAction, self).__init__(**kwargs)
        self.id = kwargs["id"]
        self.is_data_action = kwargs["is_data_action"]


class RoleAssignmentDetails(msrest.serialization.Model):
    """Role Assignment response details.

    :param id: Role Assignment ID.
    :type id: str
    :param role_definition_id: Role ID of the Synapse Built-In Role.
    :type role_definition_id: str
    :param principal_id: Object ID of the AAD principal or security-group.
    :type principal_id: str
    :param scope: Scope at the role assignment is created.
    :type scope: str
    :param principal_type: Type of the principal Id: User, Group or ServicePrincipal.
    :type principal_type: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "role_definition_id": {"key": "roleDefinitionId", "type": "str"},
        "principal_id": {"key": "principalId", "type": "str"},
        "scope": {"key": "scope", "type": "str"},
        "principal_type": {"key": "principalType", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentDetails, self).__init__(**kwargs)
        self.id = kwargs.get("id", None)
        self.role_definition_id = kwargs.get("role_definition_id", None)
        self.principal_id = kwargs.get("principal_id", None)
        self.scope = kwargs.get("scope", None)
        self.principal_type = kwargs.get("principal_type", None)


class RoleAssignmentDetailsList(msrest.serialization.Model):
    """Role Assignment response details.

    :param count: Number of role assignments.
    :type count: int
    :param value: A list of role assignments.
    :type value: list[~azure.synapse.accesscontrol.models.RoleAssignmentDetails]
    """

    _attribute_map = {
        "count": {"key": "count", "type": "int"},
        "value": {"key": "value", "type": "[RoleAssignmentDetails]"},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentDetailsList, self).__init__(**kwargs)
        self.count = kwargs.get("count", None)
        self.value = kwargs.get("value", None)


class RoleAssignmentRequest(msrest.serialization.Model):
    """Role Assignment request details.

    All required parameters must be populated in order to send to Azure.

    :param role_id: Required. Role ID of the Synapse Built-In Role.
    :type role_id: str
    :param principal_id: Required. Object ID of the AAD principal or security-group.
    :type principal_id: str
    :param scope: Required. Scope at which the role assignment is created.
    :type scope: str
    :param principal_type: Type of the principal Id: User, Group or ServicePrincipal.
    :type principal_type: str
    """

    _validation = {
        "role_id": {"required": True},
        "principal_id": {"required": True},
        "scope": {"required": True},
    }

    _attribute_map = {
        "role_id": {"key": "roleId", "type": "str"},
        "principal_id": {"key": "principalId", "type": "str"},
        "scope": {"key": "scope", "type": "str"},
        "principal_type": {"key": "principalType", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentRequest, self).__init__(**kwargs)
        self.role_id = kwargs["role_id"]
        self.principal_id = kwargs["principal_id"]
        self.scope = kwargs["scope"]
        self.principal_type = kwargs.get("principal_type", None)


class SubjectInfo(msrest.serialization.Model):
    """Subject details.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. Principal Id.
    :type principal_id: str
    :param group_ids: List of group Ids that the principalId is part of.
    :type group_ids: list[str]
    """

    _validation = {
        "principal_id": {"required": True},
    }

    _attribute_map = {
        "principal_id": {"key": "principalId", "type": "str"},
        "group_ids": {"key": "groupIds", "type": "[str]"},
    }

    def __init__(self, **kwargs):
        super(SubjectInfo, self).__init__(**kwargs)
        self.principal_id = kwargs["principal_id"]
        self.group_ids = kwargs.get("group_ids", None)


class SynapseRbacPermission(msrest.serialization.Model):
    """Synapse role definition details.

    :param actions: List of actions.
    :type actions: list[str]
    :param not_actions: List of Not actions.
    :type not_actions: list[str]
    :param data_actions: List of data actions.
    :type data_actions: list[str]
    :param not_data_actions: List of Not data actions.
    :type not_data_actions: list[str]
    """

    _attribute_map = {
        "actions": {"key": "actions", "type": "[str]"},
        "not_actions": {"key": "notActions", "type": "[str]"},
        "data_actions": {"key": "dataActions", "type": "[str]"},
        "not_data_actions": {"key": "notDataActions", "type": "[str]"},
    }

    def __init__(self, **kwargs):
        super(SynapseRbacPermission, self).__init__(**kwargs)
        self.actions = kwargs.get("actions", None)
        self.not_actions = kwargs.get("not_actions", None)
        self.data_actions = kwargs.get("data_actions", None)
        self.not_data_actions = kwargs.get("not_data_actions", None)


class SynapseRoleDefinition(msrest.serialization.Model):
    """Synapse role definition details.

    :param id: Role Definition ID.
    :type id: str
    :param name: Name of the Synapse role.
    :type name: str
    :param is_built_in: Is a built-in role or not.
    :type is_built_in: bool
    :param description: Description for the Synapse role.
    :type description: str
    :param permissions: Permissions for the Synapse role.
    :type permissions: list[~azure.synapse.accesscontrol.models.SynapseRbacPermission]
    :param scopes: Allowed scopes for the Synapse role.
    :type scopes: list[str]
    :param availability_status: Availability of the Synapse role.
    :type availability_status: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "is_built_in": {"key": "isBuiltIn", "type": "bool"},
        "description": {"key": "description", "type": "str"},
        "permissions": {"key": "permissions", "type": "[SynapseRbacPermission]"},
        "scopes": {"key": "scopes", "type": "[str]"},
        "availability_status": {"key": "availabilityStatus", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SynapseRoleDefinition, self).__init__(**kwargs)
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)
        self.is_built_in = kwargs.get("is_built_in", None)
        self.description = kwargs.get("description", None)
        self.permissions = kwargs.get("permissions", None)
        self.scopes = kwargs.get("scopes", None)
        self.availability_status = kwargs.get("availability_status", None)
