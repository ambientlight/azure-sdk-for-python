# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.synapse.spark.core.rest import HttpRequest

from ... import models as _models
from ...rest import spark_session as rest_spark_session

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SparkSessionOperations:
    """SparkSessionOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.spark.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_spark_sessions(
        self,
        *,
        from_parameter: Optional[int] = None,
        size: Optional[int] = None,
        detailed: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.SparkSessionCollection":
        """List all spark sessions which are running under a particular spark pool.

        :keyword from_parameter: Optional param specifying which index the list should begin from.
        :paramtype from_parameter: int
        :keyword size: Optional param specifying the size of the returned list.
                     By default it is 20 and that is the maximum.
        :paramtype size: int
        :keyword detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :paramtype detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkSessionCollection, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkSessionCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkSessionCollection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_get_spark_sessions_request(
            spark_pool_name=self._config.spark_pool_name,
            livy_api_version=self._config.livy_api_version,
            from_parameter=from_parameter,
            size=size,
            detailed=detailed,
            template_url=self.get_spark_sessions.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkSessionCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_sessions.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions"}  # type: ignore

    async def create_spark_session(
        self, spark_session_options: "_models.SparkSessionOptions", *, detailed: Optional[bool] = None, **kwargs: Any
    ) -> "_models.SparkSession":
        """Create new spark session.

        :param spark_session_options: Livy compatible batch job request payload.
        :type spark_session_options: ~azure.synapse.spark.models.SparkSessionOptions
        :keyword detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :paramtype detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkSession, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkSession"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(spark_session_options, "object")

        request = rest_spark_session.build_create_spark_session_request(
            spark_pool_name=self._config.spark_pool_name,
            livy_api_version=self._config.livy_api_version,
            detailed=detailed,
            json=json,
            content_type=content_type,
            template_url=self.create_spark_session.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkSession", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_spark_session.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions"}  # type: ignore

    async def get_spark_session(
        self, session_id: int, *, detailed: Optional[bool] = None, **kwargs: Any
    ) -> "_models.SparkSession":
        """Gets a single spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :keyword detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :paramtype detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkSession, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkSession"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_get_spark_session_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            livy_api_version=self._config.livy_api_version,
            detailed=detailed,
            template_url=self.get_spark_session.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkSession", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_session.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}"}  # type: ignore

    async def cancel_spark_session(self, session_id: int, **kwargs: Any) -> None:
        """Cancels a running spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_cancel_spark_session_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            livy_api_version=self._config.livy_api_version,
            template_url=self.cancel_spark_session.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_spark_session.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}"}  # type: ignore

    async def reset_spark_session_timeout(self, session_id: int, **kwargs: Any) -> None:
        """Sends a keep alive call to the current session to reset the session timeout.

        :param session_id: Identifier for the session.
        :type session_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_reset_spark_session_timeout_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            livy_api_version=self._config.livy_api_version,
            template_url=self.reset_spark_session_timeout.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    reset_spark_session_timeout.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/reset-timeout"}  # type: ignore

    async def get_spark_statements(self, session_id: int, **kwargs: Any) -> "_models.SparkStatementCollection":
        """Gets a list of statements within a spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatementCollection, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatementCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkStatementCollection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_get_spark_statements_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            livy_api_version=self._config.livy_api_version,
            template_url=self.get_spark_statements.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkStatementCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_statements.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements"}  # type: ignore

    async def create_spark_statement(
        self, session_id: int, spark_statement_options: "_models.SparkStatementOptions", **kwargs: Any
    ) -> "_models.SparkStatement":
        """Create statement within a spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param spark_statement_options: Livy compatible batch job request payload.
        :type spark_statement_options: ~azure.synapse.spark.models.SparkStatementOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatement, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatement
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkStatement"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(spark_statement_options, "object")

        request = rest_spark_session.build_create_spark_statement_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            livy_api_version=self._config.livy_api_version,
            json=json,
            content_type=content_type,
            template_url=self.create_spark_statement.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkStatement", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_spark_statement.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements"}  # type: ignore

    async def get_spark_statement(self, session_id: int, statement_id: int, **kwargs: Any) -> "_models.SparkStatement":
        """Gets a single statement within a spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param statement_id: Identifier for the statement.
        :type statement_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatement, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatement
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkStatement"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_get_spark_statement_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            statement_id=statement_id,
            livy_api_version=self._config.livy_api_version,
            template_url=self.get_spark_statement.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkStatement", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_statement.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements/{statementId}"}  # type: ignore

    async def cancel_spark_statement(
        self, session_id: int, statement_id: int, **kwargs: Any
    ) -> "_models.SparkStatementCancellationResult":
        """Kill a statement within a session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param statement_id: Identifier for the statement.
        :type statement_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatementCancellationResult, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatementCancellationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkStatementCancellationResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_session.build_cancel_spark_statement_request(
            spark_pool_name=self._config.spark_pool_name,
            session_id=session_id,
            statement_id=statement_id,
            livy_api_version=self._config.livy_api_version,
            template_url=self.cancel_spark_statement.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkStatementCancellationResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    cancel_spark_statement.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements/{statementId}/cancel"}  # type: ignore
