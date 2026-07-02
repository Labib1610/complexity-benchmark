"""Code extraction and thinking-strip for model responses."""

from __future__ import annotations

import re


_THINK_PATTERNS = [
    re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE),
    re.compile(r"<thinking>.*?</thinking>", re.DOTALL | re.IGNORECASE),
    re.compile(r"```reasoning\s.*?```", re.DOTALL | re.IGNORECASE),
]

_PYTHON_FENCE = re.compile(r"```python\s(.*?)```", re.DOTALL)
_ANY_FENCE = re.compile(r"```(?:\w+)?\s(.*?)```", re.DOTALL)


def strip_thinking(text: str) -> str:
    for pattern in _THINK_PATTERNS:
        text = pattern.sub("", text)
    return text


def extract_code(text: str) -> str:
    text = strip_thinking(text)

    m = _PYTHON_FENCE.search(text)
    if m:
        return m.group(1).strip()

    m = _ANY_FENCE.search(text)
    if m:
        return m.group(1).strip()

    return text.strip()
