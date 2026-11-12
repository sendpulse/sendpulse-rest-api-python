"""Loader for the generated operation-map fragments.

Each module under ``sendpulse.resources.operations`` exposes an ``OPERATIONS``
dict keyed by a dotted operation key. This merges them into a single map, cached
for the life of the process.
"""
from __future__ import annotations

import importlib
import pkgutil
from typing import Any

OperationMap = dict[str, dict[str, Any]]

_cache: OperationMap | None = None


def load_operations() -> OperationMap:
    global _cache
    if _cache is None:
        from sendpulse.resources import operations as _ops_pkg

        merged: OperationMap = {}
        for mod in pkgutil.iter_modules(_ops_pkg.__path__):
            module = importlib.import_module(f"{_ops_pkg.__name__}.{mod.name}")
            merged.update(getattr(module, "OPERATIONS", {}))
        _cache = merged
    return _cache
