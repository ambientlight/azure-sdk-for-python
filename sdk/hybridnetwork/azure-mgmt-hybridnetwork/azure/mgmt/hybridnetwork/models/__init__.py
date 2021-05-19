# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CustomProfile
    from ._models_py3 import DataDisk
    from ._models_py3 import Device
    from ._models_py3 import DeviceListResult
    from ._models_py3 import DevicePropertiesFormat
    from ._models_py3 import DeviceRegistrationKey
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ImageReference
    from ._models_py3 import LinuxConfiguration
    from ._models_py3 import NetworkFunction
    from ._models_py3 import NetworkFunctionListResult
    from ._models_py3 import NetworkFunctionRoleConfiguration
    from ._models_py3 import NetworkFunctionRoleInstanceListResult
    from ._models_py3 import NetworkFunctionSkuDetails
    from ._models_py3 import NetworkFunctionSkuListResult
    from ._models_py3 import NetworkFunctionSkuRoleDetails
    from ._models_py3 import NetworkFunctionTemplate
    from ._models_py3 import NetworkFunctionUserConfiguration
    from ._models_py3 import NetworkFunctionUserConfigurationOsProfile
    from ._models_py3 import NetworkFunctionVendor
    from ._models_py3 import NetworkFunctionVendorConfiguration
    from ._models_py3 import NetworkFunctionVendorListResult
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkInterfaceIPConfiguration
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationList
    from ._models_py3 import OsDisk
    from ._models_py3 import OsProfile
    from ._models_py3 import PreviewSubscription
    from ._models_py3 import PreviewSubscriptionsList
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import RoleInstance
    from ._models_py3 import SkuOverview
    from ._models_py3 import SshConfiguration
    from ._models_py3 import SshPublicKey
    from ._models_py3 import StorageProfile
    from ._models_py3 import SubResource
    from ._models_py3 import TagsObject
    from ._models_py3 import TrackedResource
    from ._models_py3 import Vendor
    from ._models_py3 import VendorListResult
    from ._models_py3 import VendorNetworkFunction
    from ._models_py3 import VendorNetworkFunctionListResult
    from ._models_py3 import VendorSku
    from ._models_py3 import VendorSkuListResult
    from ._models_py3 import VirtualHardDisk
except (SyntaxError, ImportError):
    from ._models import CustomProfile  # type: ignore
    from ._models import DataDisk  # type: ignore
    from ._models import Device  # type: ignore
    from ._models import DeviceListResult  # type: ignore
    from ._models import DevicePropertiesFormat  # type: ignore
    from ._models import DeviceRegistrationKey  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ImageReference  # type: ignore
    from ._models import LinuxConfiguration  # type: ignore
    from ._models import NetworkFunction  # type: ignore
    from ._models import NetworkFunctionListResult  # type: ignore
    from ._models import NetworkFunctionRoleConfiguration  # type: ignore
    from ._models import NetworkFunctionRoleInstanceListResult  # type: ignore
    from ._models import NetworkFunctionSkuDetails  # type: ignore
    from ._models import NetworkFunctionSkuListResult  # type: ignore
    from ._models import NetworkFunctionSkuRoleDetails  # type: ignore
    from ._models import NetworkFunctionTemplate  # type: ignore
    from ._models import NetworkFunctionUserConfiguration  # type: ignore
    from ._models import NetworkFunctionUserConfigurationOsProfile  # type: ignore
    from ._models import NetworkFunctionVendor  # type: ignore
    from ._models import NetworkFunctionVendorConfiguration  # type: ignore
    from ._models import NetworkFunctionVendorListResult  # type: ignore
    from ._models import NetworkInterface  # type: ignore
    from ._models import NetworkInterfaceIPConfiguration  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import OsDisk  # type: ignore
    from ._models import OsProfile  # type: ignore
    from ._models import PreviewSubscription  # type: ignore
    from ._models import PreviewSubscriptionsList  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RoleInstance  # type: ignore
    from ._models import SkuOverview  # type: ignore
    from ._models import SshConfiguration  # type: ignore
    from ._models import SshPublicKey  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import TagsObject  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import Vendor  # type: ignore
    from ._models import VendorListResult  # type: ignore
    from ._models import VendorNetworkFunction  # type: ignore
    from ._models import VendorNetworkFunctionListResult  # type: ignore
    from ._models import VendorSku  # type: ignore
    from ._models import VendorSkuListResult  # type: ignore
    from ._models import VirtualHardDisk  # type: ignore

from ._hybrid_network_management_client_enums import (
    DeviceType,
    DiskCreateOptionTypes,
    IPAllocationMethod,
    IPVersion,
    NetworkFunctionRoleConfigurationType,
    OperatingSystemTypes,
    OperationalState,
    ProvisioningState,
    SkuDeploymentMode,
    SkuType,
    Status,
    VMSwitchType,
    VendorProvisioningState,
    VirtualMachineSizeTypes,
)

__all__ = [
    'CustomProfile',
    'DataDisk',
    'Device',
    'DeviceListResult',
    'DevicePropertiesFormat',
    'DeviceRegistrationKey',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'ImageReference',
    'LinuxConfiguration',
    'NetworkFunction',
    'NetworkFunctionListResult',
    'NetworkFunctionRoleConfiguration',
    'NetworkFunctionRoleInstanceListResult',
    'NetworkFunctionSkuDetails',
    'NetworkFunctionSkuListResult',
    'NetworkFunctionSkuRoleDetails',
    'NetworkFunctionTemplate',
    'NetworkFunctionUserConfiguration',
    'NetworkFunctionUserConfigurationOsProfile',
    'NetworkFunctionVendor',
    'NetworkFunctionVendorConfiguration',
    'NetworkFunctionVendorListResult',
    'NetworkInterface',
    'NetworkInterfaceIPConfiguration',
    'Operation',
    'OperationDisplay',
    'OperationList',
    'OsDisk',
    'OsProfile',
    'PreviewSubscription',
    'PreviewSubscriptionsList',
    'ProxyResource',
    'Resource',
    'RoleInstance',
    'SkuOverview',
    'SshConfiguration',
    'SshPublicKey',
    'StorageProfile',
    'SubResource',
    'TagsObject',
    'TrackedResource',
    'Vendor',
    'VendorListResult',
    'VendorNetworkFunction',
    'VendorNetworkFunctionListResult',
    'VendorSku',
    'VendorSkuListResult',
    'VirtualHardDisk',
    'DeviceType',
    'DiskCreateOptionTypes',
    'IPAllocationMethod',
    'IPVersion',
    'NetworkFunctionRoleConfigurationType',
    'OperatingSystemTypes',
    'OperationalState',
    'ProvisioningState',
    'SkuDeploymentMode',
    'SkuType',
    'Status',
    'VMSwitchType',
    'VendorProvisioningState',
    'VirtualMachineSizeTypes',
]
