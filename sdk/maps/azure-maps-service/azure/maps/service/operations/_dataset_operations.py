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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DatasetOperations(object):
    """DatasetOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.maps.service.models
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

    def _create_preview_initial(
        self,
        type,  # type: Union[str, "_models.DatasetType"]
        conversion_id=None,  # type: Optional[str]
        udid=None,  # type: Optional[str]
        dataset_id=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LongRunningOperationResult"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LongRunningOperationResult"]]
        error_map = {
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json, application/xml"

        # Construct URL
        url = self._create_preview_initial.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if self._config.subscription_key is not None:
            query_parameters['subscription-key'] = self._serialize.query("self._config.subscription_key", self._config.subscription_key, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if conversion_id is not None:
            query_parameters['conversionId'] = self._serialize.query("conversion_id", conversion_id, 'str')
        if udid is not None:
            query_parameters['udid'] = self._serialize.query("udid", udid, 'str')
        query_parameters['type'] = self._serialize.query("type", type, 'str')
        if dataset_id is not None:
            query_parameters['datasetId'] = self._serialize.query("dataset_id", dataset_id, 'str')
        if description is not None:
            query_parameters['description'] = self._serialize.query("description", description, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 201:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

        if response.status_code == 201:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _create_preview_initial.metadata = {'url': '/dataset/create'}  # type: ignore

    def begin_create_preview(
        self,
        type,  # type: Union[str, "_models.DatasetType"]
        conversion_id=None,  # type: Optional[str]
        udid=None,  # type: Optional[str]
        dataset_id=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LongRunningOperationResult"]
        """**Dataset Create API**

        **Applies to:** S1 pricing tier.

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API
        and SDK. The Dataset APIs are part of Creator. This API allows the caller to create a dataset
        from data that
        was uploaded to the Azure Maps Data Service.

        You can use this API in a scenario like uploading a DWG zip package for a building, converting
        the zip package using
        the Azure Maps Conversion Service, creating a dataset from the converted zip package. The
        created dataset can be
        used to create tilesets using the Azure Maps Tileset Service and can be queried via the Azure
        Maps WFS Service.

        Submit Create Request
        ---------------------

        To create your dataset, you will use a ``POST`` request where the ``conversionId`` query
        parameter is an id that represents
        the converted DWG zip package, the ``type`` parameter will describe the data type to use for
        the dataset, the ``datasetId``
        parameter will describe if the provided data should be appended to a current dataset and,
        optionally, the
        ``description`` query parameter will contain a description (if description is not provided a
        default description will be
        given).

        The Create API is a
        `long-running request <https://aka.ms/am-creator-lrt>`_.

        :param type: The type of data to create the dataset with.
        :type type: str or ~azure.maps.service.models.DatasetType
        :param conversion_id: The unique ID used to create the dataset. The ``conversionId`` must have
         been obtained from a successful call to the Conversion Service Convert API and must be provided
         with multiple query parameters with same name (if more than one is provided). May not be
         provided in conjunction with the ``udid`` query parameter.
        :type conversion_id: str
        :param udid: The unique data ID used to create the dataset. The ``udid`` must have been
         obtained from a successful call to the Data Service Upload API and must be provided with
         multiple query parameters with the same name (if more than one is provided). May not be
         provided in conjunction with ``conversionId`` query parameter.
        :type udid: str
        :param dataset_id: The ID for the dataset to append to.
        :type dataset_id: str
        :param description: The description to be given to the dataset.
        :type description: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the LROBasePolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either LongRunningOperationResult or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.maps.service.models.LongRunningOperationResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LongRunningOperationResult"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_preview_initial(
                type=type,
                conversion_id=conversion_id,
                udid=udid,
                dataset_id=dataset_id,
                description=description,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
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
    begin_create_preview.metadata = {'url': '/dataset/create'}  # type: ignore

    def _import_preview_initial(
        self,
        dataset_id,  # type: str
        type,  # type: Union[str, "_models.ImportDataType"]
        udid=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LongRunningOperationResult"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LongRunningOperationResult"]]
        error_map = {
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json, application/xml"

        # Construct URL
        url = self._import_preview_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'datasetId': self._serialize.url("dataset_id", dataset_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if self._config.subscription_key is not None:
            query_parameters['subscription-key'] = self._serialize.query("self._config.subscription_key", self._config.subscription_key, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if udid is not None:
            query_parameters['udid'] = self._serialize.query("udid", udid, 'str')
        query_parameters['type'] = self._serialize.query("type", type, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.patch(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

        if response.status_code == 200:
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _import_preview_initial.metadata = {'url': '/dataset/import/{datasetId}'}  # type: ignore

    def begin_import_preview(
        self,
        dataset_id,  # type: str
        type,  # type: Union[str, "_models.ImportDataType"]
        udid=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LongRunningOperationResult"]
        """**Dataset Import API**

        **Applies to:** S1 pricing tier.
        :code:`<br>`

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API
        and SDK. The Dataset APIs are part of Creator. This API allows the caller to bulk import data
        into a dataset
        from data that was uploaded to the Azure Maps Data service.:code:`<br>`

        Submit Import Request
        ^^^^^^^^^^^^^^^^^^^^^

        To import data into your dataset, you will use a ``PATCH`` request where the ``datasetId``
        query parameter is the
        dataset you want to import your data into, the ``udid`` query parameter is the data you want to
        import, and the ``type``
        parameter will describe the data type to use for the import data.:code:`<br>`

        The Import API is a
        `long-running request <https://aka.ms/am-creator-lrt>`_.

        :param dataset_id: The identifier for the dataset to query from.
        :type dataset_id: str
        :param type: The type of data to import into the dataset with.
        :type type: str or ~azure.maps.service.models.ImportDataType
        :param udid: The unique data ID used to import data into the dataset. The ``udid`` must have
         been obtained from a successful call to the Data Service Upload API.
        :type udid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the LROBasePolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either LongRunningOperationResult or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.maps.service.models.LongRunningOperationResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LongRunningOperationResult"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._import_preview_initial(
                dataset_id=dataset_id,
                type=type,
                udid=udid,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('LongRunningOperationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'datasetId': self._serialize.url("dataset_id", dataset_id, 'str'),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments,  **kwargs)
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
    begin_import_preview.metadata = {'url': '/dataset/import/{datasetId}'}  # type: ignore

    def delete_preview(
        self,
        dataset_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> object
        """.. role:: raw-html-m2r(raw)
           :format: html


        **Dataset Delete API**

        **Applies to:** S1 pricing tier.
        :code:`<br>`

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API and SDK. The Dataset APIs are part of Creator.
        This API allows the caller to delete a previously created dataset.:code:`<br>`\ :raw-
        html-m2r:`<br>`
        You can also use this API to delete old/unused datasets to create space for new Creator
        content.

        Submit Delete Request
        ^^^^^^^^^^^^^^^^^^^^^

        To delete your content you will issue a ``DELETE`` request where the path will contain the
        ``datasetId`` of the dataset to delete.:code:`<br>`

        Delete Data Response
        ^^^^^^^^^^^^^^^^^^^^

        The Delete API returns a HTTP ``204 No Content`` response if the dataset resource was deleted
        successfully.:code:`<br>`.

        :param dataset_id: The identifier for the dataset to query from.
        :type dataset_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: object, or the result of cls(response)
        :rtype: object
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[object]
        error_map = {
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json, application/xml"

        # Construct URL
        url = self.delete_preview.metadata['url']  # type: ignore
        path_format_arguments = {
            'datasetId': self._serialize.url("dataset_id", dataset_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if self._config.subscription_key is not None:
            query_parameters['subscription-key'] = self._serialize.query("self._config.subscription_key", self._config.subscription_key, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 204:
            deserialized = self._deserialize('object', pipeline_response)

        if response.status_code == 204:
            deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete_preview.metadata = {'url': '/dataset/{datasetId}'}  # type: ignore

    def list_preview(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DatasetListResponse"
        """**Dataset List API**

        **Applies to:** S1 pricing tier.
        :code:`<br>`

        Creator makes it possible to develop applications based on your private indoor map data using
        Azure Maps API and SDK. The Dataset APIs are part of Creator.
        This API allows the caller to fetch a list of all previously successfully created datasets.

        Submit List Request
        ^^^^^^^^^^^^^^^^^^^

        To list all your datasets, you will issue a ``GET`` request with no additional
        parameters.:code:`<br>`

        List Data Response
        ^^^^^^^^^^^^^^^^^^

        The List API returns the complete list of all datasets in ``json`` format. The response
        contains the following fields (if they are not null or empty):

        ..

           created - The timestamp the dataset was created.
           datasetId - The id for the dataset.
           description - The description for the dataset.
           datasetSources - The source data that was used when the create request was issued.


        The ``datasetSources`` describes the source data that was used when the create request was
        issued and contains the following elements (if they are not null or empty):

        ..

           conversionIds - The list of ``conversionId`` (null if none were provided).
           udids - The list of ``udid`` (null if none were provided).
           appendDatasetId - The ``datasetId`` that was used for an append operation (null if none was
        used).
           type - The type of data stored in the dataset that was created.


        Here's a sample response returning the ``timestamp``\ , ``datasetId``\ , ``description``\ , and
        ``datasetSources`` of 3 dataset resources:

        :code:`<br>`

        .. code-block:: json

           {
             "datasets": [
               {
                 "timestamp": "2020-01-01T22:50:48+00:00",
                 "datasetId": "f6495f62-94f8-0ec2-c252-45626f82fcb2",
                 "description": "Some description or comment for the dataset.",
                 "datasetSources": {
                   "conversionIds": [
                     "15d21452-c9bb-27b6-5e79-743ca5c3205d"
                   ],
                   "type": "facility"
                 },
                 "status": "Succeeded"
               },
               {
                 "timestamp": "2020-01-01T22:57:53+00:00",
                 "datasetId": "8b1288fa-1958-4a2b-b68e-13a7i5af7d7c",
                 "description": "Create from upload '0c1288fa-2058-4a1b-b68d-13a5f5af7d7c'.",
                 "datasetSources": {
                   "udids": [
                     "0c1288fa-2058-4a1b-b68d-13a5f5af7d7c"
                   ],
                   "type": "facility"
                 },
                 "status": "Succeeded"
               },
               {
                 "timestamp": "2020-01-01T20:39:36+00:00",
                 "datasetId": "7c1288fa-2058-4a1b-b68f-13a6h5af7d7c",
                 "description": "Some other description or comment for the dataset.",
                 "datasetSources": {
                   "conversionIds": [
                     "15d21452-c9bb-27b6-5e79-743ca5c3205d"
                   ],
                   "appendDatasetId": "8b1288fa-1958-4a2b-b68e-13a7i5af7d7c",
                   "type": "facility"
                 },
                 "status": "Succeeded"
               }
             ]
           }

        :code:`<br>`.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetListResponse, or the result of cls(response)
        :rtype: ~azure.maps.service.models.DatasetListResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetListResponse"]
        error_map = {
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0"
        accept = "application/json, application/xml"

        # Construct URL
        url = self.list_preview.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if self._config.subscription_key is not None:
            query_parameters['subscription-key'] = self._serialize.query("self._config.subscription_key", self._config.subscription_key, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            deserialized = self._deserialize('DatasetListResponse', pipeline_response)

        if response.status_code == 200:
            deserialized = self._deserialize('DatasetListResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_preview.metadata = {'url': '/dataset'}  # type: ignore
