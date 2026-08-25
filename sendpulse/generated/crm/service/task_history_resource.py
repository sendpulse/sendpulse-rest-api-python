from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TaskHistoryResource(AbstractService):
    def get_task_history(self, taskId: int, fromDate: str, toDate: str) -> dict[str, Any]:
        params = {k: v for k, v in {"fromDate": fromDate, "toDate": toDate}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri=f"/tasks/{taskId}/history",
            params=params or None,
        ))
