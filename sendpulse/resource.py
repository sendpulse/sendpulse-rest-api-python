from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sendpulse.client import Client


class Resource:
    """Chained accessor over the operation map.

    Attribute access extends the dotted operation key; calling the resource
    dispatches it:

        client.crm.deals.getDeal({"dealId": 5})  ->  key "crm.deals.getDeal"
    """

    __slots__ = ("_client", "_prefix")

    def __init__(self, client: Client, prefix: str) -> None:
        self._client = client
        self._prefix = prefix

    def __getattr__(self, name: str) -> Resource:
        if name.startswith("_"):
            raise AttributeError(name)
        return Resource(self._client, f"{self._prefix}.{name}")

    def __call__(self, params: dict[str, Any] | None = None) -> dict[str, Any] | list[Any]:
        return self._client.call_operation(self._prefix, params or {})

    def __repr__(self) -> str:
        return f"<Resource {self._prefix!r}>"
