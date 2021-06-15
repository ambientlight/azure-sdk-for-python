# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer
from azure.synapse.accesscontrol.core.rest import _StreamContextManager


if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential
    from azure.synapse.accesscontrol.core.rest import HttpRequest, HttpResponse

from ._configuration import AccessControlClientConfiguration
from .operations import RoleAssignmentsOperations
from .operations import RoleDefinitionsOperations
from . import models


class AccessControlClient(object):
    """AccessControlClient.

    :ivar role_assignments: RoleAssignmentsOperations operations
    :vartype role_assignments: azure.synapse.accesscontrol.operations.RoleAssignmentsOperations
    :ivar role_definitions: RoleDefinitionsOperations operations
    :vartype role_definitions: azure.synapse.accesscontrol.operations.RoleDefinitionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param endpoint: The workspace development endpoint, for example https://myworkspace.dev.azuresynapse.net.
    :type endpoint: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        endpoint,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = "{endpoint}"
        self._config = AccessControlClientConfiguration(credential, endpoint, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.role_definitions = RoleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.synapse.accesscontrol.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.synapse.accesscontrol.rest import build_check_principal_access_request
        >>> request = build_check_principal_access_request(json, content)
        <HttpRequest [POST], url: '/checkAccessSynapseRbac'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.synapse.accesscontrol.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.synapse.accesscontrol.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.synapse.accesscontrol.core.rest.HttpResponse
        """
        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        if kwargs.pop("stream", False):
            return _StreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = HttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )
        response.read()
        return response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AccessControlClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
