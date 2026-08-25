from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class PipelineStepsResource(AbstractService):
    def get_pipeline_steps(self, pipelineId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/pipelines/{pipelineId}/steps",
        ))

    def create_pipeline_step(self, pipelineId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/pipelines/{pipelineId}/steps",
            body=json.dumps(body) if body else None,
        ))

    def update_pipeline_step(self, pipelineId: int, stepId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/pipelines/{pipelineId}/steps/{stepId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_pipeline_step(self, pipelineId: int, stepId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/pipelines/{pipelineId}/steps/{stepId}",
        ))
