from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class MessengersResource(AbstractService):
    def get_company_messengers(self, companyId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/companies/{companyId}/messengers",
        ))

    def create_company_messenger(self, entityType: str, entityId: int, companyId: str, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/companies/{companyId}/messengers",
            body=json.dumps(body) if body else None,
        ))

    def batch_create_company_messengers(self, companyId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/companies/{companyId}/messengers/batch",
            body=json.dumps(body) if body else None,
        ))

    def update_company_messenger(self, entityType: str, entityId: int, messengerId: int, companyId: str, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/companies/{companyId}/messengers/{messengerId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_company_messenger(self, entityType: str, entityId: int, messengerId: int, companyId: str) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/companies/{companyId}/messengers/{messengerId}",
        ))
