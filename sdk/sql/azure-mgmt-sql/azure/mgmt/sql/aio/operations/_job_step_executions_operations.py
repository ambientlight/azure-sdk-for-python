# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class JobStepExecutionsOperations:
    """JobStepExecutionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.sql.models
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

    def list_by_job_execution(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        create_time_min: Optional[datetime.datetime] = None,
        create_time_max: Optional[datetime.datetime] = None,
        end_time_min: Optional[datetime.datetime] = None,
        end_time_max: Optional[datetime.datetime] = None,
        is_active: Optional[bool] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs
    ) -> AsyncIterable["_models.JobExecutionListResult"]:
        """Lists the step executions of a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :param job_execution_id: The id of the job execution.
        :type job_execution_id: str
        :param create_time_min: If specified, only job executions created at or after the specified
         time are included.
        :type create_time_min: ~datetime.datetime
        :param create_time_max: If specified, only job executions created before the specified time are
         included.
        :type create_time_max: ~datetime.datetime
        :param end_time_min: If specified, only job executions completed at or after the specified time
         are included.
        :type end_time_min: ~datetime.datetime
        :param end_time_max: If specified, only job executions completed before the specified time are
         included.
        :type end_time_max: ~datetime.datetime
        :param is_active: If specified, only active or only completed job executions are included.
        :type is_active: bool
        :param skip: The number of elements in the collection to skip.
        :type skip: int
        :param top: The number of elements to return from the collection.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobExecutionListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.JobExecutionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.JobExecutionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_job_execution.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'serverName': self._serialize.url("server_name", server_name, 'str'),
                    'jobAgentName': self._serialize.url("job_agent_name", job_agent_name, 'str'),
                    'jobName': self._serialize.url("job_name", job_name, 'str'),
                    'jobExecutionId': self._serialize.url("job_execution_id", job_execution_id, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if create_time_min is not None:
                    query_parameters['createTimeMin'] = self._serialize.query("create_time_min", create_time_min, 'iso-8601')
                if create_time_max is not None:
                    query_parameters['createTimeMax'] = self._serialize.query("create_time_max", create_time_max, 'iso-8601')
                if end_time_min is not None:
                    query_parameters['endTimeMin'] = self._serialize.query("end_time_min", end_time_min, 'iso-8601')
                if end_time_max is not None:
                    query_parameters['endTimeMax'] = self._serialize.query("end_time_max", end_time_max, 'iso-8601')
                if is_active is not None:
                    query_parameters['isActive'] = self._serialize.query("is_active", is_active, 'bool')
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('JobExecutionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_job_execution.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        step_name: str,
        **kwargs
    ) -> "_models.JobExecution":
        """Gets a step execution of a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :param job_execution_id: The unique id of the job execution.
        :type job_execution_id: str
        :param step_name: The name of the step.
        :type step_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobExecution, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.JobExecution
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.JobExecution"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serverName': self._serialize.url("server_name", server_name, 'str'),
            'jobAgentName': self._serialize.url("job_agent_name", job_agent_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str'),
            'jobExecutionId': self._serialize.url("job_execution_id", job_execution_id, 'str'),
            'stepName': self._serialize.url("step_name", step_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JobExecution', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName}'}  # type: ignore
