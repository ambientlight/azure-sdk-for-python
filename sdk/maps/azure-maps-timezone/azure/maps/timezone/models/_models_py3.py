# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CountryRecord(msrest.serialization.Model):
    """A country record.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Country Name.
    :vartype name: str
    :ivar code: ISO-3166 2-letter country code for the country.
    :vartype code: str
    """

    _validation = {
        'name': {'readonly': True},
        'code': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'code': {'key': 'Code', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CountryRecord, self).__init__(**kwargs)
        self.name = None
        self.code = None


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.maps.timezone.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.maps.timezone.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~azure.maps.timezone.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class IanaId(msrest.serialization.Model):
    """IanaId.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id property.
    :vartype id: str
    :ivar is_alias: IsAlias property.
    :vartype is_alias: bool
    :ivar alias_of: AliasOf property.
    :vartype alias_of: str
    :ivar has_zone1970_location: HasZone1970Location property.
    :vartype has_zone1970_location: bool
    """

    _validation = {
        'id': {'readonly': True},
        'is_alias': {'readonly': True},
        'alias_of': {'readonly': True},
        'has_zone1970_location': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_alias': {'key': 'isAlias', 'type': 'bool'},
        'alias_of': {'key': 'aliasOf', 'type': 'str'},
        'has_zone1970_location': {'key': 'hasZone1970Location', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(IanaId, self).__init__(**kwargs)
        self.id = None
        self.is_alias = None
        self.alias_of = None
        self.has_zone1970_location = None


class ReferenceTimeByCoordinates(msrest.serialization.Model):
    """Details in effect at the local time.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar tag: Time zone name in effect at the reference timestamp (i.e. PST or PDT depending
     whether Daylight Savings Time is in effect).
    :vartype tag: str
    :ivar standard_offset: UTC offset in effect at the ``ReferenceUTCTimestamp``.
    :vartype standard_offset: str
    :ivar daylight_savings: Time saving in minutes in effect at the ``ReferenceUTCTimestamp``.
    :vartype daylight_savings: str
    :ivar wall_time: Current wall time at the given time zone as shown in the ``Tag`` property.
    :vartype wall_time: str
    :ivar posix_tz_valid_year: The year this POSIX string is valid for. Note: A POSIX string will
     only be valid in the given year.
    :vartype posix_tz_valid_year: int
    :ivar posix_tz: POSIX string used to set the time zone environment variable.
    :vartype posix_tz: str
    :ivar sunrise: Sunrise at the given time zone as shown in the ``Tag`` property.
    :vartype sunrise: str
    :ivar sunset: Sunset at the given time zone as shown in the ``Tag`` property.
    :vartype sunset: str
    """

    _validation = {
        'tag': {'readonly': True},
        'standard_offset': {'readonly': True},
        'daylight_savings': {'readonly': True},
        'wall_time': {'readonly': True},
        'posix_tz_valid_year': {'readonly': True},
        'posix_tz': {'readonly': True},
        'sunrise': {'readonly': True},
        'sunset': {'readonly': True},
    }

    _attribute_map = {
        'tag': {'key': 'Tag', 'type': 'str'},
        'standard_offset': {'key': 'StandardOffset', 'type': 'str'},
        'daylight_savings': {'key': 'DaylightSavings', 'type': 'str'},
        'wall_time': {'key': 'WallTime', 'type': 'str'},
        'posix_tz_valid_year': {'key': 'PosixTzValidYear', 'type': 'int'},
        'posix_tz': {'key': 'PosixTz', 'type': 'str'},
        'sunrise': {'key': 'Sunrise', 'type': 'str'},
        'sunset': {'key': 'Sunset', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ReferenceTimeByCoordinates, self).__init__(**kwargs)
        self.tag = None
        self.standard_offset = None
        self.daylight_savings = None
        self.wall_time = None
        self.posix_tz_valid_year = None
        self.posix_tz = None
        self.sunrise = None
        self.sunset = None


class ReferenceTimeById(msrest.serialization.Model):
    """Details in effect at the local time.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar tag: Time zone name in effect at the reference timestamp (i.e. PST or PDT depending
     whether Daylight Savings Time is in effect).
    :vartype tag: str
    :ivar standard_offset: UTC offset in effect at the ``ReferenceUTCTimestamp``.
    :vartype standard_offset: str
    :ivar daylight_savings: Time saving in minutes in effect at the ``ReferenceUTCTimestamp``.
    :vartype daylight_savings: str
    :ivar wall_time: Current wall time at the given time zone as shown in the ``Tag`` property.
    :vartype wall_time: str
    :ivar posix_tz_valid_year: The year this POSIX string is valid for. Note: A POSIX string will
     only be valid in the given year.
    :vartype posix_tz_valid_year: int
    :ivar posix_tz: POSIX string used to set the time zone environment variable.
    :vartype posix_tz: str
    """

    _validation = {
        'tag': {'readonly': True},
        'standard_offset': {'readonly': True},
        'daylight_savings': {'readonly': True},
        'wall_time': {'readonly': True},
        'posix_tz_valid_year': {'readonly': True},
        'posix_tz': {'readonly': True},
    }

    _attribute_map = {
        'tag': {'key': 'Tag', 'type': 'str'},
        'standard_offset': {'key': 'StandardOffset', 'type': 'str'},
        'daylight_savings': {'key': 'DaylightSavings', 'type': 'str'},
        'wall_time': {'key': 'WallTime', 'type': 'str'},
        'posix_tz_valid_year': {'key': 'PosixTzValidYear', 'type': 'int'},
        'posix_tz': {'key': 'PosixTz', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ReferenceTimeById, self).__init__(**kwargs)
        self.tag = None
        self.standard_offset = None
        self.daylight_savings = None
        self.wall_time = None
        self.posix_tz_valid_year = None
        self.posix_tz = None


class RepresentativePoint(msrest.serialization.Model):
    """Representative point property.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar latitude: Latitude property.
    :vartype latitude: float
    :ivar longitude: Longitude property.
    :vartype longitude: float
    """

    _validation = {
        'latitude': {'readonly': True},
        'longitude': {'readonly': True},
    }

    _attribute_map = {
        'latitude': {'key': 'Latitude', 'type': 'float'},
        'longitude': {'key': 'Longitude', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RepresentativePoint, self).__init__(**kwargs)
        self.latitude = None
        self.longitude = None


class TimeTransition(msrest.serialization.Model):
    """TimeTransition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar tag: Tag property.
    :vartype tag: str
    :ivar standard_offset: StandardOffset property.
    :vartype standard_offset: str
    :ivar daylight_savings: DaylightSavings property.
    :vartype daylight_savings: str
    :ivar utc_start: Start date, start time for this transition period.
    :vartype utc_start: ~datetime.datetime
    :ivar utc_end: End date, end time for this transition period.
    :vartype utc_end: ~datetime.datetime
    """

    _validation = {
        'tag': {'readonly': True},
        'standard_offset': {'readonly': True},
        'daylight_savings': {'readonly': True},
        'utc_start': {'readonly': True},
        'utc_end': {'readonly': True},
    }

    _attribute_map = {
        'tag': {'key': 'Tag', 'type': 'str'},
        'standard_offset': {'key': 'StandardOffset', 'type': 'str'},
        'daylight_savings': {'key': 'DaylightSavings', 'type': 'str'},
        'utc_start': {'key': 'UtcStart', 'type': 'iso-8601'},
        'utc_end': {'key': 'UtcEnd', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TimeTransition, self).__init__(**kwargs)
        self.tag = None
        self.standard_offset = None
        self.daylight_savings = None
        self.utc_start = None
        self.utc_end = None


class TimeZoneByCoordinates(msrest.serialization.Model):
    """TimeZoneByCoordinates.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id property.
    :vartype id: str
    :ivar aliases: An array of time zone ID aliases.  Only returned when [options]=\ *zoneinfo* or
     *all*.
    
     Note: may be null.
    :vartype aliases: list[str]
    :ivar countries: An array of country records. Only returned when [options]=\ *zoneinfo* or
     *all*.
    :vartype countries: list[~azure.maps.timezone.models.CountryRecord]
    :param names: Timezone names object.
    :type names: ~azure.maps.timezone.models.TimezoneNames
    :ivar reference_time: Details in effect at the local time.
    :vartype reference_time: ~azure.maps.timezone.models.ReferenceTimeByCoordinates
    :ivar representative_point: Representative point property.
    :vartype representative_point: ~azure.maps.timezone.models.RepresentativePoint
    :ivar time_transitions: Time zone DST transitions from [transitionsFrom] until timestamp + 1
     year.
    :vartype time_transitions: list[~azure.maps.timezone.models.TimeTransition]
    """

    _validation = {
        'id': {'readonly': True},
        'aliases': {'readonly': True},
        'countries': {'readonly': True},
        'reference_time': {'readonly': True},
        'representative_point': {'readonly': True},
        'time_transitions': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'aliases': {'key': 'Aliases', 'type': '[str]'},
        'countries': {'key': 'Countries', 'type': '[CountryRecord]'},
        'names': {'key': 'Names', 'type': 'TimezoneNames'},
        'reference_time': {'key': 'ReferenceTime', 'type': 'ReferenceTimeByCoordinates'},
        'representative_point': {'key': 'RepresentativePoint', 'type': 'RepresentativePoint'},
        'time_transitions': {'key': 'TimeTransitions', 'type': '[TimeTransition]'},
    }

    def __init__(
        self,
        *,
        names: Optional["TimezoneNames"] = None,
        **kwargs
    ):
        super(TimeZoneByCoordinates, self).__init__(**kwargs)
        self.id = None
        self.aliases = None
        self.countries = None
        self.names = names
        self.reference_time = None
        self.representative_point = None
        self.time_transitions = None


class TimezoneByCoordinatesResult(msrest.serialization.Model):
    """This object is returned from a successful Timezone By Coordinates call.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar version: Version property.
    :vartype version: str
    :ivar reference_utc_timestamp: Reference Utc Timestamp property.
    :vartype reference_utc_timestamp: ~datetime.datetime
    :ivar time_zones: TimeZoneByCoordinates array.
    :vartype time_zones: list[~azure.maps.timezone.models.TimeZoneByCoordinates]
    """

    _validation = {
        'version': {'readonly': True},
        'reference_utc_timestamp': {'readonly': True},
        'time_zones': {'readonly': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'reference_utc_timestamp': {'key': 'ReferenceUtcTimestamp', 'type': 'iso-8601'},
        'time_zones': {'key': 'TimeZones', 'type': '[TimeZoneByCoordinates]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TimezoneByCoordinatesResult, self).__init__(**kwargs)
        self.version = None
        self.reference_utc_timestamp = None
        self.time_zones = None


class TimezoneById(msrest.serialization.Model):
    """TimezoneById.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id property.
    :vartype id: str
    :ivar aliases: An array of time zone ID aliases.  Only returned when [options]=\ *zoneinfo* or
     *all*.
    
     Note: may be null.
    :vartype aliases: list[str]
    :ivar countries: An array of country records. Only returned when [options]=\ *zoneinfo* or
     *all*.
    :vartype countries: list[~azure.maps.timezone.models.CountryRecord]
    :param names: Timezone names object.
    :type names: ~azure.maps.timezone.models.TimezoneNames
    :ivar reference_time: Details in effect at the local time.
    :vartype reference_time: ~azure.maps.timezone.models.ReferenceTimeById
    :ivar representative_point: Representative point property.
    :vartype representative_point: ~azure.maps.timezone.models.RepresentativePoint
    :ivar time_transitions: Time zone DST transitions from [transitionsFrom] until timestamp + 1
     year.
    :vartype time_transitions: list[~azure.maps.timezone.models.TimeTransition]
    """

    _validation = {
        'id': {'readonly': True},
        'aliases': {'readonly': True},
        'countries': {'readonly': True},
        'reference_time': {'readonly': True},
        'representative_point': {'readonly': True},
        'time_transitions': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'aliases': {'key': 'Aliases', 'type': '[str]'},
        'countries': {'key': 'Countries', 'type': '[CountryRecord]'},
        'names': {'key': 'Names', 'type': 'TimezoneNames'},
        'reference_time': {'key': 'ReferenceTime', 'type': 'ReferenceTimeById'},
        'representative_point': {'key': 'RepresentativePoint', 'type': 'RepresentativePoint'},
        'time_transitions': {'key': 'TimeTransitions', 'type': '[TimeTransition]'},
    }

    def __init__(
        self,
        *,
        names: Optional["TimezoneNames"] = None,
        **kwargs
    ):
        super(TimezoneById, self).__init__(**kwargs)
        self.id = None
        self.aliases = None
        self.countries = None
        self.names = names
        self.reference_time = None
        self.representative_point = None
        self.time_transitions = None


class TimezoneByIdResult(msrest.serialization.Model):
    """This object is returned from a successful Timezone By ID call.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar version: Version property.
    :vartype version: str
    :ivar reference_utc_timestamp: Reference Utc Timestamp property.
    :vartype reference_utc_timestamp: ~datetime.datetime
    :ivar time_zones: TimeZoneById array.
    :vartype time_zones: list[~azure.maps.timezone.models.TimezoneById]
    """

    _validation = {
        'version': {'readonly': True},
        'reference_utc_timestamp': {'readonly': True},
        'time_zones': {'readonly': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'reference_utc_timestamp': {'key': 'ReferenceUtcTimestamp', 'type': 'iso-8601'},
        'time_zones': {'key': 'TimeZones', 'type': '[TimezoneById]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TimezoneByIdResult, self).__init__(**kwargs)
        self.version = None
        self.reference_utc_timestamp = None
        self.time_zones = None


class TimezoneEnumWindow(msrest.serialization.Model):
    """TimezoneEnumWindow.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar windows_id: Windows Id property.
    :vartype windows_id: str
    :ivar territory: Territory property.
    :vartype territory: str
    :param iana_ids: IanaIds array.
    :type iana_ids: list[str]
    """

    _validation = {
        'windows_id': {'readonly': True},
        'territory': {'readonly': True},
    }

    _attribute_map = {
        'windows_id': {'key': 'WindowsId', 'type': 'str'},
        'territory': {'key': 'Territory', 'type': 'str'},
        'iana_ids': {'key': 'IanaIds', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        iana_ids: Optional[List[str]] = None,
        **kwargs
    ):
        super(TimezoneEnumWindow, self).__init__(**kwargs)
        self.windows_id = None
        self.territory = None
        self.iana_ids = iana_ids


class TimezoneIanaVersionResult(msrest.serialization.Model):
    """This object is returned from a successful Timezone IANA Version call.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar version: Version property.
    :vartype version: str
    """

    _validation = {
        'version': {'readonly': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TimezoneIanaVersionResult, self).__init__(**kwargs)
        self.version = None


class TimezoneNames(msrest.serialization.Model):
    """Timezone names object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar iso6391_language_code: The ISO 639-1 language code of the Names.
    :vartype iso6391_language_code: str
    :ivar generic: Generic Name.
    :vartype generic: str
    :ivar standard: Standard Name.
    :vartype standard: str
    :ivar daylight: Daylight Name.
    :vartype daylight: str
    """

    _validation = {
        'iso6391_language_code': {'readonly': True},
        'generic': {'readonly': True},
        'standard': {'readonly': True},
        'daylight': {'readonly': True},
    }

    _attribute_map = {
        'iso6391_language_code': {'key': 'ISO6391LanguageCode', 'type': 'str'},
        'generic': {'key': 'Generic', 'type': 'str'},
        'standard': {'key': 'Standard', 'type': 'str'},
        'daylight': {'key': 'Daylight', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TimezoneNames, self).__init__(**kwargs)
        self.iso6391_language_code = None
        self.generic = None
        self.standard = None
        self.daylight = None
