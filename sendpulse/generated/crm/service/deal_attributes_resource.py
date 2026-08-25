from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealAttributesResource(AbstractService):
    def list_pipeline_attributes(self, pipelineId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/pipelines/{pipelineId}/attributes",
        ))

    def create_pipeline_attribute(self, pipelineId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/pipelines/{pipelineId}/attributes",
            body=json.dumps(body) if body else None,
        ))

    def update_pipeline_attribute(self, pipelineId: int, attributeId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/pipelines/{pipelineId}/attributes/{attributeId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_pipeline_attribute(self, pipelineId: int, attributeId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/pipelines/{pipelineId}/attributes/{attributeId}",
        ))

    def delete_deal_attribute(self, dealId: int, attributeId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/deals/{dealId}/attributes/{attributeId}",
        ))
