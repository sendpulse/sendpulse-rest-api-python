from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TaskChecklistResource(AbstractService):
    def create_task_checklist(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/checklists/single",
            body=json.dumps(body) if body else None,
        ))

    def update_task_checklist_single(self, taskId: int, checklistId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/tasks/{taskId}/checklists/{checklistId}/single",
            body=json.dumps(body) if body else None,
        ))

    def get_task_checklists(self, taskId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/tasks/{taskId}/checklists",
        ))

    def create_task_checklists(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/checklists",
            body=json.dumps(body) if body else None,
        ))

    def update_task_checklists(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/tasks/{taskId}/checklists",
            body=json.dumps(body) if body else None,
        ))

    def delete_task_checklist(self, taskId: int, checklistId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/tasks/{taskId}/checklists/{checklistId}",
        ))
