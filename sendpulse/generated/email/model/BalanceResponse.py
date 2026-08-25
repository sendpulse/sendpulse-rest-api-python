from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BalanceResponse:
    currency: str | None = None
    balance_currency: float | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BalanceResponse:
        return cls(
            currency=data.get("currency"),
            balance_currency=data.get("balance_currency"),
        )
