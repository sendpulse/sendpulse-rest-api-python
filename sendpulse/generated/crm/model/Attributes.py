from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.AttributeValue import AttributeValue


@dataclass(slots=True)
class Attributes:
    type: int | None = None
    name: str | None = None
    status: bool | None = None
    value: list[AttributeValue] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Attributes:
        return cls(
            type=data.get("type"),
            name=data.get("name"),
            status=data.get("status"),
            value=[AttributeValue.from_dict(i) for i in data["value"]] if isinstance(data.get("value"), list) else None,
        )
