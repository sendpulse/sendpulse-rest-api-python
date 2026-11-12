from __future__ import annotations

import json
import os
import tempfile
from typing import TypedDict

try:
    import fcntl as _fcntl

    _HAS_FCNTL = True
except ImportError:
    _HAS_FCNTL = False


class TokenData(TypedDict):
    access_token: str
    token_type: str
    expires_at: int


class FileTokenStorage:
    def __init__(self, cache_dir: str | None = None) -> None:
        if cache_dir:
            self._dir = cache_dir
        else:
            dirname = f"sendpulse-{os.getuid()}-tokens" if hasattr(os, "getuid") else "sendpulse-tokens"
            self._dir = os.path.join(tempfile.gettempdir(), dirname)
        os.makedirs(self._dir, mode=0o700, exist_ok=True)

    def get(self, key: str) -> TokenData | None:
        path = self._path(key)
        flags = os.O_RDONLY
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        try:
            fd = os.open(path, flags)
        except OSError:
            return None
        try:
            with os.fdopen(fd, "r") as f:
                if _HAS_FCNTL:
                    _fcntl.flock(f, _fcntl.LOCK_SH)
                    try:
                        data: object = json.load(f)
                    finally:
                        _fcntl.flock(f, _fcntl.LOCK_UN)
                else:
                    data = json.load(f)
        except (OSError, json.JSONDecodeError):
            return None

        if not self._is_valid(data):
            return None

        return data  # type: ignore[return-value]

    def set(self, key: str, token: TokenData) -> None:
        path = self._path(key)
        try:
            fd, tmp = tempfile.mkstemp(dir=self._dir, prefix="sp_", suffix=".json.tmp")
            try:
                with os.fdopen(fd, "w") as f:
                    if _HAS_FCNTL:
                        _fcntl.flock(f, _fcntl.LOCK_EX)
                        try:
                            json.dump(token, f)
                        finally:
                            _fcntl.flock(f, _fcntl.LOCK_UN)
                    else:
                        json.dump(token, f)
            except Exception:
                try:
                    os.unlink(tmp)
                except OSError:
                    pass
                raise
            os.replace(tmp, path)
        except OSError as e:
            raise RuntimeError(f"Cannot write token cache file: {path}") from e

    def delete(self, key: str) -> None:
        path = self._path(key)
        try:
            os.unlink(path)
        except FileNotFoundError:
            pass

    def _path(self, key: str) -> str:
        return os.path.join(self._dir, f"sp_token_{key}.json")

    @staticmethod
    def _is_valid(data: object) -> bool:
        return (
            isinstance(data, dict)
            and isinstance(data.get("access_token"), str)
            and isinstance(data.get("token_type"), str)
            and isinstance(data.get("expires_at"), int)
        )


class InMemoryTokenStorage:
    def __init__(self) -> None:
        self._store: dict[str, TokenData] = {}

    def get(self, key: str) -> TokenData | None:
        return self._store.get(key)

    def set(self, key: str, token: TokenData) -> None:
        self._store[key] = token

    def delete(self, key: str) -> None:
        self._store.pop(key, None)
