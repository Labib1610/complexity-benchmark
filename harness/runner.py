"""Safely runs a Python solution against a single test-case input.

Audit B10: submitted code is hardened at the OS level -- it runs in an isolated temporary
working directory (so relative paths cannot reach the repo, answer keys, references, or
validators), with a scrubbed environment (no API keys / secrets), in its own process session
so the whole process group can be killed on timeout (no surviving descendants), with the RSS
limit still applied and captured output capped. This is defense-in-depth, not a full
sandbox: for untrusted models a container/VM with no answer-key mount is still the real fix.
"""

from __future__ import annotations

import os
import signal
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

OUTPUT_CAP_BYTES = 16 * 1024 * 1024   # cap stored stdout/stderr at 16 MB


@dataclass
class RunResult:
    status: str       # OK | TLE | RUNTIME_ERROR
    stdout: str = ""
    stderr: str = ""
    elapsed_s: float = 0.0


def _make_preexec(memory_limit_mb: int):
    """preexec_fn: cap address space (best effort). Session isolation is done via
    start_new_session=True so the whole group can be killed on timeout."""
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


def _scrubbed_env() -> dict:
    """Minimal environment: enough to run python, nothing sensitive (no *_API_KEY etc.)."""
    return {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "HOME": "/tmp",
        "PYTHONHASHSEED": "0",
        "LC_ALL": "C.UTF-8",
        "LANG": "C.UTF-8",
    }


def _kill_group(proc: subprocess.Popen) -> None:
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)   # kill child AND its descendants
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def run_solution(
    solution_path: Path | str,
    input_text: str,
    timeout_s: float,
    memory_limit_mb: int = 256,
) -> RunResult:
    solution_path = Path(solution_path).resolve()   # absolute, so cwd change can't lose it
    input_bytes = input_text.encode()
    preexec = _make_preexec(memory_limit_mb)
    start = time.monotonic()

    with tempfile.TemporaryDirectory(prefix="cb_run_") as workdir:
        try:
            proc = subprocess.Popen(
                ["python3", str(solution_path)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=workdir,                 # isolated: relative paths cannot reach the repo
                env=_scrubbed_env(),         # no secrets in the child's environment
                preexec_fn=preexec,          # RSS limit
                start_new_session=True,      # own process group -> killpg on timeout
            )
        except Exception as e:
            return RunResult(status="RUNTIME_ERROR", stderr=str(e),
                             elapsed_s=time.monotonic() - start)

        try:
            out, err = proc.communicate(input=input_bytes, timeout=timeout_s)
            elapsed = time.monotonic() - start
        except subprocess.TimeoutExpired:
            _kill_group(proc)
            try:
                proc.communicate(timeout=5)   # reap
            except Exception:
                pass
            return RunResult(status="TLE", stderr="timeout",
                             elapsed_s=time.monotonic() - start)
        except Exception as e:
            _kill_group(proc)
            return RunResult(status="RUNTIME_ERROR", stderr=str(e),
                             elapsed_s=time.monotonic() - start)

        out = (out or b"")[:OUTPUT_CAP_BYTES].decode(errors="replace")
        err = (err or b"")[:OUTPUT_CAP_BYTES].decode(errors="replace")
        status = "OK" if proc.returncode == 0 else "RUNTIME_ERROR"
        return RunResult(status=status, stdout=out, stderr=err, elapsed_s=elapsed)
