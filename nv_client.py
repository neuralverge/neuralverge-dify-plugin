"""Shared HTTP client for the NeuralVerge tools. Every tool is a thin wrapper over one REST endpoint."""
import json
from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

API_BASE = "https://api.neuralverge.ai/functions/v1"
REQUEST_TIMEOUT = 290

ERROR_HINTS = {
    400: "the request parameters are invalid",
    401: "the API key is missing, invalid, or expired",
    402: "plan or usage limits reached",
    404: "the requested resource does not exist or is not available",
    429: "rate limit exceeded, retry shortly",
    500: "upstream provider or temporary service failure",
}


def _headers(api_key: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}


def _parse(response: requests.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        return response.text


def _raise_for_status(response: requests.Response) -> None:
    if response.ok:
        return
    hint = ERROR_HINTS.get(response.status_code, "request failed")
    detail = _parse(response)
    if not isinstance(detail, str):
        detail = json.dumps(detail, ensure_ascii=False)
    raise Exception(f"NeuralVerge API error ({response.status_code}): {hint}. {detail}")


def _coerce(value: Any, kind: str) -> Any:
    """Converts a Dify parameter value to what the API expects; None means 'leave it out'."""
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    if kind == "integer":
        return int(float(value))
    if kind == "number":
        return float(value)
    if kind == "boolean":
        if isinstance(value, str):
            return value.strip().lower() in ("true", "1", "yes")
        return bool(value)
    if kind == "array":
        if isinstance(value, list):
            return value
        text = str(value).strip()
        if text.startswith("["):
            return json.loads(text)
        return [item.strip() for item in text.split(",") if item.strip()]
    if kind == "object":
        return value if isinstance(value, dict) else json.loads(str(value))
    return str(value)


def build_body(fields: dict[str, str], groups: dict[str, dict[str, str]], params: dict[str, Any]) -> dict[str, Any]:
    flattened = {f"{group}_{sub}" for group, subs in groups.items() for sub in subs}
    body: dict[str, Any] = {}
    for key, kind in fields.items():
        if key in flattened:
            continue
        value = _coerce(params.get(key), kind)
        if value is not None:
            body[key] = value
    for group, subs in groups.items():
        nested = {}
        for sub, kind in subs.items():
            value = _coerce(params.get(f"{group}_{sub}"), kind)
            if value is not None:
                nested[sub] = value
        if nested:
            body[group] = nested
    return body


def call(
    tool: Tool,
    endpoint: str,
    fields: dict[str, str],
    groups: dict[str, dict[str, str]],
    params: dict[str, Any],
) -> Generator[ToolInvokeMessage]:
    api_key = tool.runtime.credentials.get("api_key")
    if not api_key:
        raise Exception("NeuralVerge API key is not configured.")
    try:
        body = build_body(fields, groups, params)
    except (ValueError, TypeError) as exc:
        raise Exception(f"Invalid parameter value: {exc}")
    response = requests.post(
        f"{API_BASE}/{endpoint}", headers=_headers(api_key), json=body, timeout=REQUEST_TIMEOUT
    )
    _raise_for_status(response)
    data = _parse(response)
    yield tool.create_json_message(data if isinstance(data, dict) else {"result": data})


def check_api_key(api_key: str) -> None:
    """Calls a free endpoint with an unknown session id: a bad key fails with 401, a good one with 404."""
    response = requests.get(
        f"{API_BASE}/get-session-status",
        params={"session_id": "00000000-0000-0000-0000-000000000000"},
        headers=_headers(api_key),
        timeout=30,
    )
    if response.status_code == 401:
        raise Exception("The API key is invalid or expired.")
