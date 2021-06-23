# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RenderV2Operations:
    """RenderV2Operations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.maps.render.models
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

    async def get_map_tile_preview(
        self,
        tileset_id: Union[str, "_models.TilesetID"],
        zoom: int,
        x_tile_index: int,
        y_tile_index: int,
        time_stamp: Optional[str] = None,
        tile_size: Optional[Union[str, "_models.TileSize"]] = None,
        language: Optional[str] = None,
        view: Optional[str] = None,
        **kwargs: Any
    ) -> IO:
        """**Applies to**\ : S0 and S1 pricing tiers.

        The Get Map Tiles API allows users to request map tiles in vector or raster formats typically
        to be integrated  into a map control or SDK. Some example tiles that can be requested are Azure
        Maps road tiles, real-time  Weather Radar tiles or the map tiles created using `Azure Maps
        Creator <https://aka.ms/amcreator>`_. By default,  Azure Maps uses vector tiles for its web map
        control (Web SDK) and Android SDK.

        :param tileset_id: A tileset is a collection of raster or vector data broken up into a uniform
         grid of square tiles at preset  zoom levels. Every tileset has a **tilesetId** to use when
         making requests. The **tilesetId** for tilesets created using `Azure Maps Creator
         <https://aka.ms/amcreator>`_ are generated through the  `Tileset Create API
         <https://docs.microsoft.com/en-us/rest/api/maps/tileset>`_. The ready-to-use tilesets supplied
         by Azure Maps are listed below. For example, microsoft.base.
        :type tileset_id: str or ~azure.maps.render.models.TilesetID
        :param zoom: Zoom level for the desired tile. Please find TilesetID list below for more details
         on supported zoom level for each tilesetId.:code:`<br>`

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type zoom: int
        :param x_tile_index: X coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type x_tile_index: int
        :param y_tile_index: Y coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type y_tile_index: int
        :param time_stamp: The desired date and time of the requested tile. This parameter must be
         specified in the standard date-time format (e.g. 2019-11-14T16:03:00-08:00), as defined by `ISO
         8601 <https://en.wikipedia.org/wiki/ISO_8601>`_. This parameter is only supported when
         tilesetId parameter is set to one of the values below.


         * microsoft.weather.infrared.main: We provide tiles up to 3 hours in the past. Tiles are
         available in 10-minute intervals. We round the timeStamp value to the nearest 10-minute time
         frame.
         * microsoft.weather.radar.main: We provide tiles up to 1.5 hours in the past and up to 2 hours
         in the future. Tiles are available in 5-minute intervals. We round the timeStamp value to the
         nearest 5-minute time frame.
        :type time_stamp: str
        :param tile_size: The size of the returned map tile in pixels.
        :type tile_size: str or ~azure.maps.render.models.TileSize
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.

         Please refer to `Supported Languages
         <https://docs.microsoft.com/en-us/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :param view: The View parameter specifies which set of geopolitically disputed content is
         returned via Azure Maps services, including  borders and labels displayed on the map. The View
         parameter (also referred to as “user region parameter”) will show the  correct maps for that
         country/region. By default, the View parameter is set to “Unified” even if you haven’t defined
         it in  the request. It is your responsibility to determine the location of your users, and then
         set the View parameter correctly  for that location. Alternatively, you have the option to set
         ‘View=Auto’, which will return the map data based on the IP  address of the request. The View
         parameter in Azure Maps must be used in compliance with applicable laws, including those
         regarding mapping, of the country where maps, images and other data and third party content
         that you are authorized to  access via Azure Maps is made available. Example: view=IN.

         Please refer to `Supported Views <https://aka.ms/AzureMapsLocalizationViews>`_ for details and
         to see the available Views.
        :type view: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0"
        accept = "application/json, image/jpeg, image/png, image/pbf, application/vnd.mapbox-vector-tile"

        # Construct URL
        url = self.get_map_tile_preview.metadata['url']  # type: ignore
        path_format_arguments = {
            'geography': self._serialize.url("self._config.geography", self._config.geography, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        query_parameters['tilesetId'] = self._serialize.query("tileset_id", tileset_id, 'str')
        query_parameters['zoom'] = self._serialize.query("zoom", zoom, 'int')
        query_parameters['x'] = self._serialize.query("x_tile_index", x_tile_index, 'int')
        query_parameters['y'] = self._serialize.query("y_tile_index", y_tile_index, 'int')
        if time_stamp is not None:
            query_parameters['timeStamp'] = self._serialize.query("time_stamp", time_stamp, 'str')
        if tile_size is not None:
            query_parameters['tileSize'] = self._serialize.query("tile_size", tile_size, 'str')
        if language is not None:
            query_parameters['language'] = self._serialize.query("language", language, 'str')
        if view is not None:
            query_parameters['view'] = self._serialize.query("view", view, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.x_ms_client_id is not None:
            header_parameters['x-ms-client-id'] = self._serialize.header("self._config.x_ms_client_id", self._config.x_ms_client_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Content-Type']=self._deserialize('str', response.headers.get('Content-Type'))
        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_map_tile_preview.metadata = {'url': '/map/tile'}  # type: ignore
