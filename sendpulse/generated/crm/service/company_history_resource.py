from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class CompanyHistoryResource(AbstractService):
    def get_company_history(self, companyId: str, dateFrom: str | None = None, dateTo: str | None = None, limit: int | None = None, offset: int | None = None) -> dict[str, Any]:
        params = {k: v for k, v in {"dateFrom": dateFrom, "dateTo": dateTo, "limit": limit, "offset": offset}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri=f"/companies/{companyId}/history",
            params=params or None,
        ))
