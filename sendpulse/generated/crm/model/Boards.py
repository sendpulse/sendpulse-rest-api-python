from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.BoardAttribute import BoardAttribute
from sendpulse.generated.crm.model.BoardSettings import BoardSettings
from sendpulse.generated.crm.model.BoardSteps import BoardSteps


@dataclass(slots=True)
class Boards:
    id: int | None = None
    name: str | None = None
    userId: int | None = None
    order: int | None = None
    steps: BoardSteps | None = None
    settings: BoardSettings | None = None
    attributes: BoardAttribute | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Boards:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            userId=data.get("userId"),
            order=data.get("order"),
            steps=BoardSteps.from_dict(data["steps"]) if isinstance(data.get("steps"), dict) else None,
            settings=BoardSettings.from_dict(data["settings"]) if isinstance(data.get("settings"), dict) else None,
            attributes=BoardAttribute.from_dict(data["attributes"]) if isinstance(data.get("attributes"), dict) else None,
        )
