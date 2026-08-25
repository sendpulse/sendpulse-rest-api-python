from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ManagerSettingsResource(AbstractService):
    def list_manager_settings_sections(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/manager-settings/sections",
        ))

    def get_manager_settings_managers(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/manager-settings/managers",
        ))

    def create_manager_settings(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/manager-settings",
            body=json.dumps(body) if body else None,
        ))

    def update_manager_setting(self, settingId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/manager-settings/{settingId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_managers_from_manager_setting(self, settingId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/manager-settings/{settingId}",
            body=json.dumps(body) if body else None,
        ))

    def get_managers_by_section(self, sectionId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/manager-settings/{sectionId}",
        ))
