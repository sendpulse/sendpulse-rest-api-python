from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.DealAttributeValue import DealAttributeValue
from sendpulse.generated.crm.model.DealComment import DealComment
from sendpulse.generated.crm.model.DealExpiration import DealExpiration
from sendpulse.generated.crm.model.DealHistory import DealHistory
from sendpulse.generated.crm.model.DealSourceType import DealSourceType
from sendpulse.generated.crm.model.DealStatusProperty import DealStatusProperty
from sendpulse.generated.crm.model.EntityAttachment import EntityAttachment


@dataclass(slots=True)
class Deal:
    id: int | None = None
    pipelineId: int | None = None
    status: DealStatusProperty | None = None
    stepId: int | None = None
    responsibleId: int | None = None
    number: int | None = None
    name: str | None = None
    price: float | None = None
    currency: str | None = None
    profit: float | None = None
    hasExpense: bool | None = None
    order: int | None = None
    sourceType: DealSourceType | None = None
    sourceId: int | None = None
    history: list[DealHistory] | None = None
    comments: list[DealComment] | None = None
    attributes: list[DealAttributeValue] | None = None
    expiration: DealExpiration | None = None
    attachments: EntityAttachment | None = None
    tasks: list[Any] | None = None
    createdAt: str | None = None
    updatedAt: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Deal:
        return cls(
            id=data.get("id"),
            pipelineId=data.get("pipelineId"),
            status=DealStatusProperty.from_dict(data["status"]) if isinstance(data.get("status"), dict) else None,
            stepId=data.get("stepId"),
            responsibleId=data.get("responsibleId"),
            number=data.get("number"),
            name=data.get("name"),
            price=data.get("price"),
            currency=data.get("currency"),
            profit=data.get("profit"),
            hasExpense=data.get("hasExpense"),
            order=data.get("order"),
            sourceType=DealSourceType.from_dict(data["sourceType"]) if isinstance(data.get("sourceType"), dict) else None,
            sourceId=data.get("sourceId"),
            history=[DealHistory.from_dict(i) for i in data["history"]] if isinstance(data.get("history"), list) else None,
            comments=[DealComment.from_dict(i) for i in data["comments"]] if isinstance(data.get("comments"), list) else None,
            attributes=[DealAttributeValue.from_dict(i) for i in data["attributes"]] if isinstance(data.get("attributes"), list) else None,
            expiration=DealExpiration.from_dict(data["expiration"]) if isinstance(data.get("expiration"), dict) else None,
            attachments=EntityAttachment.from_dict(data["attachments"]) if isinstance(data.get("attachments"), dict) else None,
            tasks=data.get("tasks"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
        )
