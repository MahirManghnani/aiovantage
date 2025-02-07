"""Clients for communicating with the Vantage Host Command service.

The Host Command service is a text-based service that allows interaction with devices
controlled by a Vantage InFusion Controller.

Among other things, this service allows you to change the state of devices
(eg. turn on/off a light) as well as subscribe to status changes for devices.

The service is exposed on port 3010 (SSL) by default, and on port 3001 (non-SSL) if this
port has been opened by the firewall on the controller.

The service is discoverable via mDNS as `_hc._tcp.local` and/or `_secure_hc._tcp.local`.
"""

from ._client import CommandClient, CommandResponse
from ._converter import Converter
from ._events import Event, EventStream, EventType

__all__ = [
    "CommandClient",
    "CommandResponse",
    "Converter",
    "Event",
    "EventStream",
    "EventType",
]
