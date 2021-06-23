# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from ._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, Union

    from azure.core.credentials import TokenCredential


class MapsRenderClientConfiguration(Configuration):
    """Configuration for MapsRenderClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param x_ms_client_id: Specifies which account is intended for usage in conjunction with the Azure AD security model.  It represents a unique ID for the Azure Maps account and can be retrieved from the Azure Maps management  plane Account API. To use Azure AD security in Azure Maps see the following `articles <https://aka.ms/amauthdetails>`_ for guidance.
    :type x_ms_client_id: str
    :param geography: This parameter specifies where the Azure Maps Creator resource is located.  Valid values are us and eu.
    :type geography: str or ~azure.maps.render.models.Geography
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        x_ms_client_id=None,  # type: Optional[str]
        geography="us",  # type: Union[str, "_models.Geography"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if geography is None:
            raise ValueError("Parameter 'geography' must not be None.")
        super(MapsRenderClientConfiguration, self).__init__(**kwargs)

        self.credential = credential
        self.x_ms_client_id = x_ms_client_id
        self.geography = geography
        self.credential_scopes = kwargs.pop('credential_scopes', ['https://atlas.microsoft.com/.default'])
        kwargs.setdefault('sdk_moniker', 'maps-render/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
