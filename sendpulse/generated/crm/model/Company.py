from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.AttachmentResource import AttachmentResource
from sendpulse.generated.crm.model.Attribute import Attribute
from sendpulse.generated.crm.model.Email import Email
from sendpulse.generated.crm.model.Messenger import Messenger
from sendpulse.generated.crm.model.Phone import Phone


@dataclass(slots=True)
class Company:
    id: int | None = None
    companyName: str | None = None
    responsibleId: int | None = None
    address: str | None = None
    annualBusinessVolume: int | None = None
    currency: str | None = None
    messengers: list[Messenger] | None = None
    phones: list[Phone] | None = None
    emails: list[Email] | None = None
    attributes: list[Attribute] | None = None
    contacts: list[Any] | None = None
    attachments: list[AttachmentResource] | None = None
    createdAt: str | None = None
    updatedAt: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Company:
        return cls(
            id=data.get("id"),
            companyName=data.get("companyName"),
            responsibleId=data.get("responsibleId"),
            address=data.get("address"),
            annualBusinessVolume=data.get("annualBusinessVolume"),
            currency=data.get("currency"),
            messengers=[Messenger.from_dict(i) for i in data["messengers"]] if isinstance(data.get("messengers"), list) else None,
            phones=[Phone.from_dict(i) for i in data["phones"]] if isinstance(data.get("phones"), list) else None,
            emails=[Email.from_dict(i) for i in data["emails"]] if isinstance(data.get("emails"), list) else None,
            attributes=[Attribute.from_dict(i) for i in data["attributes"]] if isinstance(data.get("attributes"), list) else None,
            contacts=data.get("contacts"),
            attachments=[AttachmentResource.from_dict(i) for i in data["attachments"]] if isinstance(data.get("attachments"), list) else None,
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
        )
