from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TaskAttachment:
    id: int | None = None
    link: str | None = None
    taskId: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskAttachment:
        return cls(
            id=data.get("id"),
            link=data.get("link"),
            taskId=data.get("taskId"),
        )
