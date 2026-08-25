from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignCreateResponse:
    id: int | None = None
    status: int | None = None
    count: int | None = None
    tariff_email_qty: int | None = None
    overdraft_price: str | None = None
    ovedraft_currency: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignCreateResponse:
        return cls(
            id=data.get("id"),
            status=data.get("status"),
            count=data.get("count"),
            tariff_email_qty=data.get("tariff_email_qty"),
            overdraft_price=data.get("overdraft_price"),
            ovedraft_currency=data.get("ovedraft_currency"),
        )
