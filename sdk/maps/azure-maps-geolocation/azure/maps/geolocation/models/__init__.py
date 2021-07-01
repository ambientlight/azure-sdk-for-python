# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CountryRegion
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import IpAddressToLocationResult
except (SyntaxError, ImportError):
    from ._models import CountryRegion  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import IpAddressToLocationResult  # type: ignore

from ._geolocation_client_enums import (
    GeographicResourceLocation,
    Geography,
    ResponseFormat,
)

__all__ = [
    'CountryRegion',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'IpAddressToLocationResult',
    'GeographicResourceLocation',
    'Geography',
    'ResponseFormat',
]
