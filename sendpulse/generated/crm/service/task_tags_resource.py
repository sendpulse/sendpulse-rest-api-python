from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TaskTagsResource(AbstractService):
    def detach_tag_from_task(self, tagId: int, taskId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/task-tags/{tagId}/task/{taskId}",
        ))

    def get_task_tags(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/task-tags",
        ))

    def create_task_tag(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/task-tags",
            body=json.dumps(body) if body else None,
        ))

    def update_task_tag(self, tagId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/task-tags/{tagId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_task_tag(self, tagId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/task-tags/{tagId}",
        ))
