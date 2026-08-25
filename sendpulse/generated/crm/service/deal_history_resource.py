from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealHistoryResource(AbstractService):
    def get_deal_history(self, dealId: int, fromDate: str, toDate: str) -> dict[str, Any]:
        params = {k: v for k, v in {"fromDate": fromDate, "toDate": toDate}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri=f"/deals/{dealId}/history",
            params=params or None,
        ))
