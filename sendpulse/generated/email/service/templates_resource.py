from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.ResultTrue import ResultTrue
from sendpulse.generated.email.model.TemplateCreation import TemplateCreation
from sendpulse.generated.email.model.TemplateDetails import TemplateDetails
from sendpulse.generated.email.model.TemplateSummary import TemplateSummary
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TemplatesResource(AbstractService):
    def create_template(self, body: dict[str, Any] | list[Any] | None = None) -> TemplateCreation:
        return TemplateCreation.from_dict(self._send(Request(
            method="POST",
            uri="/template",
            body=json.dumps(body) if body else None,
        )))

    def update_template(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri=f"/template/edit/{id}",
            body=json.dumps(body) if body else None,
        )))

    def get_template_by_id(self, template_id: str, owner: str | None = None, lang: str | None = None) -> TemplateDetails:
        params = {k: v for k, v in {"owner": owner, "lang": lang}.items() if v is not None}
        return TemplateDetails.from_dict(self._send(Request(
            method="GET",
            uri=f"/template/{template_id}",
            params=params or None,
        )))

    def get_template_by_slug(self, name_slug: str, owner: str | None = None, lang: str | None = None) -> TemplateDetails:
        params = {k: v for k, v in {"owner": owner, "lang": lang}.items() if v is not None}
        return TemplateDetails.from_dict(self._send(Request(
            method="GET",
            uri=f"/template/slug/{name_slug}",
            params=params or None,
        )))

    def get_templates(self, owner: str | None = None, only_active: bool | None = None, limit: int | None = None, offset: int | None = None) -> list[TemplateSummary]:
        params = {k: v for k, v in {"owner": owner, "only_active": only_active, "limit": limit, "offset": offset}.items() if v is not None}
        return [TemplateSummary.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri="/templates",
            params=params or None,
        ))]
