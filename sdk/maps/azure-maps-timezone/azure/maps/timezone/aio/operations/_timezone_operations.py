# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TimezoneOperations:
    """TimezoneOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.maps.timezone.models
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

    async def get_timezone_by_id(
        self,
        format: Union[str, "_models.ResponseFormat"],
        query: str,
        accept_language: Optional[str] = None,
        options: Optional[Union[str, "_models.TimezoneOptions"]] = None,
        time_stamp: Optional[datetime.datetime] = None,
        transitions_from: Optional[datetime.datetime] = None,
        transitions_years: Optional[int] = None,
        **kwargs: Any
    ) -> "_models.TimezoneByIdResult":
        """**Time Zone by Id**

        **Applies to**\ : S0 and S1 pricing tiers.

        This API returns current, historical, and future time zone information for the specified IANA
        time zone ID.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.timezone.models.ResponseFormat
        :param query: The IANA time zone ID.
        :type query: str
        :param accept_language: Specifies the language code in which the timezone names should be
         returned. If no language code is provided, the response will be in "EN". Please refer to
         `Supported Languages <https://docs.microsoft.com/en-us/azure/azure-maps/supported-languages>`_
         for details.
        :type accept_language: str
        :param options: Alternatively, use alias "o". Options available for types of information
         returned in the result.
        :type options: str or ~azure.maps.timezone.models.TimezoneOptions
        :param time_stamp: Alternatively, use alias "stamp", or "s". Reference time, if omitted, the
         API will use the machine time serving the request.
        :type time_stamp: ~datetime.datetime
        :param transitions_from: Alternatively, use alias "tf". The start date from which daylight
         savings time (DST) transitions are requested, only applies when "options" = all or "options" =
         transitions.
        :type transitions_from: ~datetime.datetime
        :param transitions_years: Alternatively, use alias "ty". The number of years from
         "transitionsFrom" for which DST transitions are requested, only applies when "options" = all or
         "options" = transitions.
        :type transitions_years: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TimezoneByIdResult, or the result of cls(response)
        :rtype: ~azure.maps.timezone.models.TimezoneByIdResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TimezoneByIdResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json"

        # Construct URL
        url = self.get_timezone_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'format': self._serialize.url("format", format, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if options is not None:
            query_parameters['options'] = self._serialize.query("options", options, 'str')
        if time_stamp is not None:
            query_parameters['timeStamp'] = self._serialize.query("time_stamp", time_stamp, 'iso-8601')
        if transitions_from is not None:
            query_parameters['transitionsFrom'] = self._serialize.query("transitions_from", transitions_from, 'iso-8601')
        if transitions_years is not None:
            query_parameters['transitionsYears'] = self._serialize.query("transitions_years", transitions_years, 'int')
        query_parameters['query'] = self._serialize.query("query", query, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        if accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("accept_language", accept_language, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TimezoneByIdResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_timezone_by_id.metadata = {'url': '/timezone/byId/{format}'}  # type: ignore

    async def get_timezone_by_coordinates(
        self,
        format: Union[str, "_models.ResponseFormat"],
        query: str,
        accept_language: Optional[str] = None,
        options: Optional[Union[str, "_models.TimezoneOptions"]] = None,
        time_stamp: Optional[datetime.datetime] = None,
        transitions_from: Optional[datetime.datetime] = None,
        transitions_years: Optional[int] = None,
        **kwargs: Any
    ) -> "_models.TimezoneByCoordinatesResult":
        """**Time Zone by Coordinates**

        **Applies to**\ : S0 and S1 pricing tiers.

        This API returns current, historical, and future time zone information for a specified
        latitude-longitude pair. In addition, the API provides sunset and sunrise times for a given
        location.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.timezone.models.ResponseFormat
        :param query: Coordinates of the point for which time zone information is requested. The
         applicable query is specified as a comma separated string composed by latitude followed by
         longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param accept_language: Specifies the language code in which the timezone names should be
         returned. If no language code is provided, the response will be in "EN". Please refer to
         `Supported Languages <https://docs.microsoft.com/en-us/azure/azure-maps/supported-languages>`_
         for details.
        :type accept_language: str
        :param options: Alternatively, use alias "o". Options available for types of information
         returned in the result.
        :type options: str or ~azure.maps.timezone.models.TimezoneOptions
        :param time_stamp: Alternatively, use alias "stamp", or "s". Reference time, if omitted, the
         API will use the machine time serving the request.
        :type time_stamp: ~datetime.datetime
        :param transitions_from: Alternatively, use alias "tf". The start date from which daylight
         savings time (DST) transitions are requested, only applies when "options" = all or "options" =
         transitions.
        :type transitions_from: ~datetime.datetime
        :param transitions_years: Alternatively, use alias "ty". The number of years from
         "transitionsFrom" for which DST transitions are requested, only applies when "options" = all or
         "options" = transitions.
        :type transitions_years: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TimezoneByCoordinatesResult, or the result of cls(response)
        :rtype: ~azure.maps.timezone.models.TimezoneByCoordinatesResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TimezoneByCoordinatesResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json"

        # Construct URL
        url = self.get_timezone_by_coordinates.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'format': self._serialize.url("format", format, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if options is not None:
            query_parameters['options'] = self._serialize.query("options", options, 'str')
        if time_stamp is not None:
            query_parameters['timeStamp'] = self._serialize.query("time_stamp", time_stamp, 'iso-8601')
        if transitions_from is not None:
            query_parameters['transitionsFrom'] = self._serialize.query("transitions_from", transitions_from, 'iso-8601')
        if transitions_years is not None:
            query_parameters['transitionsYears'] = self._serialize.query("transitions_years", transitions_years, 'int')
        query_parameters['query'] = self._serialize.query("query", query, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        if accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("accept_language", accept_language, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TimezoneByCoordinatesResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_timezone_by_coordinates.metadata = {'url': '/timezone/byCoordinates/{format}'}  # type: ignore

    async def get_timezone_enum_windows(
        self,
        format: Union[str, "_models.ResponseFormat"],
        **kwargs: Any
    ) -> List["_models.TimezoneEnumWindow"]:
        """**Enumerate Windows Time Zones**

        **Applies to**\ : S0 and S1 pricing tiers.

        This API returns a full list of Windows Time Zone IDs.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.timezone.models.ResponseFormat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of TimezoneEnumWindow, or the result of cls(response)
        :rtype: list[~azure.maps.timezone.models.TimezoneEnumWindow]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.TimezoneEnumWindow"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json"

        # Construct URL
        url = self.get_timezone_enum_windows.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'format': self._serialize.url("format", format, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[TimezoneEnumWindow]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_timezone_enum_windows.metadata = {'url': '/timezone/enumWindows/{format}'}  # type: ignore

    async def get_timezone_enum_iana(
        self,
        format: Union[str, "_models.ResponseFormat"],
        **kwargs: Any
    ) -> List["_models.IanaId"]:
        """**Enumerate IANA Time Zones**

        **Applies to**\ : S0 and S1 pricing tiers.

        This API returns a full list of IANA time zone IDs. Updates to the IANA service will be
        reflected in the system within one day.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.timezone.models.ResponseFormat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of IanaId, or the result of cls(response)
        :rtype: list[~azure.maps.timezone.models.IanaId]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.IanaId"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json"

        # Construct URL
        url = self.get_timezone_enum_iana.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'format': self._serialize.url("format", format, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[IanaId]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_timezone_enum_iana.metadata = {'url': '/timezone/enumIana/{format}'}  # type: ignore

    async def get_timezone_iana_version(
        self,
        format: Union[str, "_models.ResponseFormat"],
        **kwargs: Any
    ) -> "_models.TimezoneIanaVersionResult":
        """**Time Zone IANA Version**

        **Applies to**\ : S0 and S1 pricing tiers.

        This API returns the current IANA version number.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.timezone.models.ResponseFormat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TimezoneIanaVersionResult, or the result of cls(response)
        :rtype: ~azure.maps.timezone.models.TimezoneIanaVersionResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TimezoneIanaVersionResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json"

        # Construct URL
        url = self.get_timezone_iana_version.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'format': self._serialize.url("format", format, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TimezoneIanaVersionResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_timezone_iana_version.metadata = {'url': '/timezone/ianaVersion/{format}'}  # type: ignore

    async def get_timezone_windows_to_iana(
        self,
        format: Union[str, "_models.ResponseFormat"],
        query: str,
        territory: Optional[str] = None,
        **kwargs: Any
    ) -> List["_models.IanaId"]:
        """**Windows to IANA Time Zone**

        **Applies to**\ : S0 and S1 pricing tiers.

        This API returns a corresponding IANA ID, given a valid Windows Time Zone ID. Multiple IANA IDs
        may be returned for a single Windows ID. It is possible to narrow these results by adding an
        optional territory parameter.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.timezone.models.ResponseFormat
        :param query: The Windows time zone ID.
        :type query: str
        :param territory: Windows Time Zone territory code.
        :type territory: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of IanaId, or the result of cls(response)
        :rtype: list[~azure.maps.timezone.models.IanaId]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.IanaId"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json"

        # Construct URL
        url = self.get_timezone_windows_to_iana.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'format': self._serialize.url("format", format, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        query_parameters['query'] = self._serialize.query("query", query, 'str')
        if territory is not None:
            query_parameters['territory'] = self._serialize.query("territory", territory, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[IanaId]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_timezone_windows_to_iana.metadata = {'url': '/timezone/windowsToIana/{format}'}  # type: ignore
