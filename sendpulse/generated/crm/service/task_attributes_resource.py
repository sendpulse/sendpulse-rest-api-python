from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TaskAttributesResource(AbstractService):
    def create_task_attribute_value(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/attributes",
            body=json.dumps(body) if body else None,
        ))

    def update_task_attribute_value(self, attributeId: int, valueId: int, boardId: str, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/{boardId}/attributes/{attributeId}/values/{valueId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_attribute_value(self, attributeId: int, valueId: int, boardId: str) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/{boardId}/attributes/{attributeId}/values/{valueId}",
        ))
