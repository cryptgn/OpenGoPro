"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Defines the structure of protobuf message for network management
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from . import response_generic_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumNetworkOwner:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumNetworkOwnerEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumNetworkOwner.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DEPRECATED_1: _EnumNetworkOwner.ValueType
    DEPRECATED_2: _EnumNetworkOwner.ValueType
    DEPRECATED_3: _EnumNetworkOwner.ValueType
    DEPRECATED_4: _EnumNetworkOwner.ValueType
    DEPRECATED_5: _EnumNetworkOwner.ValueType
    DEPRECATED_6: _EnumNetworkOwner.ValueType
    DEPRECATED_7: _EnumNetworkOwner.ValueType

class EnumNetworkOwner(_EnumNetworkOwner, metaclass=_EnumNetworkOwnerEnumTypeWrapper): ...

DEPRECATED_1: EnumNetworkOwner.ValueType
DEPRECATED_2: EnumNetworkOwner.ValueType
DEPRECATED_3: EnumNetworkOwner.ValueType
DEPRECATED_4: EnumNetworkOwner.ValueType
DEPRECATED_5: EnumNetworkOwner.ValueType
DEPRECATED_6: EnumNetworkOwner.ValueType
DEPRECATED_7: EnumNetworkOwner.ValueType
global___EnumNetworkOwner = EnumNetworkOwner

class _EnumProvisioning:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumProvisioningEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumProvisioning.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROVISIONING_UNKNOWN: _EnumProvisioning.ValueType
    PROVISIONING_NEVER_STARTED: _EnumProvisioning.ValueType
    PROVISIONING_STARTED: _EnumProvisioning.ValueType
    PROVISIONING_ABORTED_BY_SYSTEM: _EnumProvisioning.ValueType
    PROVISIONING_CANCELLED_BY_USER: _EnumProvisioning.ValueType
    PROVISIONING_SUCCESS_NEW_AP: _EnumProvisioning.ValueType
    PROVISIONING_SUCCESS_OLD_AP: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_FAILED_TO_ASSOCIATE: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_PASSWORD_AUTH: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_EULA_BLOCKING: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_NO_INTERNET: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_UNSUPPORTED_TYPE: _EnumProvisioning.ValueType

class EnumProvisioning(_EnumProvisioning, metaclass=_EnumProvisioningEnumTypeWrapper): ...

PROVISIONING_UNKNOWN: EnumProvisioning.ValueType
PROVISIONING_NEVER_STARTED: EnumProvisioning.ValueType
PROVISIONING_STARTED: EnumProvisioning.ValueType
PROVISIONING_ABORTED_BY_SYSTEM: EnumProvisioning.ValueType
PROVISIONING_CANCELLED_BY_USER: EnumProvisioning.ValueType
PROVISIONING_SUCCESS_NEW_AP: EnumProvisioning.ValueType
PROVISIONING_SUCCESS_OLD_AP: EnumProvisioning.ValueType
PROVISIONING_ERROR_FAILED_TO_ASSOCIATE: EnumProvisioning.ValueType
PROVISIONING_ERROR_PASSWORD_AUTH: EnumProvisioning.ValueType
PROVISIONING_ERROR_EULA_BLOCKING: EnumProvisioning.ValueType
PROVISIONING_ERROR_NO_INTERNET: EnumProvisioning.ValueType
PROVISIONING_ERROR_UNSUPPORTED_TYPE: EnumProvisioning.ValueType
global___EnumProvisioning = EnumProvisioning

class _EnumScanning:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumScanningEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumScanning.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SCANNING_UNKNOWN: _EnumScanning.ValueType
    SCANNING_NEVER_STARTED: _EnumScanning.ValueType
    SCANNING_STARTED: _EnumScanning.ValueType
    SCANNING_ABORTED_BY_SYSTEM: _EnumScanning.ValueType
    SCANNING_CANCELLED_BY_USER: _EnumScanning.ValueType
    SCANNING_SUCCESS: _EnumScanning.ValueType

class EnumScanning(_EnumScanning, metaclass=_EnumScanningEnumTypeWrapper): ...

SCANNING_UNKNOWN: EnumScanning.ValueType
SCANNING_NEVER_STARTED: EnumScanning.ValueType
SCANNING_STARTED: EnumScanning.ValueType
SCANNING_ABORTED_BY_SYSTEM: EnumScanning.ValueType
SCANNING_CANCELLED_BY_USER: EnumScanning.ValueType
SCANNING_SUCCESS: EnumScanning.ValueType
global___EnumScanning = EnumScanning

class _EnumScanEntryFlags:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumScanEntryFlagsEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumScanEntryFlags.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SCAN_FLAG_OPEN: _EnumScanEntryFlags.ValueType
    SCAN_FLAG_AUTHENTICATED: _EnumScanEntryFlags.ValueType
    SCAN_FLAG_CONFIGURED: _EnumScanEntryFlags.ValueType
    SCAN_FLAG_BEST_SSID: _EnumScanEntryFlags.ValueType
    SCAN_FLAG_ASSOCIATED: _EnumScanEntryFlags.ValueType
    SCAN_FLAG_UNSUPPORTED_TYPE: _EnumScanEntryFlags.ValueType
    DEPRECATED: _EnumScanEntryFlags.ValueType

class EnumScanEntryFlags(_EnumScanEntryFlags, metaclass=_EnumScanEntryFlagsEnumTypeWrapper): ...

SCAN_FLAG_OPEN: EnumScanEntryFlags.ValueType
SCAN_FLAG_AUTHENTICATED: EnumScanEntryFlags.ValueType
SCAN_FLAG_CONFIGURED: EnumScanEntryFlags.ValueType
SCAN_FLAG_BEST_SSID: EnumScanEntryFlags.ValueType
SCAN_FLAG_ASSOCIATED: EnumScanEntryFlags.ValueType
SCAN_FLAG_UNSUPPORTED_TYPE: EnumScanEntryFlags.ValueType
DEPRECATED: EnumScanEntryFlags.ValueType
global___EnumScanEntryFlags = EnumScanEntryFlags

class NotifProvisioningState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROVISIONING_STATE_FIELD_NUMBER: builtins.int
    provisioning_state: global___EnumProvisioning.ValueType
    "Provisioning/connection state"

    def __init__(self, *, provisioning_state: global___EnumProvisioning.ValueType | None = ...) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["provisioning_state", b"provisioning_state"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["provisioning_state", b"provisioning_state"]
    ) -> None: ...

global___NotifProvisioningState = NotifProvisioningState

class NotifStartScanning(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCANNING_STATE_FIELD_NUMBER: builtins.int
    SCAN_ID_FIELD_NUMBER: builtins.int
    TOTAL_ENTRIES_FIELD_NUMBER: builtins.int
    TOTAL_CONFIGURED_SSID_FIELD_NUMBER: builtins.int
    scanning_state: global___EnumScanning.ValueType
    "Scanning state"
    scan_id: builtins.int
    "ID associated with scan results (included if scan was successful)"
    total_entries: builtins.int
    "Number of APs found during scan (included if scan was successful)"
    total_configured_ssid: builtins.int
    "Total count of camera's provisioned SSIDs"

    def __init__(
        self,
        *,
        scanning_state: global___EnumScanning.ValueType | None = ...,
        scan_id: builtins.int | None = ...,
        total_entries: builtins.int | None = ...,
        total_configured_ssid: builtins.int | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "scan_id",
            b"scan_id",
            "scanning_state",
            b"scanning_state",
            "total_configured_ssid",
            b"total_configured_ssid",
            "total_entries",
            b"total_entries",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "scan_id",
            b"scan_id",
            "scanning_state",
            b"scanning_state",
            "total_configured_ssid",
            b"total_configured_ssid",
            "total_entries",
            b"total_entries",
        ],
    ) -> None: ...

global___NotifStartScanning = NotifStartScanning

class RequestConnect(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SSID_FIELD_NUMBER: builtins.int
    OWNER_PURPOSE_FIELD_NUMBER: builtins.int
    ssid: builtins.str
    "AP SSID"
    owner_purpose: global___EnumNetworkOwner.ValueType
    "Deprecated"

    def __init__(
        self,
        *,
        ssid: builtins.str | None = ...,
        owner_purpose: global___EnumNetworkOwner.ValueType | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["owner_purpose", b"owner_purpose", "ssid", b"ssid"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["owner_purpose", b"owner_purpose", "ssid", b"ssid"]
    ) -> None: ...

global___RequestConnect = RequestConnect

class RequestConnectNew(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SSID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    STATIC_IP_FIELD_NUMBER: builtins.int
    GATEWAY_FIELD_NUMBER: builtins.int
    SUBNET_FIELD_NUMBER: builtins.int
    DNS_PRIMARY_FIELD_NUMBER: builtins.int
    DNS_SECONDARY_FIELD_NUMBER: builtins.int
    SET_TO_LEAST_PREFERRED_AP_FIELD_NUMBER: builtins.int
    OWNER_PURPOSE_FIELD_NUMBER: builtins.int
    ssid: builtins.str
    "AP SSID"
    password: builtins.str
    "AP password"
    static_ip: builtins.bytes
    "Static IP address"
    gateway: builtins.bytes
    "Gateway IP address"
    subnet: builtins.bytes
    "Subnet mask"
    dns_primary: builtins.bytes
    "Primary DNS"
    dns_secondary: builtins.bytes
    "Secondary DNS"
    set_to_least_preferred_ap: builtins.bool
    "Deprecated"
    owner_purpose: global___EnumNetworkOwner.ValueType
    "Deprecated"

    def __init__(
        self,
        *,
        ssid: builtins.str | None = ...,
        password: builtins.str | None = ...,
        static_ip: builtins.bytes | None = ...,
        gateway: builtins.bytes | None = ...,
        subnet: builtins.bytes | None = ...,
        dns_primary: builtins.bytes | None = ...,
        dns_secondary: builtins.bytes | None = ...,
        set_to_least_preferred_ap: builtins.bool | None = ...,
        owner_purpose: global___EnumNetworkOwner.ValueType | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "dns_primary",
            b"dns_primary",
            "dns_secondary",
            b"dns_secondary",
            "gateway",
            b"gateway",
            "owner_purpose",
            b"owner_purpose",
            "password",
            b"password",
            "set_to_least_preferred_ap",
            b"set_to_least_preferred_ap",
            "ssid",
            b"ssid",
            "static_ip",
            b"static_ip",
            "subnet",
            b"subnet",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "dns_primary",
            b"dns_primary",
            "dns_secondary",
            b"dns_secondary",
            "gateway",
            b"gateway",
            "owner_purpose",
            b"owner_purpose",
            "password",
            b"password",
            "set_to_least_preferred_ap",
            b"set_to_least_preferred_ap",
            "ssid",
            b"ssid",
            "static_ip",
            b"static_ip",
            "subnet",
            b"subnet",
        ],
    ) -> None: ...

global___RequestConnectNew = RequestConnectNew

class RequestGetApEntries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    START_INDEX_FIELD_NUMBER: builtins.int
    MAX_ENTRIES_FIELD_NUMBER: builtins.int
    SCAN_ID_FIELD_NUMBER: builtins.int
    start_index: builtins.int
    "Used for paging. 0 <= start_index < NotifStartScanning.total_entries"
    max_entries: builtins.int
    "Used for paging. Value must be < NotifStartScanning.total_entries"
    scan_id: builtins.int
    "ID corresponding to a set of scan results (i.e."

    def __init__(
        self,
        *,
        start_index: builtins.int | None = ...,
        max_entries: builtins.int | None = ...,
        scan_id: builtins.int | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "max_entries", b"max_entries", "scan_id", b"scan_id", "start_index", b"start_index"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "max_entries", b"max_entries", "scan_id", b"scan_id", "start_index", b"start_index"
        ],
    ) -> None: ...

global___RequestGetApEntries = RequestGetApEntries

class RequestReleaseNetwork(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___RequestReleaseNetwork = RequestReleaseNetwork

class RequestStartScan(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___RequestStartScan = RequestStartScan

class ResponseConnect(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    PROVISIONING_STATE_FIELD_NUMBER: builtins.int
    TIMEOUT_SECONDS_FIELD_NUMBER: builtins.int
    result: response_generic_pb2.EnumResultGeneric.ValueType
    "Generic pass/fail/error info"
    provisioning_state: global___EnumProvisioning.ValueType
    "Provisioning/connection state"
    timeout_seconds: builtins.int
    "Network connection timeout (seconds)"

    def __init__(
        self,
        *,
        result: response_generic_pb2.EnumResultGeneric.ValueType | None = ...,
        provisioning_state: global___EnumProvisioning.ValueType | None = ...,
        timeout_seconds: builtins.int | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "provisioning_state",
            b"provisioning_state",
            "result",
            b"result",
            "timeout_seconds",
            b"timeout_seconds",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "provisioning_state",
            b"provisioning_state",
            "result",
            b"result",
            "timeout_seconds",
            b"timeout_seconds",
        ],
    ) -> None: ...

global___ResponseConnect = ResponseConnect

class ResponseConnectNew(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    PROVISIONING_STATE_FIELD_NUMBER: builtins.int
    TIMEOUT_SECONDS_FIELD_NUMBER: builtins.int
    result: response_generic_pb2.EnumResultGeneric.ValueType
    "Status of Connect New request"
    provisioning_state: global___EnumProvisioning.ValueType
    "Current provisioning state of the network"
    timeout_seconds: builtins.int

    def __init__(
        self,
        *,
        result: response_generic_pb2.EnumResultGeneric.ValueType | None = ...,
        provisioning_state: global___EnumProvisioning.ValueType | None = ...,
        timeout_seconds: builtins.int | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "provisioning_state",
            b"provisioning_state",
            "result",
            b"result",
            "timeout_seconds",
            b"timeout_seconds",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "provisioning_state",
            b"provisioning_state",
            "result",
            b"result",
            "timeout_seconds",
            b"timeout_seconds",
        ],
    ) -> None: ...

global___ResponseConnectNew = ResponseConnectNew

class ScanEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SSID_FIELD_NUMBER: builtins.int
    SIGNAL_STRENGTH_BARS_FIELD_NUMBER: builtins.int
    SIGNAL_FREQUENCY_MHZ_FIELD_NUMBER: builtins.int
    SCAN_ENTRY_FLAGS_FIELD_NUMBER: builtins.int
    OWNER_PURPOSE_FIELD_NUMBER: builtins.int
    ssid: builtins.str
    "AP SSID"
    signal_strength_bars: builtins.int
    "Signal strength (3 bars: >-70 dBm; 2 bars: >-85 dBm; 1 bar: <=-85"
    signal_frequency_mhz: builtins.int
    "Signal frequency (MHz)"
    scan_entry_flags: builtins.int
    "Bitmasked value from EnumScanEntryFlags"
    owner_purpose: global___EnumNetworkOwner.ValueType
    "Deprecated"

    def __init__(
        self,
        *,
        ssid: builtins.str | None = ...,
        signal_strength_bars: builtins.int | None = ...,
        signal_frequency_mhz: builtins.int | None = ...,
        scan_entry_flags: builtins.int | None = ...,
        owner_purpose: global___EnumNetworkOwner.ValueType | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "owner_purpose",
            b"owner_purpose",
            "scan_entry_flags",
            b"scan_entry_flags",
            "signal_frequency_mhz",
            b"signal_frequency_mhz",
            "signal_strength_bars",
            b"signal_strength_bars",
            "ssid",
            b"ssid",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "owner_purpose",
            b"owner_purpose",
            "scan_entry_flags",
            b"scan_entry_flags",
            "signal_frequency_mhz",
            b"signal_frequency_mhz",
            "signal_strength_bars",
            b"signal_strength_bars",
            "ssid",
            b"ssid",
        ],
    ) -> None: ...

global___ScanEntry = ScanEntry

class ResponseGetApEntries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    SCAN_ID_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    result: response_generic_pb2.EnumResultGeneric.ValueType
    "Generic pass/fail/error info"
    scan_id: builtins.int
    "ID associated with this batch of results"

    @property
    def entries(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ScanEntry]:
        """Array containing details about discovered APs"""
    def __init__(
        self,
        *,
        result: response_generic_pb2.EnumResultGeneric.ValueType | None = ...,
        scan_id: builtins.int | None = ...,
        entries: collections.abc.Iterable[global___ScanEntry] | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["result", b"result", "scan_id", b"scan_id"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "entries", b"entries", "result", b"result", "scan_id", b"scan_id"
        ],
    ) -> None: ...

global___ResponseGetApEntries = ResponseGetApEntries

class ResponseStartScanning(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    SCANNING_STATE_FIELD_NUMBER: builtins.int
    result: response_generic_pb2.EnumResultGeneric.ValueType
    "Generic pass/fail/error info"
    scanning_state: global___EnumScanning.ValueType
    "Scanning state"

    def __init__(
        self,
        *,
        result: response_generic_pb2.EnumResultGeneric.ValueType | None = ...,
        scanning_state: global___EnumScanning.ValueType | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["result", b"result", "scanning_state", b"scanning_state"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["result", b"result", "scanning_state", b"scanning_state"]
    ) -> None: ...

global___ResponseStartScanning = ResponseStartScanning
