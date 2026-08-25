from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class PaymentOrderPrice:
    amount: str | None = None
    currency: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PaymentOrderPrice:
        return cls(
            amount=data.get("amount"),
            currency=data.get("currency"),
        )
