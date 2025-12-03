from __future__ import annotations

import json
import logging
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv

LOGGER = logging.getLogger(__name__)


@dataclass
class JetstreamConfig:
    base_url: str
    api_key: str | None
    model: str
    temperature: float = 0.5
    top_p: float = 0.9
    max_tokens: int = 1024


class JetstreamClient:
    def __init__(self, config: JetstreamConfig, timeout: int = 60, max_retries: int = 3):
        self.config = config
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()

    @classmethod
    def from_env(cls) -> "JetstreamClient":
        load_dotenv()
        config = JetstreamConfig(
            base_url=os.environ.get("JETSTREAM_API_BASE", "").rstrip("/"),
            api_key=os.environ.get("JETSTREAM_API_KEY") or None,
            model=os.environ.get("JETSTREAM_MODEL", "llama-4-scout"),
            temperature=float(os.environ.get("JETSTREAM_TEMPERATURE", 0.5)),
            top_p=float(os.environ.get("JETSTREAM_TOP_P", 0.9)),
            max_tokens=int(os.environ.get("JETSTREAM_MAX_TOKENS", 1024)),
        )
        if not config.base_url:
            raise ValueError("JETSTREAM_API_BASE is required")
        if not config.base_url.endswith("/chat/completions"):
            config.base_url = f"{config.base_url}/chat/completions"
        return cls(config)

    def generate_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self.config.temperature,
            "top_p": self.config.top_p,
            "max_tokens": self.config.max_tokens,
            "response_format": {"type": "json_object"},
        }
        raw_response = self._post(payload)
        content = raw_response["choices"][0]["message"]["content"]
        try:
            return json.loads(content)
        except json.JSONDecodeError as exc:
            LOGGER.error("Failed to decode Jetstream JSON: %s", exc)
            raise

    def _post(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json"}
        if self.config.api_key:
            headers["Authorization"] = f"Bearer {self.config.api_key}"
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.session.post(
                    self.config.base_url,
                    json=payload,
                    headers=headers,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response.json()
            except requests.RequestException as exc:
                LOGGER.warning("Jetstream request failed (attempt %s/%s): %s", attempt, self.max_retries, exc)
                if attempt == self.max_retries:
                    raise
                time.sleep(2**attempt)
        raise RuntimeError("Jetstream request failed after retries")
