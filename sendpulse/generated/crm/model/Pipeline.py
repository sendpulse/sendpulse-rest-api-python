from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.DefaultStatusProperty import DefaultStatusProperty
from sendpulse.generated.crm.model.Setting import Setting
from sendpulse.generated.crm.model.Step import Step


@dataclass(slots=True)
class Pipeline:
    id: int | None = None
    userId: int | None = None
    name: str | None = None
    status: DefaultStatusProperty | None = None
    order: int | None = None
    steps: list[Step] | None = None
    settings: list[Setting] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Pipeline:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            name=data.get("name"),
            status=DefaultStatusProperty.from_dict(data["status"]) if isinstance(data.get("status"), dict) else None,
            order=data.get("order"),
            steps=[Step.from_dict(i) for i in data["steps"]] if isinstance(data.get("steps"), list) else None,
            settings=[Setting.from_dict(i) for i in data["settings"]] if isinstance(data.get("settings"), list) else None,
        )
