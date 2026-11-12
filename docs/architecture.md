# Thin client architecture & decisions

_Status as of 2026-10-27._

Record of what we built, why, and what's left — so the next session (human or AI)
can pick up without re-deriving it. The Python SDK is a direct analog of the PHP
one; this mirrors its architecture doc.

## Goal

A **thin client** (no generated typed-model layer) that is still **user-friendly**
(IDE autocomplete) and **AI-friendly** (machine-readable, loadable by coding
agents).

## Core decisions

1. **Drop the generated typed layer.** An earlier attempt generated dataclass
   models + resource/service classes per endpoint (`sendpulse/generated/…`). It
   was high-maintenance and low-value — deleted. The failed concept lives only in
   the abandoned sibling repo for reference.

2. **Thin transport stays.** `Client`, `Config`, `http/*`, `auth/*`, token
   storage, `response/validator`, `exception/*`. The `HttpClient` protocol
   (`send(Request) -> Response`) is the **seam** — any object with that method can
   replace the bundled `httpx` transport.

3. **Client surface = `get/post/put/patch/delete`** over `request()`/`send()`.
   Dict bodies are JSON-encoded; `get()` dict params become the query string.

4. **Operation map, not code, for discoverability.** A flat data map keyed by a
   dotted call-chain is the single source of truth.

5. **Chained surface + flat map:**
   - `client.crm.deals.getDeal({"dealId": 5})`
   - validation is **shallow** (required top-level + path params only); body shape
     is judged by the API, not us.

## How it works

### Runtime (SDK)

- `sendpulse/resources/operations/<service>.py` — generated map fragments, each an
  `OPERATIONS` dict.
- `sendpulse/resources/__init__.py` — `load_operations()` globs + merges the
  fragments (pkgutil), cached for the process.
- `Client.__getattr__` returns a `Resource` proxy; `Resource.__getattr__` extends
  the dotted key; `Resource.__call__` dispatches via `Client.call_operation()`.
- `call_operation()` looks up the key, validates required params, substitutes
  `{path}` params (url-encoded), routes declared params (path vs query), and
  passes any **undeclared** param through (query for GET, JSON body otherwise).

### Call convention

One dict. Path params (`{name}`) + declared query params are routed automatically;
everything else → body (GET → query). `"!"` in a param type = required.

### IDE autocomplete

- `sendpulse/stubs.pyi` — generated phantom classes mirroring the chain: service
  classes with one attribute per resource; resource classes with real method
  signatures. Each method's HTTP route + parameter list is in its docstring.
- `client.py` declares `crm: Crm`, … under `TYPE_CHECKING` (importing from
  `sendpulse.stubs`), so checkers resolve the chain while `__getattr__` drives it
  at runtime.
- **Stub signature style: `params: dict[str, Any]` + docstring.** Rejected
  alternatives: per-op `TypedDict` (closed — would reject the undeclared body keys
  most POST ops rely on) and kwargs (would diverge from the dict-call convention).
  The stub still catches unknown resources/methods and missing required args.
- Not imported at runtime (zero cost). PyCharm / Pylance / mypy pick it up.

### AI

- `llms.txt` (repo root) — generated: static Python-usage header + full endpoint
  catalog from the map. One file an agent loads to know auth, conventions, error
  classes, and every path + required param.

## Generator (`/Users/bilovol/Projects/sdk-generator`)

- `generators/python/generate.py` — parse spec → extract path/params/naming →
  emit the flat map fragment. (Rewritten from the old typed-model generator.)
- Chain key = `service.resource.method` = `alias` + `lcfirst(tag)` +
  `lcfirst(operationId)`. Method names kept verbatim from `operationId`.
- **Base path fix:** the path prefix (`/crm/v1`, `/chatbots`) lives in
  `servers[0].url`; the generator prepends its path component (host is added by
  `Client`).
- `generators/python/generate_stubs.py` — map → `sendpulse/stubs.pyi`.
- `generators/python/generate_llms.py` — map → `llms.txt`.
- `generate.sh` chains all three passes (and bootstraps a local venv with PyYAML),
  so map + stubs + llms can't drift.
- `sdks.json`: python `output_path` → `sendpulse/resources/operations`.
- Verified **byte-for-byte parity** with the PHP generator's map (287 ops, 0
  key/method/path/params differences).

## Current state

- **287 operations** generated: crm 189, email 60, sms 18, smtp 17, chatbot 3.
- mypy `strict` **green**; **344 tests** pass; ruff clean.
- Dict-call dispatch validated (path substitution, routing, required params,
  unknown op, raw verbs, OAuth 401-retry, api-key no-retry).

## Known caveats

- One CRM key collision (`crm.eCommerceProduct.updateProductSections`): two
  operations share tag+operationId; last wins (logged as WARN). Same as PHP.
- `sendpulse/resources/operations/` and `stubs.pyi` are generated — excluded from
  ruff (and the fragments from mypy).

## Open / next steps

- Confirm the release version (`2.0.0`; legacy PyPI `pysendpulse` was `0.1.8`).
- Commit / PR (not done yet).
