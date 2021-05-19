# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional, TYPE_CHECKING, Union

from azure.core.pipeline.transport._base import _format_url_section
from azure.purview.scanning.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

_SERIALIZER = Serializer()


def build_create_or_update_request(
    data_source_name: str,
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Creates or Updates a data source.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :keyword json:
    :paramtype json: Any
    :keyword content:
    :paramtype content: Any
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # kind template as part of your input body
            kind = 'AdlsGen1DataSource' or 'AdlsGen2DataSource' or 'AmazonAccountDataSource' or 'AmazonPostgreSqlDataSource' or 'AmazonS3DataSource' or 'AmazonSqlDataSource' or 'AzureCosmosDbDataSource' or 'AzureDataExplorerDataSource' or 'AzureFileServiceDataSource' or 'AzureMySqlDataSource' or 'AzurePostgreSqlDataSource' or 'AzureResourceGroupDataSource' or 'AzureSqlDataWarehouseDataSource' or 'AzureSqlDatabaseDataSource' or 'AzureSqlDatabaseManagedInstanceDataSource' or 'AzureStorageDataSource' or 'AzureSubscriptionDataSource' or 'AzureSynapseDataSource' or 'AzureSynapseWorkspaceDataSource' or 'OracleDataSource' or 'PowerBIDataSource' or 'SapEccDataSource' or 'SapS4HanaDataSource' or 'SqlServerDatabaseDataSource' or 'TeradataDataSource'

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "kind": "DataSource",
                "scans": [
                    {
                        "kind": "Scan",
                        "scanResults": [
                            {
                                "assetsClassified": "long (optional)",
                                "assetsDiscovered": "long (optional)",
                                "dataSourceType": "str (optional)",
                                "diagnostics": {},
                                "endTime": "datetime (optional)",
                                "error": {},
                                "errorMessage": "str (optional)",
                                "id": "str (optional)",
                                "parentId": "str (optional)",
                                "pipelineStartTime": "datetime (optional)",
                                "queuedTime": "datetime (optional)",
                                "resourceId": "str (optional)",
                                "runType": "str (optional)",
                                "scanLevelType": "str (optional)",
                                "scanRulesetType": "str (optional)",
                                "scanRulesetVersion": "int (optional)",
                                "startTime": "datetime (optional)",
                                "status": "str (optional)"
                            }
                        ]
                    }
                ]
            }


            # response body for status code(s): 200, 201
            response_body == {
                "kind": "DataSource",
                "scans": [
                    {
                        "kind": "Scan",
                        "scanResults": [
                            {
                                "assetsClassified": "long (optional)",
                                "assetsDiscovered": "long (optional)",
                                "dataSourceType": "str (optional)",
                                "diagnostics": {},
                                "endTime": "datetime (optional)",
                                "error": {},
                                "errorMessage": "str (optional)",
                                "id": "str (optional)",
                                "parentId": "str (optional)",
                                "pipelineStartTime": "datetime (optional)",
                                "queuedTime": "datetime (optional)",
                                "resourceId": "str (optional)",
                                "runType": "str (optional)",
                                "scanLevelType": "str (optional)",
                                "scanRulesetType": "str (optional)",
                                "scanRulesetVersion": "int (optional)",
                                "startTime": "datetime (optional)",
                                "status": "str (optional)"
                            }
                        ]
                    }
                ]
            }

    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_request(
    data_source_name: str,
    **kwargs: Any
) -> HttpRequest:
    """Get a data source.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "kind": "DataSource",
                "scans": [
                    {
                        "kind": "Scan",
                        "scanResults": [
                            {
                                "assetsClassified": "long (optional)",
                                "assetsDiscovered": "long (optional)",
                                "dataSourceType": "str (optional)",
                                "diagnostics": {},
                                "endTime": "datetime (optional)",
                                "error": {},
                                "errorMessage": "str (optional)",
                                "id": "str (optional)",
                                "parentId": "str (optional)",
                                "pipelineStartTime": "datetime (optional)",
                                "queuedTime": "datetime (optional)",
                                "resourceId": "str (optional)",
                                "runType": "str (optional)",
                                "scanLevelType": "str (optional)",
                                "scanRulesetType": "str (optional)",
                                "scanRulesetVersion": "int (optional)",
                                "startTime": "datetime (optional)",
                                "status": "str (optional)"
                            }
                        ]
                    }
                ]
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    data_source_name: str,
    **kwargs: Any
) -> HttpRequest:
    """Deletes a data source.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "kind": "DataSource",
                "scans": [
                    {
                        "kind": "Scan",
                        "scanResults": [
                            {
                                "assetsClassified": "long (optional)",
                                "assetsDiscovered": "long (optional)",
                                "dataSourceType": "str (optional)",
                                "diagnostics": {},
                                "endTime": "datetime (optional)",
                                "error": {},
                                "errorMessage": "str (optional)",
                                "id": "str (optional)",
                                "parentId": "str (optional)",
                                "pipelineStartTime": "datetime (optional)",
                                "queuedTime": "datetime (optional)",
                                "resourceId": "str (optional)",
                                "runType": "str (optional)",
                                "scanLevelType": "str (optional)",
                                "scanRulesetType": "str (optional)",
                                "scanRulesetVersion": "int (optional)",
                                "startTime": "datetime (optional)",
                                "status": "str (optional)"
                            }
                        ]
                    }
                ]
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_all_request(
    **kwargs: Any
) -> HttpRequest:
    """List data sources in Data catalog.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "count": "long (optional)",
                "nextLink": "str (optional)",
                "value": [
                    {
                        "kind": "DataSource",
                        "scans": [
                            {
                                "kind": "Scan",
                                "scanResults": [
                                    {
                                        "assetsClassified": "long (optional)",
                                        "assetsDiscovered": "long (optional)",
                                        "dataSourceType": "str (optional)",
                                        "diagnostics": {},
                                        "endTime": "datetime (optional)",
                                        "error": {},
                                        "errorMessage": "str (optional)",
                                        "id": "str (optional)",
                                        "parentId": "str (optional)",
                                        "pipelineStartTime": "datetime (optional)",
                                        "queuedTime": "datetime (optional)",
                                        "resourceId": "str (optional)",
                                        "runType": "str (optional)",
                                        "scanLevelType": "str (optional)",
                                        "scanRulesetType": "str (optional)",
                                        "scanRulesetVersion": "int (optional)",
                                        "startTime": "datetime (optional)",
                                        "status": "str (optional)"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

