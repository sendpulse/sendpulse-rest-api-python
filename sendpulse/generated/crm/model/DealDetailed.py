from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.DealAttributeValue import DealAttributeValue
from sendpulse.generated.crm.model.DealComment import DealComment
from sendpulse.generated.crm.model.DealHistory import DealHistory
from sendpulse.generated.crm.model.DealSourceType import DealSourceType
from sendpulse.generated.crm.model.DealStatusProperty import DealStatusProperty


@dataclass(slots=True)
class DealDetailed:
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
    createdAt: str | None = None
    updatedAt: str | None = None
    history: DealHistory | None = None
    comments: DealComment | None = None
    attributes: DealAttributeValue | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DealDetailed:
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
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
            history=DealHistory.from_dict(data["history"]) if isinstance(data.get("history"), dict) else None,
            comments=DealComment.from_dict(data["comments"]) if isinstance(data.get("comments"), dict) else None,
            attributes=DealAttributeValue.from_dict(data["attributes"]) if isinstance(data.get("attributes"), dict) else None,
        )
