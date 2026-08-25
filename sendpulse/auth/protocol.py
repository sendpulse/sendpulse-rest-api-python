from __future__ import annotations

from typing import Protocol

from sendpulse.auth.token_storage import TokenData


class TokenStorageProtocol(Protocol):
    def get(self, key: str) -> TokenData | None: ...
    def set(self, key: str, token: TokenData) -> None: ...
    def delete(self, key: str) -> None: ...
