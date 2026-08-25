from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TaskCommentsResource(AbstractService):
    def add_task_comment(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/comments",
            body=json.dumps(body) if body else None,
        ))

    def update_task_comment(self, taskId: int, commentId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/tasks/{taskId}/comments/{commentId}",
            body=json.dumps(body) if body else None,
        ))
