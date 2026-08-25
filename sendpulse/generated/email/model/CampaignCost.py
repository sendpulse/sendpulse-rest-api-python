from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignCost:
    cur: str | None = None
    sent_emails_qty: int | None = None
    overdraftAllEmailsPrice: float | None = None
    result: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignCost:
        return cls(
            cur=data.get("cur"),
            sent_emails_qty=data.get("sent_emails_qty"),
            overdraftAllEmailsPrice=data.get("overdraftAllEmailsPrice"),
            result=data.get("result"),
        )
