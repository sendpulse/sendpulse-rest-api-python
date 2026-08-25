from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TasksResource(AbstractService):
    def list_tasks(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/tasks/list",
            body=json.dumps(body) if body else None,
        ))

    def create_task(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/tasks",
            body=json.dumps(body) if body else None,
        ))

    def get_task_repeat_templates(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/tasks-repeat/templates",
        ))

    def get_task_by_id(self, taskId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/tasks/{taskId}",
        ))

    def update_task_by_id(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/tasks/{taskId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_task(self, taskId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/tasks/{taskId}",
        ))

    def set_task_parent(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/parent",
            body=json.dumps(body) if body else None,
        ))

    def change_task_step_order(self, taskId: int, stepId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/steps/{stepId}/order",
            body=json.dumps(body) if body else None,
        ))
