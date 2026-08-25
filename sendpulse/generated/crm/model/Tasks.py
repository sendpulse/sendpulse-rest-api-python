from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.Attributes import Attributes
from sendpulse.generated.crm.model.EntityAttachment import EntityAttachment
from sendpulse.generated.crm.model.TaskChecklist import TaskChecklist
from sendpulse.generated.crm.model.TaskComment import TaskComment
from sendpulse.generated.crm.model.TaskHistory import TaskHistory
from sendpulse.generated.crm.model.TaskTag import TaskTag


@dataclass(slots=True)
class Tasks:
    id: int | None = None
    name: str | None = None
    userId: int | None = None
    responsibleId: int | None = None
    parentId: int | None = None
    boardId: int | None = None
    stepId: int | None = None
    priority: int | None = None
    order: int | None = None
    description: int | None = None
    alert: str | None = None
    repeat: int | None = None
    startAt: str | None = None
    finishAt: str | None = None
    observers: list[Any] | None = None
    checklists: TaskChecklist | None = None
    attachments: EntityAttachment | None = None
    attributes: Attributes | None = None
    comments: TaskComment | None = None
    histories: TaskHistory | None = None
    tags: TaskTag | None = None
    deals: list[Any] | None = None
    tasks: list[Any] | None = None
    contacts: list[Any] | None = None
    subTasks: list[Any] | None = None
    updatedDaysAt: float | None = None
    createdDaysAt: float | None = None
    createdAt: str | None = None
    updatedAt: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Tasks:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            userId=data.get("userId"),
            responsibleId=data.get("responsibleId"),
            parentId=data.get("parentId"),
            boardId=data.get("boardId"),
            stepId=data.get("stepId"),
            priority=data.get("priority"),
            order=data.get("order"),
            description=data.get("description"),
            alert=data.get("alert"),
            repeat=data.get("repeat"),
            startAt=data.get("startAt"),
            finishAt=data.get("finishAt"),
            observers=data.get("observers"),
            checklists=TaskChecklist.from_dict(data["checklists"]) if isinstance(data.get("checklists"), dict) else None,
            attachments=EntityAttachment.from_dict(data["attachments"]) if isinstance(data.get("attachments"), dict) else None,
            attributes=Attributes.from_dict(data["attributes"]) if isinstance(data.get("attributes"), dict) else None,
            comments=TaskComment.from_dict(data["comments"]) if isinstance(data.get("comments"), dict) else None,
            histories=TaskHistory.from_dict(data["histories"]) if isinstance(data.get("histories"), dict) else None,
            tags=TaskTag.from_dict(data["tags"]) if isinstance(data.get("tags"), dict) else None,
            deals=data.get("deals"),
            tasks=data.get("tasks"),
            contacts=data.get("contacts"),
            subTasks=data.get("subTasks"),
            updatedDaysAt=data.get("updatedDaysAt"),
            createdDaysAt=data.get("createdDaysAt"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
        )
