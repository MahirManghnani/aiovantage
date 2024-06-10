"""Generic_HVAC_RS485_Zone_CHILD Thermostat."""

from dataclasses import dataclass

from .thermostat import Thermostat


@dataclass
class VantageGenericHVACRS485ZoneChild(Thermostat):
    """Generic_HVAC_RS485_Zone_CHILD Thermostat."""

    class Meta:
        name = "Vantage.Generic_HVAC_RS485_Zone_CHILD"

