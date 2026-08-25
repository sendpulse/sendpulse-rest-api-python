from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealAttributeValueResource(AbstractService):
    def get_deal_attribute_values(self, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/deals/{dealId}/attributes",
        ))

    def add_deal_attribute(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/deals/{dealId}/attributes",
            body=json.dumps(body) if body else None,
        ))

    def list_deal_attributes_by_pipeline(self, pipelineId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/deals/attributes/{pipelineId}",
        ))

    def update_deal_attribute_value(self, dealId: int, attributeId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/deals/{dealId}/attributes/{attributeId}",
            body=json.dumps(body) if body else None,
        ))
