from __future__ import annotations

from sendpulse.auth.token_manager import TokenManager


class ApiKeyAuth:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def get_authorization_header(self) -> str:
        return f"Bearer {self._api_key}"

    def invalidate(self) -> None:
        pass

    def supports_refresh(self) -> bool:
        return False


class OAuthAuth:
    def __init__(self, token_manager: TokenManager) -> None:
        self._token_manager = token_manager

    def get_authorization_header(self) -> str:
        return f"Bearer {self._token_manager.get_token()}"

    def invalidate(self) -> None:
        self._token_manager.invalidate()

    def supports_refresh(self) -> bool:
        return True
