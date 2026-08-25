from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.ContactAttributeValue import ContactAttributeValue
from sendpulse.generated.crm.model.ContactComment import ContactComment
from sendpulse.generated.crm.model.ContactEmail import ContactEmail
from sendpulse.generated.crm.model.ContactHistory import ContactHistory
from sendpulse.generated.crm.model.ContactMessenger import ContactMessenger
from sendpulse.generated.crm.model.ContactPhone import ContactPhone
from sendpulse.generated.crm.model.ContactTag import ContactTag
from sendpulse.generated.crm.model.EntityAttachment import EntityAttachment


@dataclass(slots=True)
class Contact:
    id: int | None = None
    userId: int | None = None
    sourceType: str | None = None
    responsibleId: int | None = None
    firstName: str | None = None
    lastName: str | None = None
    dealsQty: int | None = None
    externalContactId: str | None = None
    comments: list[ContactComment] | None = None
    tags: list[ContactTag] | None = None
    phones: list[ContactPhone] | None = None
    emails: list[ContactEmail] | None = None
    messengers: list[ContactMessenger] | None = None
    attributes: list[ContactAttributeValue] | None = None
    history: list[ContactHistory] | None = None
    tasks: list[Any] | None = None
    createdAt: str | None = None
    updatedAt: str | None = None
    attachments: EntityAttachment | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Contact:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            sourceType=data.get("sourceType"),
            responsibleId=data.get("responsibleId"),
            firstName=data.get("firstName"),
            lastName=data.get("lastName"),
            dealsQty=data.get("dealsQty"),
            externalContactId=data.get("externalContactId"),
            comments=[ContactComment.from_dict(i) for i in data["comments"]] if isinstance(data.get("comments"), list) else None,
            tags=[ContactTag.from_dict(i) for i in data["tags"]] if isinstance(data.get("tags"), list) else None,
            phones=[ContactPhone.from_dict(i) for i in data["phones"]] if isinstance(data.get("phones"), list) else None,
            emails=[ContactEmail.from_dict(i) for i in data["emails"]] if isinstance(data.get("emails"), list) else None,
            messengers=[ContactMessenger.from_dict(i) for i in data["messengers"]] if isinstance(data.get("messengers"), list) else None,
            attributes=[ContactAttributeValue.from_dict(i) for i in data["attributes"]] if isinstance(data.get("attributes"), list) else None,
            history=[ContactHistory.from_dict(i) for i in data["history"]] if isinstance(data.get("history"), list) else None,
            tasks=data.get("tasks"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
            attachments=EntityAttachment.from_dict(data["attachments"]) if isinstance(data.get("attachments"), dict) else None,
        )
