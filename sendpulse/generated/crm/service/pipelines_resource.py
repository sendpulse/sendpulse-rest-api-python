from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class PipelinesResource(AbstractService):
    def get_pipelines(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/pipelines",
        ))

    def create_pipeline(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/pipelines",
            body=json.dumps(body) if body else None,
        ))

    def get_pipeline_by_id(self, pipelineId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/pipelines/{pipelineId}",
        ))

    def update_pipeline(self, pipelineId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/pipelines/{pipelineId}",
            body=json.dumps(body) if body else None,
        ))
