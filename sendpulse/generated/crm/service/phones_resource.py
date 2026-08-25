from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class PhonesResource(AbstractService):
    def get_company_phones(self, companyId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/companies/{companyId}/phones",
        ))

    def create_company_phone(self, companyId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/companies/{companyId}/phones",
            body=json.dumps(body) if body else None,
        ))

    def batch_create_company_phones(self, companyId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/companies/{companyId}/phones/batch",
            body=json.dumps(body) if body else None,
        ))

    def update_company_phone(self, entityType: str, entityId: int, phoneId: int, companyId: str, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/companies/{companyId}/phones/{phoneId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_company_phone(self, entityType: str, entityId: int, phoneId: int, companyId: str) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/companies/{companyId}/phones/{phoneId}",
        ))
