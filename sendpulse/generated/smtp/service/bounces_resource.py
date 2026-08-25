from __future__ import annotations

from typing import Any

from sendpulse.generated.smtp.model.BounceReport import BounceReport
from sendpulse.generated.smtp.model.TotalCount import TotalCount
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class BouncesResource(AbstractService):
    def get_bounce_report(self, date: str | None = None, limit: int | None = None, offset: int | None = None) -> BounceReport:
        params = {k: v for k, v in {"date": date, "limit": limit, "offset": offset}.items() if v is not None}
        return BounceReport.from_dict(self._send(Request(
            method="GET",
            uri="/smtp/bounces/day",
            params=params or None,
        )))

    def get_smtp_bounces_total(self) -> TotalCount:
        return TotalCount.from_dict(self._send(Request(
            method="GET",
            uri="/smtp/bounces/day/total",
        )))
