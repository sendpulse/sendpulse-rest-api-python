from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactTagsResource(AbstractService):
    def add_tag_to_contact(self, tagId: int, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contact-tags/{tagId}/contact/{contactId}",
        ))

    def delete_contact_tag_from_contact(self, tagId: int, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contact-tags/{tagId}/contact/{contactId}",
        ))

    def list_contact_tags(self, name: str | None = None, search: str | None = None) -> dict[str, Any]:
        params = {k: v for k, v in {"name": name, "search": search}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri="/contact-tags",
            params=params or None,
        ))

    def create_contact_tag(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/contact-tags",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_tag(self, tagId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contact-tags/{tagId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_tag(self, tagId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contact-tags/{tagId}",
        ))
