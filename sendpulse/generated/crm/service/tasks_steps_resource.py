from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TasksStepsResource(AbstractService):
    def create_board_steps(self, boardId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/boards/{boardId}/steps",
            body=json.dumps(body) if body else None,
        ))

    def update_board_step(self, boardId: int, stepId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/boards/{boardId}/steps/{stepId}",
            body=json.dumps(body) if body else None,
        ))
