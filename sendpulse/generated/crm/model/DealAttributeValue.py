from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DealAttributeValue:
    id: int | None = None
    pipelineId: int | None = None
    name: str | None = None
    status: int | None = None
    type: int | None = None
    mandatory: bool | None = None
    order: int | None = None
    options: list[Any] | None = None
    value: Any = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DealAttributeValue:
        return cls(
            id=data.get("id"),
            pipelineId=data.get("pipelineId"),
            name=data.get("name"),
            status=data.get("status"),
            type=data.get("type"),
            mandatory=data.get("mandatory"),
            order=data.get("order"),
            options=data.get("options"),
            value=data.get("value"),
        )
