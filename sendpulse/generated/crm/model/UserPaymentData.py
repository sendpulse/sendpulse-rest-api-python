from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class UserPaymentData:
    id: int | None = None
    userId: int | None = None
    contactId: int | None = None
    dealId: int | None = None
    status: int | None = None
    firstName: str | None = None
    lastName: str | None = None
    name: str | None = None
    responsibleId: int | None = None
    price: dict[str, Any] | None = None
    description: str | None = None
    merchantName: str | None = None
    merchantUuid: str | None = None
    paymentMethod: str | None = None
    promoCode: str | None = None
    promoCodeDiscount: str | None = None
    createdAt: str | None = None
    externalContactId: str | None = None
    paymentItems: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> UserPaymentData:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            contactId=data.get("contactId"),
            dealId=data.get("dealId"),
            status=data.get("status"),
            firstName=data.get("firstName"),
            lastName=data.get("lastName"),
            name=data.get("name"),
            responsibleId=data.get("responsibleId"),
            price=data.get("price"),
            description=data.get("description"),
            merchantName=data.get("merchantName"),
            merchantUuid=data.get("merchantUuid"),
            paymentMethod=data.get("paymentMethod"),
            promoCode=data.get("promoCode"),
            promoCodeDiscount=data.get("promoCodeDiscount"),
            createdAt=data.get("createdAt"),
            externalContactId=data.get("externalContactId"),
            paymentItems=data.get("paymentItems"),
        )
