from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class EmailsResource(AbstractService):
    def get_company_emails(self, entityType: str, entityId: int, companyId: str) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/companies/{companyId}/emails",
        ))

    def create_company_email(self, entityType: str, entityId: int, companyId: str, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/companies/{companyId}/emails",
            body=json.dumps(body) if body else None,
        ))

    def batch_create_company_emails(self, companyId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/companies/{companyId}/emails/batch",
            body=json.dumps(body) if body else None,
        ))

    def update_company_email(self, companyId: int, emailId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/companies/{companyId}/emails/{emailId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_company_email(self, companyId: int, emailId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/companies/{companyId}/emails/{emailId}",
        ))
