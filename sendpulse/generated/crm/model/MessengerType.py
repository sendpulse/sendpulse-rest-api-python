from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.MessengerTypeProperty import MessengerTypeProperty


@dataclass(slots=True)
class MessengerType:
    id: MessengerTypeProperty | None = None
    name: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MessengerType:
        return cls(
            id=MessengerTypeProperty.from_dict(data["id"]) if isinstance(data.get("id"), dict) else None,
            name=data.get("name"),
        )
