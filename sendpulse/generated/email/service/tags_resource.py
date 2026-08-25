from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.TagListResponse import TagListResponse
from sendpulse.generated.email.model.TagQueueResponse import TagQueueResponse
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TagsResource(AbstractService):
    def get_tags(self) -> TagListResponse:
        return TagListResponse.from_dict(self._send(Request(
            method="GET",
            uri="/tags",
        )))

    def create_tag(self, body: dict[str, Any] | list[Any] | None = None) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="POST",
            uri="/tags",
            body=json.dumps(body) if body else None,
        )))

    def update_tag(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="PUT",
            uri=f"/tags/{id}",
            body=json.dumps(body) if body else None,
        )))

    def delete_tag(self, id: int) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="DELETE",
            uri=f"/tags/{id}",
        )))

    def pin_tag_to_email(self, body: dict[str, Any] | list[Any] | None = None) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="POST",
            uri="/tags/pin/email",
            body=json.dumps(body) if body else None,
        )))

    def pin_tag_to_phone(self, body: dict[str, Any] | list[Any] | None = None) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="POST",
            uri="/tags/pin/phone",
            body=json.dumps(body) if body else None,
        )))

    def unpin_tag_from_email(self, body: dict[str, Any] | list[Any] | None = None) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="POST",
            uri="/tags/unpin/email",
            body=json.dumps(body) if body else None,
        )))

    def unpin_tag_from_phone(self, body: dict[str, Any] | list[Any] | None = None) -> TagQueueResponse:
        return TagQueueResponse.from_dict(self._send(Request(
            method="POST",
            uri="/tags/unpin/phone",
            body=json.dumps(body) if body else None,
        )))
