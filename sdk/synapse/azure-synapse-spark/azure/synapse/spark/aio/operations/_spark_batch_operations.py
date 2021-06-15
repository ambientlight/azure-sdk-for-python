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
from ...rest import spark_batch as rest_spark_batch

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SparkBatchOperations:
    """SparkBatchOperations async operations.

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

    async def get_spark_batch_jobs(
        self,
        *,
        from_parameter: Optional[int] = None,
        size: Optional[int] = None,
        detailed: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.SparkBatchJobCollection":
        """List all spark batch jobs which are running under a particular spark pool.

        :keyword from_parameter: Optional param specifying which index the list should begin from.
        :paramtype from_parameter: int
        :keyword size: Optional param specifying the size of the returned list.
                     By default it is 20 and that is the maximum.
        :paramtype size: int
        :keyword detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :paramtype detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkBatchJobCollection, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkBatchJobCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkBatchJobCollection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_batch.build_get_spark_batch_jobs_request(
            spark_pool_name=self._config.spark_pool_name,
            livy_api_version=self._config.livy_api_version,
            from_parameter=from_parameter,
            size=size,
            detailed=detailed,
            template_url=self.get_spark_batch_jobs.metadata["url"],
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

        deserialized = self._deserialize("SparkBatchJobCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_batch_jobs.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches"}  # type: ignore

    async def create_spark_batch_job(
        self, spark_batch_job_options: "_models.SparkBatchJobOptions", *, detailed: Optional[bool] = None, **kwargs: Any
    ) -> "_models.SparkBatchJob":
        """Create new spark batch job.

        :param spark_batch_job_options: Livy compatible batch job request payload.
        :type spark_batch_job_options: ~azure.synapse.spark.models.SparkBatchJobOptions
        :keyword detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :paramtype detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkBatchJob, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkBatchJob
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkBatchJob"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(spark_batch_job_options, "object")

        request = rest_spark_batch.build_create_spark_batch_job_request(
            spark_pool_name=self._config.spark_pool_name,
            livy_api_version=self._config.livy_api_version,
            detailed=detailed,
            json=json,
            content_type=content_type,
            template_url=self.create_spark_batch_job.metadata["url"],
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

        deserialized = self._deserialize("SparkBatchJob", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_spark_batch_job.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches"}  # type: ignore

    async def get_spark_batch_job(
        self, batch_id: int, *, detailed: Optional[bool] = None, **kwargs: Any
    ) -> "_models.SparkBatchJob":
        """Gets a single spark batch job.

        :param batch_id: Identifier for the batch job.
        :type batch_id: int
        :keyword detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :paramtype detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkBatchJob, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkBatchJob
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkBatchJob"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_batch.build_get_spark_batch_job_request(
            spark_pool_name=self._config.spark_pool_name,
            batch_id=batch_id,
            livy_api_version=self._config.livy_api_version,
            detailed=detailed,
            template_url=self.get_spark_batch_job.metadata["url"],
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

        deserialized = self._deserialize("SparkBatchJob", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_batch_job.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches/{batchId}"}  # type: ignore

    async def cancel_spark_batch_job(self, batch_id: int, **kwargs: Any) -> None:
        """Cancels a running spark batch job.

        :param batch_id: Identifier for the batch job.
        :type batch_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_spark_batch.build_cancel_spark_batch_job_request(
            spark_pool_name=self._config.spark_pool_name,
            batch_id=batch_id,
            livy_api_version=self._config.livy_api_version,
            template_url=self.cancel_spark_batch_job.metadata["url"],
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

    cancel_spark_batch_job.metadata = {"url": "/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches/{batchId}"}  # type: ignore
