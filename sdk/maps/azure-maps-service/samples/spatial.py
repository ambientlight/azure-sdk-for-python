# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
import os

from azure.core.credentials import AzureKeyCredential
from common.common import AzureKeyInQueryCredentialPolicy
import json
import datetime

from azure.maps.creator.models import ResponseFormat, GeofenceMode
from azure.maps.creator import CreatorClient

parser = argparse.ArgumentParser(
    description='Spatial Samples Program. Set SUBSCRIPTION_KEY env variable.')
parser.add_argument('--udid', action="store", required=True)
parser.add_argument('--device_id', action="store", required=True)
parsed = parser.parse_args()
udid = parsed.udid
device_id = parsed.device_id

client = CreatorClient('None', x_ms_client_id=os.environ.get("CLIENT_ID", None), authentication_policy=AzureKeyInQueryCredentialPolicy(
    AzureKeyCredential(os.environ.get("SUBSCRIPTION_KEY")), "subscription-key"))

result = client.spatial.get_buffer(ResponseFormat.JSON, udid, "176.3")
print("Get Buffer")
print(result)


result = client.spatial.get_closest_point(
    ResponseFormat.JSON, udid, 47.622942, -122.316456)
print("Get Closest Point")
print(result)


result = client.spatial.get_geofence(ResponseFormat.JSON, device_id, udid, 48.36, -124.63, None,
                                     datetime.datetime(2018, 9, 9, 10, 0, 0), 50, False, GeofenceMode.ENTER_AND_EXIT)
print("Get Geofence")
print(result)


result = client.spatial.get_great_circle_distance(
    ResponseFormat.JSON, "47.622942,-122.316456:47.610378,-122.200676")
print("Get Great Circle Distance")
print(result)


result = client.spatial.get_point_in_polygon(
    ResponseFormat.JSON, udid, 47.622942, -122.316456)
print("Get Point In Polygon")
print(result)


with open("resources/spatial_buffer_request_body.json", "r") as file:
    result = client.spatial.post_buffer(ResponseFormat.JSON, json.load(file))
    print("Post Buffer")
    print(result)


with open("resources/spatial_closest_point_request_body.json", "r") as file:
    result = client.spatial.post_closest_point(
        ResponseFormat.JSON, 47.622942, -122.316456, json.load(file))
    print("Post Closest Point")
    print(result)


with open("resources/spatial_geofence_request_body.json", "r") as file:
    result = client.spatial.post_geofence(ResponseFormat.JSON, device_id, 48.36, -124.63, json.load(
        file), None, datetime.datetime(2018, 9, 9, 10, 0, 0), 50, False, GeofenceMode.ENTER_AND_EXIT)
    print("Post Geofence")
    print(result)


with open("resources/spatial_point_in_polygon_request_body.json", "r") as file:
    result = client.spatial.post_point_in_polygon(
        ResponseFormat.JSON, 48.36, -124.63, json.load(file))
    print("Post Point In Polygon")
    print(result)
