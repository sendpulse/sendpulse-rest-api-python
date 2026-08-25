from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TaskEntityResource(AbstractService):
    def detach_contact_from_task(self, taskId: int, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/task-contacts/{taskId}/contact/{contactId}",
        ))

    def detach_deal_from_task(self, taskId: int, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/task-deals/{taskId}/deal/{dealId}",
        ))

    def detach_task_from_task(self, taskHeadId: int, taskId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/task-to-task/{taskHeadId}/task/{taskId}",
        ))

    def attach_entities_to_task(self, taskId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/tasks/{taskId}/entity-attach",
            body=json.dumps(body) if body else None,
        ))
