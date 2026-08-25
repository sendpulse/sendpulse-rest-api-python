from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealExpirationResource(AbstractService):
    def upsert_deal_expiration(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/deals/{dealId}/expiration",
            body=json.dumps(body) if body else None,
        ))

    def remove_deal_expiration(self, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/deals/{dealId}/expiration",
        ))
