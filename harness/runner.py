"""Safely runs a Python solution against a single test-case input."""

from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class RunResult:
    status: str       # OK | TLE | RUNTIME_ERROR
    stdout: str = ""
    stderr: str = ""
    elapsed_s: float = 0.0


def _make_preexec(memory_limit_mb: int):
    """Return a preexec_fn that sets RSS limit; no-op if resource unavailable."""
    try:
        import resource
        limit_bytes = memory_limit_mb * 1024 * 1024

        def preexec():
            try:
                resource.setrlimit(resource.RLIMIT_AS, (limit_bytes, limit_bytes))
            except Exception:
                pass

        return preexec
    except ImportError:
        return None


def run_solution(
    solution_path: Path | str,
    input_text: str,
    timeout_s: float,
    memory_limit_mb: int = 256,
) -> RunResult:
    solution_path = Path(solution_path)
    input_bytes = input_text.encode()
    preexec = _make_preexec(memory_limit_mb)

    start = time.monotonic()
    try:
        proc = subprocess.run(
            ["python3", str(solution_path)],
            input=input_bytes,
            capture_output=True,
            timeout=timeout_s,
            preexec_fn=preexec,
        )
        elapsed = time.monotonic() - start

        if proc.returncode != 0:
            return RunResult(
                status="RUNTIME_ERROR",
                stdout=proc.stdout.decode(errors="replace"),
                stderr=proc.stderr.decode(errors="replace"),
                elapsed_s=elapsed,
            )
        return RunResult(
            status="OK",
            stdout=proc.stdout.decode(errors="replace"),
            stderr=proc.stderr.decode(errors="replace"),
            elapsed_s=elapsed,
        )
    except subprocess.TimeoutExpired as e:
        elapsed = time.monotonic() - start
        return RunResult(
            status="TLE",
            stderr=str(e),
            elapsed_s=elapsed,
        )
    except Exception as e:
        elapsed = time.monotonic() - start
        return RunResult(
            status="RUNTIME_ERROR",
            stderr=str(e),
            elapsed_s=elapsed,
        )
