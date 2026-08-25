from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.DefaultStatusProperty import DefaultStatusProperty


@dataclass(slots=True)
class Step:
    id: int | None = None
    pipelineId: int | None = None
    name: str | None = None
    order: int | None = None
    status: DefaultStatusProperty | None = None
    color: str | None = None
    addEndHours: int | None = None
    notifyIn: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Step:
        return cls(
            id=data.get("id"),
            pipelineId=data.get("pipelineId"),
            name=data.get("name"),
            order=data.get("order"),
            status=DefaultStatusProperty.from_dict(data["status"]) if isinstance(data.get("status"), dict) else None,
            color=data.get("color"),
            addEndHours=data.get("addEndHours"),
            notifyIn=data.get("notifyIn"),
        )
