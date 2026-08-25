from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.PaymentOrderPrice import PaymentOrderPrice


@dataclass(slots=True)
class Payment:
    id: int | None = None
    name: str | None = None
    price: PaymentOrderPrice | None = None
    status: int | None = None
    orderId: str | None = None
    paymentDescription: str | None = None
    paymentMethod: str | None = None
    createdAt: str | None = None
    promoCode: str | None = None
    promoCodeDiscount: float | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Payment:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            price=PaymentOrderPrice.from_dict(data["price"]) if isinstance(data.get("price"), dict) else None,
            status=data.get("status"),
            orderId=data.get("orderId"),
            paymentDescription=data.get("paymentDescription"),
            paymentMethod=data.get("paymentMethod"),
            createdAt=data.get("createdAt"),
            promoCode=data.get("promoCode"),
            promoCodeDiscount=data.get("promoCodeDiscount"),
        )
