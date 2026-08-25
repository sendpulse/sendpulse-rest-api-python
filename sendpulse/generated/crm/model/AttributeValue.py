from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class AttributeValue:
    id: float | None = None
    value: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AttributeValue:
        return cls(
            id=data.get("id"),
            value=data.get("value"),
        )
