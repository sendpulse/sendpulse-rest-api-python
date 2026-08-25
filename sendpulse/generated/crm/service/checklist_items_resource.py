from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ChecklistItemsResource(AbstractService):
    def create_checklist_items(self, checklistId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/checklists/{checklistId}/items",
            body=json.dumps(body) if body else None,
        ))

    def reorder_checklist_item(self, checklistId: int, itemId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/checklists/{checklistId}/items/{itemId}",
            body=json.dumps(body) if body else None,
        ))

    def update_checklist_item(self, checklistId: int, itemId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/checklists/{checklistId}/items/{itemId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_checklist_item(self, checklistId: int, itemId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/checklists/{checklistId}/items/{itemId}",
        ))
