# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ConversionOperations(object):
    """ConversionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.maps.conversion.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _convert_initial(
        self,
        udid,  # type: str
        output_ontology,  # type: str
        description=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LongRunningOperationResult"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LongRunningOperationResult"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0"
        accept = "application/json"

        # Construct URL
        url = self._convert_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        query_parameters['udid'] = self._serialize.query("udid", udid, 'str')
        query_parameters['outputOntology'] = self._serialize.query("output_ontology", output_ontology, 'str')
        if description is not None:
            query_parameters['description'] = self._serialize.query("description", description, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            response_headers['Resource-Location']=self._deserialize('str', response.headers.get('Resource-Location'))
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _convert_initial.metadata = {'url': '/conversions'}  # type: ignore

    def begin_convert(
        self,
        udid,  # type: str
        output_ontology,  # type: str
        description=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LongRunningOperationResult"]
        """**Applies to:** see pricing `tiers <https://aka.ms/AzureMapsPricingTier>`_.

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API and SDK. `This
        <https://docs.microsoft.com/azure/azure-maps/creator-indoor-maps>`_ article introduces concepts
        and tools that apply to Azure Maps Creator.

        The Conversion API lets the caller import a set of DWG design files as a zipped `Drawing
        Package <https://aka.ms/am-drawing-package>`_ into Azure Maps. The `Drawing Package
        <https://aka.ms/am-drawing-package>`_ should first be uploaded using the `Azure Maps Data
        Service <https://docs.microsoft.com/rest/api/maps/data>`_. Once uploaded, use the ``udid``
        returned by the `Data Upload API
        <https://docs.microsoft.com/rest/api/maps/data/uploadpreview>`_ to call this Conversion API.

        Convert DWG package
        -------------------

        The Conversion API performs a `long-running request <https://aka.ms/am-creator-lrt-v2>`_.

        Debug DWG package issues
        ------------------------

        During the Conversion process, if there are any issues with the DWG package `errors and
        warnings <https://aka.ms/am-conversion-errors>`_ are provided in the response along with a
        *diagnostic package* to visualize and diagnose these issues. In case any issues are encountered
        with your DWG package, the Conversion operation status process as detailed `here
        <https://aka.ms/am-creator-lrt-v2>`_ returns the location of the *diagnostic package* that can
        be downloaded by the caller to help them visualize and diagnose these issues. The *diagnostic
        package* location can be found in the properties section of the conversion operation status
        response and looks like the following:

        .. code-block:: json

           {
               "properties": {
                   "diagnosticPackageLocation":
        "https://us.atlas.microsoft.com/mapdata/{DiagnosticPackageId}?api-version=1.0"
               }
           }

        The *diagnostic package* can be downloaded by executing a ``HTTP GET`` request on the
        ``diagnosticPackageLocation``.
        For more details on how to use the tool to visualize and diagnose all the errors and warnings
        see `Drawing Error Visualizer <https://aka.ms/am-drawing-errors-visualizer>`_. :code:`<br>`

        A conversion operation will be marked as *success* if there are zero or more warnings but will
        be marked as *failed* if any errors are encountered.

        :param udid: The unique data id for the content. The ``udid`` must have been obtained from a
         successful `Data Upload API
         <https://docs.microsoft.com/en-us/rest/api/maps/data%20v2/uploadpreview>`_ call.
        :type udid: str
        :param output_ontology: Output ontology version. "facility-2.0" is the only supported value at
         this time. Please refer to this `article
         <https://docs.microsoft.com/en-us/azure/azure-maps/creator-facility-ontology>`_ for more
         information about Azure Maps Creator ontologies.
        :type output_ontology: str
        :param description: User provided description of the content being converted.
        :type description: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling.
         Pass in False for this operation to not poll, or pass in your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either LongRunningOperationResult or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.maps.conversion.models.LongRunningOperationResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LongRunningOperationResult"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._convert_initial(
                udid=udid,
                output_ontology=output_ontology,
                description=description,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Resource-Location']=self._deserialize('str', response.headers.get('Resource-Location'))
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'location'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_convert.metadata = {'url': '/conversions'}  # type: ignore

    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ConversionListResponse"]
        """**Applies to:** see pricing `tiers <https://aka.ms/AzureMapsPricingTier>`_.

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API and SDK. `This
        <https://docs.microsoft.com/azure/azure-maps/creator-indoor-maps>`_ article introduces concepts
        and tools that apply to Azure Maps Creator.

        This API allows the caller to fetch a list of all successful data conversions submitted
        previously using the `Conversion API
        <https://docs.microsoft.com/en-us/rest/api/maps/conversion/convertpreview>`_.

        Submit List Request
        ^^^^^^^^^^^^^^^^^^^

        To list all successful conversions you will issue a ``GET`` request with no additional
        parameters.

        List Data Response
        ^^^^^^^^^^^^^^^^^^

        The Conversion List API returns the complete list of all conversion details in ``json``
        format.:code:`<br>`

        Here is a sample response returning the details of two successful conversion requests:

        :code:`<br>`

        .. code-block:: json

           {
               "conversions":
               [
                   {
                       "conversionId": "54398242-ea6c-1f31-4fa6-79b1ae0fc24d",
                       "udid": "31838736-8b84-11ea-bc55-0242ac130003",
                       "created": "5/19/2020 9:00:00 AM +00:00",
                       "description": "User provided description.",
                       "featureCounts": {
                           "DIR": 1,
                           "LVL": 3,
                           "FCL": 1,
                           "UNIT": 150,
                           "CTG": 8,
                           "AEL": 0,
                           "OPN": 10
                       }
                   },
                   {
                       "conversionId": "2acf7d32-8b84-11ea-bc55-0242ac130003",
                       "udid": "1214bc58-8b84-11ea-bc55-0242ac1300039",
                       "created": "5/19/2020 9:00:00 AM +00:00",
                       "description": "User provided description.",
                       "featureCounts": {
                           "DIR": 1,
                           "LVL": 3,
                           "FCL": 1,
                           "UNIT": 150,
                           "CTG": 8,
                           "AEL": 0,
                           "OPN": 10
                       }
                   }
               ]
           }

        :code:`<br>`.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ConversionListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.maps.conversion.models.ConversionListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConversionListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            if self._config.x_ms_client_id is not None:
                header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ConversionListResponse', pipeline_response)
            list_of_elem = deserialized.conversions
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/conversions'}  # type: ignore

    def get(
        self,
        conversion_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ConversionListDetailInfo"
        """**Applies to:** see pricing `tiers <https://aka.ms/AzureMapsPricingTier>`_.

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API and SDK. `This
        <https://docs.microsoft.com/azure/azure-maps/creator-indoor-maps>`_ article introduces concepts
        and tools that apply to Azure Maps Creator.

        This API allows the caller to fetch a successful data conversion submitted previously using the
        `Conversion API <https://docs.microsoft.com/en-us/rest/api/maps/conversion/convertpreview>`_.

        :param conversion_id: The conversion id for the content. The ``conversionId`` must have been
         obtained from a successful `Conversion API
         <https://docs.microsoft.com/en-us/rest/api/maps/v2/conversion/convert>`_ call.
        :type conversion_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConversionListDetailInfo, or the result of cls(response)
        :rtype: ~azure.maps.conversion.models.ConversionListDetailInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConversionListDetailInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'conversionId': self._serialize.url("conversion_id", conversion_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ConversionListDetailInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/conversions/{conversionId}'}  # type: ignore

    def delete(
        self,
        conversion_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """.. role:: raw-html-m2r(raw)
           :format: html


        **Applies to:** see pricing `tiers <https://aka.ms/AzureMapsPricingTier>`_.

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API and SDK. `This
        <https://docs.microsoft.com/azure/azure-maps/creator-indoor-maps>`_ article introduces concepts
        and tools that apply to Azure Maps Creator.

        This API allows the caller to delete any data conversions created previously using the
        `Conversion API <https://docs.microsoft.com/en-us/rest/api/maps/conversion/convertpreview>`_.

        Submit Delete Request
        ^^^^^^^^^^^^^^^^^^^^^

        To delete your conversion data you will issue a ``DELETE`` request where the path will contain
        the ``conversionId`` of the data to delete.

        Conversion Delete Response
        ^^^^^^^^^^^^^^^^^^^^^^^^^^

        The Conversion Delete API returns a HTTP ``204 No Content`` response with an empty body, if the
        converted data resources were deleted successfully.:code:`<br>`\ :raw-html-m2r:`<br>`
        A HTTP ``400 Bad Request`` error response will be returned if no resource associated with the
        passed-in ``conversionId`` is found.

        :param conversion_id: The conversion id for the content. The ``conversionId`` must have been
         obtained from a successful `Conversion API
         <https://docs.microsoft.com/en-us/rest/api/maps/v2/conversion/convert>`_ call.
        :type conversion_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'conversionId': self._serialize.url("conversion_id", conversion_id, 'str'),
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

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/conversions/{conversionId}'}  # type: ignore

    def get_operation(
        self,
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.LongRunningOperationResult"
        """This path will be obtained from a call to POST /conversions.  While in progress, an http200
        will be returned with no extra headers -  followed by an http200 with Resource-Location header
        once successfully completed.

        :param operation_id: The ID to query the status for the dataset create/import request.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LongRunningOperationResult, or the result of cls(response)
        :rtype: ~azure.maps.conversion.models.LongRunningOperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LongRunningOperationResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0"
        accept = "application/json"

        # Construct URL
        url = self.get_operation.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Resource-Location']=self._deserialize('str', response.headers.get('Resource-Location'))
        deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_operation.metadata = {'url': '/conversions/operations/{operationId}'}  # type: ignore
