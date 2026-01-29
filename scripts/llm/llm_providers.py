from __future__ import annotations

import json
import ssl
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class LLMResponse:
    content: str
    raw: Dict[str, Any]


def _http_post_json(
    url: str,
    payload: Dict[str, Any],
    headers: Dict[str, str],
    timeout: int,
) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
        return json.loads(body)
    except (ssl.SSLError, urllib.error.URLError):
        return _curl_post_json(url, payload, headers, timeout=timeout)


def _curl_post_json(
    url: str,
    payload: Dict[str, Any],
    headers: Dict[str, str],
    timeout: int,
) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    cmd = ["curl", "-fsSL", "--max-time", str(timeout), "-X", "POST"]
    for k, v in headers.items():
        cmd.extend(["-H", f"{k}: {v}"])
    cmd.extend(["--data-binary", "@-", url])
    out = subprocess.check_output(cmd, input=data)
    return json.loads(out.decode("utf-8"))


def _post_with_retries(
    url: str,
    payload: Dict[str, Any],
    headers: Dict[str, str],
    timeout: int = 60,
    max_retries: int = 3,
) -> Dict[str, Any]:
    for attempt in range(1, max_retries + 1):
        try:
            return _http_post_json(url, payload, headers, timeout)
        except urllib.error.HTTPError as exc:
            status = getattr(exc, "code", None)
            if status in (429, 500, 502, 503, 504) and attempt < max_retries:
                time.sleep(2.0 * attempt)
                continue
            raise
        except urllib.error.URLError:
            if attempt < max_retries:
                time.sleep(2.0 * attempt)
                continue
            raise
    raise RuntimeError("Exceeded retry budget")


def call_openai_compatible(
    api_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    timeout: int = 60,
    max_retries: int = 3,
) -> LLMResponse:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    raw = _post_with_retries(api_url, payload, headers, timeout=timeout, max_retries=max_retries)
    choices = raw.get("choices") or []
    if not choices:
        raise RuntimeError("No choices returned")
    content = (choices[0].get("message") or {}).get("content")
    if not isinstance(content, str):
        raise RuntimeError("Missing message.content in response")
    return LLMResponse(content=content, raw=raw)


def call_anthropic(
    api_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int = 1024,
    timeout: int = 60,
    max_retries: int = 3,
) -> LLMResponse:
    # Anthropic "messages" API expects system separately.
    system_parts: List[str] = []
    converted: List[Dict[str, str]] = []
    for msg in messages:
        role = msg.get("role")
        content = msg.get("content", "")
        if role == "system":
            system_parts.append(content)
            continue
        if role == "user":
            converted.append({"role": "user", "content": content})
        elif role == "assistant":
            converted.append({"role": "assistant", "content": content})
        else:
            converted.append({"role": "user", "content": content})

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    payload: Dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": converted,
    }
    system_text = "\n".join([p for p in system_parts if p]).strip()
    if system_text:
        payload["system"] = system_text

    raw = _post_with_retries(api_url, payload, headers, timeout=timeout, max_retries=max_retries)
    content_blocks = raw.get("content") or []
    if not isinstance(content_blocks, list) or not content_blocks:
        raise RuntimeError("Missing content blocks in response")
    # Prefer first text block
    for block in content_blocks:
        if isinstance(block, dict) and block.get("type") == "text" and isinstance(block.get("text"), str):
            return LLMResponse(content=block["text"], raw=raw)
    raise RuntimeError("No text content block found")


def call_gemini(
    api_base: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_output_tokens: int = 1024,
    timeout: int = 60,
    max_retries: int = 3,
) -> LLMResponse:
    # Gemini API uses API key in query string.
    api_base = api_base.rstrip("/")
    url = f"{api_base}/models/{urllib.parse.quote(model)}:generateContent?key={urllib.parse.quote(api_key)}"

    system_parts: List[str] = []
    contents: List[Dict[str, Any]] = []
    for msg in messages:
        role = msg.get("role")
        content = msg.get("content", "")
        if role == "system":
            system_parts.append(content)
            continue
        # Gemini roles: "user" or "model"
        gemini_role = "user" if role != "assistant" else "model"
        contents.append({"role": gemini_role, "parts": [{"text": content}]})

    payload: Dict[str, Any] = {
        "contents": contents,
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_output_tokens,
        },
    }
    system_text = "\n".join([p for p in system_parts if p]).strip()
    if system_text:
        payload["systemInstruction"] = {"parts": [{"text": system_text}]}

    headers = {"Content-Type": "application/json"}
    raw = _post_with_retries(url, payload, headers, timeout=timeout, max_retries=max_retries)

    candidates = raw.get("candidates") or []
    if not isinstance(candidates, list) or not candidates:
        raise RuntimeError("No candidates returned")
    content = candidates[0].get("content") if isinstance(candidates[0], dict) else None
    parts = content.get("parts") if isinstance(content, dict) else None
    if isinstance(parts, list) and parts and isinstance(parts[0], dict) and isinstance(parts[0].get("text"), str):
        return LLMResponse(content=parts[0]["text"], raw=raw)
    raise RuntimeError("Could not extract text from Gemini response")


def call_ollama(
    api_url: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    timeout: int = 60,
    max_retries: int = 3,
) -> LLMResponse:
    headers = {"Content-Type": "application/json"}
    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature},
    }
    raw = _post_with_retries(api_url, payload, headers, timeout=timeout, max_retries=max_retries)
    message = raw.get("message") if isinstance(raw, dict) else None
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, str):
        raise RuntimeError("Missing message.content in Ollama response")
    return LLMResponse(content=content, raw=raw)
