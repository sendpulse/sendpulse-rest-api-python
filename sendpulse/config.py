from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Config:
    api_key: str | None = field(default=None, repr=False)
    client_id: str | None = field(default=None, repr=False)
    client_secret: str | None = field(default=None, repr=False)
    connect_timeout: float = 10.0
    request_timeout: float = 30.0
    cache_dir: str | None = None

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        has_api_key = bool(self.api_key)
        has_oauth = bool(self.client_id) and bool(self.client_secret)

        if not has_api_key and not has_oauth:
            raise ValueError("Provide either api_key or both client_id and client_secret.")

        if has_api_key and (self.client_id or self.client_secret):
            raise ValueError("Provide either api_key or client_id+client_secret, not both.")

    @property
    def is_oauth(self) -> bool:
        return self.client_id is not None
