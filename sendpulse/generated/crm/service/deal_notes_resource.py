from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealNotesResource(AbstractService):
    def get_deal_comments(self, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/deals/{dealId}/comments",
        ))

    def add_deal_comment(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/deals/{dealId}/comments",
            body=json.dumps(body) if body else None,
        ))

    def update_deal_comment(self, dealId: int, commentId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/deals/{dealId}/comments/{commentId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_deal_comment(self, dealId: int, commentId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/deals/{dealId}/comments/{commentId}",
        ))
