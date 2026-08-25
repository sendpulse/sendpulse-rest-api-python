from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DetailedBalanceResponse:
    balance: dict[str, Any] | None = None
    email: dict[str, Any] | None = None
    smtp: dict[str, Any] | None = None
    push: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DetailedBalanceResponse:
        return cls(
            balance=data.get("balance"),
            email=data.get("email"),
            smtp=data.get("smtp"),
            push=data.get("push"),
        )
