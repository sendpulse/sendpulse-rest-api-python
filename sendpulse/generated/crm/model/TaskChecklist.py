from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.ChecklistItems import ChecklistItems


@dataclass(slots=True)
class TaskChecklist:
    id: int | None = None
    name: str | None = None
    taskId: int | None = None
    isDone: bool | None = None
    items: ChecklistItems | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskChecklist:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            taskId=data.get("taskId"),
            isDone=data.get("isDone"),
            items=ChecklistItems.from_dict(data["items"]) if isinstance(data.get("items"), dict) else None,
        )
