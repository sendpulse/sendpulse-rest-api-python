from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ECommerceProductResource(AbstractService):
    def get_products_by_filter(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/products/all",
            body=json.dumps(body) if body else None,
        ))

    def get_category_product(self, productId: float, categoryId: float) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/products/categories/{categoryId}/{productId}",
        ))

    def add_product_to_deal(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/products/deals",
            body=json.dumps(body) if body else None,
        ))

    def get_products_by_deal_id(self, dealId: float) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/products/deals/{dealId}",
        ))

    def update_products_in_deal(self, headId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/products/deals/{headId}",
            body=json.dumps(body) if body else None,
        ))

    def get_products_by_contact_deals(self, contactId: float) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/products/contacts/{contactId}/deals",
        ))

    def detach_product_from_deal(self, categoryId: float, productId: float, headId: float) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/products/categories/{categoryId}/{productId}/deals/{headId}",
        ))

    def get_product_by_id(self, productId: float) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/products/{productId}",
        ))

    def update_product(self, productId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/products/{productId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_product(self, productId: float) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/products/{productId}",
        ))

    def update_product_category(self, categoryId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/products/categories/{categoryId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_product_category(self, categoryId: float) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/products/categories/{categoryId}",
        ))

    def get_product_categories(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/products/categories",
        ))

    def create_product_category(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/products/categories",
            body=json.dumps(body) if body else None,
        ))

    def update_product_prices(self, productId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/products/{productId}/prices",
            body=json.dumps(body) if body else None,
        ))

    def create_product_sections(self, productId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/products/{productId}/sections",
            body=json.dumps(body) if body else None,
        ))

    def update_product_sections(self, productId: float, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/products/{productId}/sections",
            body=json.dumps(body) if body else None,
        ))

    def delete_product_section(self, productId: float, sectionId: float) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/products/{productId}/sections/{sectionId}",
        ))

    def create_product(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/products",
            body=json.dumps(body) if body else None,
        ))
