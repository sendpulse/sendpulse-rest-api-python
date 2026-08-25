from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactsResource(AbstractService):
    def get_contacts_list(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/contacts/get-list",
            body=json.dumps(body) if body else None,
        ))

    def get_contact_list_by_email(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/contacts/get-list-by-email",
            body=json.dumps(body) if body else None,
        ))

    def create_contact(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/contacts",
            body=json.dumps(body) if body else None,
        ))

    def get_contact_by_id(self, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/{contactId}",
        ))

    def update_contact(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/{contactId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_by_id(self, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}",
        ))

    def get_contact_deals(self, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/{contactId}/deals",
        ))

    def add_contact_comment(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/comments",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_comment(self, contactId: int, commentId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/{contactId}/comments/{commentId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_comment(self, contactId: int, commentId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}/comments/{commentId}",
        ))

    def get_contact_edu_payments(self, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/{contactId}/edu-payments",
        ))

    def get_contact_edu_statistic(self, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/{contactId}/edu-statistic",
        ))

    def get_contact_by_external_id(self, externalContactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/external/{externalContactId}",
        ))

    def get_contact_by_messenger_external_id(self, messengerContactId: str) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/messenger-external/{messengerContactId}",
        ))

    def add_contact_company_relation(self, contactId: int, companyId: int) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/relation/{companyId}",
        ))

    def delete_contact_company_relation(self, contactId: int, companyId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}/relation/{companyId}",
        ))
