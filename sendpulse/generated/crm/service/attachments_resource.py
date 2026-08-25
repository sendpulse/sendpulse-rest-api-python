from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class AttachmentsResource(AbstractService):
    def create_attachment(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/attachments",
            body=json.dumps(body) if body else None,
        ))

    def create_attachments_batch(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/attachments/batch",
            body=json.dumps(body) if body else None,
        ))

    def update_attachment(self, attachmentId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/attachments/{attachmentId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_attachment(self, attachmentId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/attachments/{attachmentId}",
        ))
