from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TasksBoardsResource(AbstractService):
    def get_boards(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/boards",
        ))

    def create_board(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/boards",
            body=json.dumps(body) if body else None,
        ))

    def get_board_by_id(self, boardId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/boards/{boardId}",
        ))

    def update_board(self, boardId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/boards/{boardId}",
            body=json.dumps(body) if body else None,
        ))
