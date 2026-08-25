from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.smtp.model.ResultTrue import ResultTrue
from sendpulse.generated.smtp.model.SentEmail import SentEmail
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class UnsubscribeResource(AbstractService):
    def get_smtp_unsubscribed(self, date: str | None = None, limit: int | None = None, offset: int | None = None) -> dict[str, Any]:
        params = {k: v for k, v in {"date": date, "limit": limit, "offset": offset}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri="/smtp/unsubscribe",
            params=params or None,
        ))

    def unsubscribe_smtp_recipients(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri="/smtp/unsubscribe",
            body=json.dumps(body) if body else None,
        )))

    def remove_smtp_unsubscribe(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri="/smtp/unsubscribe",
            body=json.dumps(body) if body else None,
        )))

    def search_smtp_unsubscribe(self, email: str) -> ResultTrue:
        params = {k: v for k, v in {"email": email}.items() if v is not None}
        return ResultTrue.from_dict(self._send(Request(
            method="GET",
            uri="/smtp/unsubscribe/search",
            params=params or None,
        )))

    def resubscribe_smtp_recipient(self, body: dict[str, Any] | list[Any] | None = None) -> SentEmail:
        return SentEmail.from_dict(self._send(Request(
            method="POST",
            uri="/smtp/resubscribe",
            body=json.dumps(body) if body else None,
        )))
