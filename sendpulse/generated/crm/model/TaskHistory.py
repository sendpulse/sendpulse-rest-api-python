from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TaskHistory:
    id: int | None = None
    taskId: int | None = None
    eventTime: str | None = None
    eventType: str | None = None
    eventData: dict[str, Any] | None = None
    userId: float | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskHistory:
        return cls(
            id=data.get("id"),
            taskId=data.get("taskId"),
            eventTime=data.get("eventTime"),
            eventType=data.get("eventType"),
            eventData=data.get("eventData"),
            userId=data.get("userId"),
        )
