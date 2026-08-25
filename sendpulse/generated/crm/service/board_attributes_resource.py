from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class BoardAttributesResource(AbstractService):
    def get_board_attributes(self, boardId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/boards/{boardId}/attributes",
        ))

    def create_board_attribute(self, boardId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/boards/{boardId}/attributes",
            body=json.dumps(body) if body else None,
        ))

    def update_board_attribute(self, boardId: int, attributeId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/boards/{boardId}/attributes/{attributeId}",
            body=json.dumps(body) if body else None,
        ))
