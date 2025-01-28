"""Controller holding and managing Vantage blinds."""

from decimal import Decimal

from typing_extensions import override

from aiovantage.objects import (
    QISBlind,
    QubeBlind,
    RelayBlind,
    SomfyRS485ShadeChild,
    SomfyURTSI2ShadeChild,
)

from .base import BaseController

BlindTypes = (
    QISBlind | QubeBlind | RelayBlind | SomfyRS485ShadeChild | SomfyURTSI2ShadeChild
)


class BlindsController(BaseController[BlindTypes]):
    """Controller holding and managing Vantage blinds."""

    vantage_types = (
        "QISBlind",
        "QubeBlind",
        "RelayBlind",
        "Somfy.RS-485_Shade_CHILD",
        "Somfy.URTSI_2_Shade_CHILD",
    )
    """The Vantage object types that this controller will fetch."""

    status_types = ("BLIND",)
    """Which Vantage 'STATUS' types this controller handles, if any."""

    @override
    def handle_status(self, obj: BlindTypes, status: str, *args: str) -> None:
        """Handle simple status messages from the event stream."""
        if status != "BLIND":
            return

        # STATUS BLIND
        # -> S:BLIND <id> <position (0.000 - 100.000)>
        state = {
            "position": Decimal(args[0]),
        }

        self.update_state(obj, state)
