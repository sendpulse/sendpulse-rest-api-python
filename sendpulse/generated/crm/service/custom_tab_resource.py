from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.crm.model.CustomTab import CustomTab
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class CustomTabResource(AbstractService):
    def get_custom_tabs(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/custom-tab",
        ))

    def create_custom_tab(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/custom-tab",
            body=json.dumps(body) if body else None,
        ))

    def update_custom_tab(self, customTabId: float, body: dict[str, Any] | list[Any] | None = None) -> CustomTab:
        return CustomTab.from_dict(self._send(Request(
            method="PUT",
            uri=f"/custom-tab/{customTabId}",
            body=json.dumps(body) if body else None,
        )))

    def delete_custom_tab(self, customTabId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/custom-tab/{customTabId}",
            body=json.dumps(body) if body else None,
        ))

    def add_custom_tab_relation(self, customTabId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/custom-tab/{customTabId}/relation",
            body=json.dumps(body) if body else None,
        ))

    def delete_custom_tab_relation(self, customTabId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/custom-tab/{customTabId}/relation",
            body=json.dumps(body) if body else None,
        ))
