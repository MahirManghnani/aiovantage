"""Common types."""

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Parent:
    """Parent tag."""

    id: int
    position: int = field(metadata={"type": "Attribute"})
