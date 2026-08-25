from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.WebhookListResponse import WebhookListResponse
from sendpulse.generated.email.model.WebhookResponse import WebhookResponse
from sendpulse.generated.email.model.WebhookResult import WebhookResult
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class WebhooksResource(AbstractService):
    def get_webhooks(self) -> WebhookListResponse:
        return WebhookListResponse.from_dict(self._send(Request(
            method="GET",
            uri="/v2/email-service/webhook",
        )))

    def create_webhook(self, body: dict[str, Any] | list[Any] | None = None) -> WebhookListResponse:
        return WebhookListResponse.from_dict(self._send(Request(
            method="POST",
            uri="/v2/email-service/webhook",
            body=json.dumps(body) if body else None,
        )))

    def get_webhook_by_id(self, id: int) -> WebhookResponse:
        return WebhookResponse.from_dict(self._send(Request(
            method="GET",
            uri=f"/v2/email-service/webhook/{id}",
        )))

    def update_webhook(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> WebhookResult:
        return WebhookResult.from_dict(self._send(Request(
            method="PUT",
            uri=f"/v2/email-service/webhook/{id}",
            body=json.dumps(body) if body else None,
        )))

    def delete_webhook(self, id: int) -> WebhookResult:
        return WebhookResult.from_dict(self._send(Request(
            method="DELETE",
            uri=f"/v2/email-service/webhook/{id}",
        )))
