from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealsResource(AbstractService):
    def get_deals_list(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/deals/get-list",
            body=json.dumps(body) if body else None,
        ))

    def create_deal(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/deals",
            body=json.dumps(body) if body else None,
        ))

    def get_deal(self, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/deals/{dealId}",
        ))

    def update_deal_by_id(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/deals/{dealId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_deal(self, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/deals/{dealId}",
        ))

    def change_deal_pipeline(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/deals/{dealId}/change-pipeline",
            body=json.dumps(body) if body else None,
        ))
