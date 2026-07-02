"""Multi-turn study driver skeleton.

Builds a running message history across turns, evaluates per-turn code against
the corresponding criterion, and records turn trajectories.

See studies/multiturn/driver_notes.md for the full design.
Full wiring of the 18 sequences × 2 conditions is done when the user runs the study.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).parent.parent


# ── message history helpers ────────────────────────────────────────────────────

def build_turn_messages(history: list[dict], new_user_content: str) -> list[dict]:
    """Append a user turn to the conversation history and return the new list."""
    return history + [{"role": "user", "content": new_user_content}]


def _lookup_criterion(family, class_label: str):
    """Return the Criterion matching class_label within a Family."""
    cls_map = {"NPC": "npc", "P": "p", "INFEASIBLE": "infeasible"}
    suffix = cls_map.get(class_label.upper(), class_label.lower())
    for criterion in family.criteria:
        if suffix in criterion.criterion_id:
            return criterion
    raise ValueError(
        f"No criterion matching class {class_label!r} in family {family.family_id}"
    )


def _write_temp_solution(code: str) -> Path:
    """Write code to a temp file and return its path."""
    tf = tempfile.NamedTemporaryFile(
        suffix=".py", prefix="multiturn_sol_", delete=False,
        mode="w", encoding="utf-8"
    )
    tf.write(code)
    tf.close()
    return Path(tf.name)


# ── per-sequence runner ────────────────────────────────────────────────────────

def run_sequence(
    sequence: list[str],
    family,
    condition: str,
    model: dict,
    run_dir: Path,
    timeout_s: float = 10.0,
) -> list[dict]:
    """Run one transition sequence for one family+model pair.

    Returns a list of per-turn result dicts:
      {turn: int, class_label: str, condition: str, verdict: str,
       n_passed: int, n_cases: int, elapsed_s: float}
    """
    from harness.backends import generate
    from harness.checker import judge_problem
    from harness.extract import extract_code, strip_thinking

    history: list[dict] = []
    trajectory: list[dict] = []

    system = (
        "You are an expert competitive programmer. You write correct, efficient Python 3\n"
        "solutions. Your program reads all input from standard input and writes only the\n"
        "required answer to standard output. Output only a single Python 3 code block and\n"
        "nothing else — no explanation before or after."
    )

    for turn_idx, class_label in enumerate(sequence):
        criterion = _lookup_criterion(family, class_label)

        if turn_idx == 0 or condition == "explicit":
            user_content = (
                f"Solve the following problem in Python 3.\n\n"
                f"{criterion.statement_path.read_text()}\n\n"
                "Requirements:\n"
                "- Read from standard input, write to standard output.\n"
                "- Output only the answer in the exact format specified.\n"
                "- Return only one Python 3 code block."
            )
        else:
            delta = criterion.meta.get("constraint_delta", "")
            user_content = (
                f"Now assume the following change to the problem: {delta}\n"
                "Keep solving in the same format and return only one Python 3 code block."
            )

        history = build_turn_messages(history, user_content)

        raw = generate(
            backend=model["backend"],
            model_string=model["model_string"],
            system=system,
            user="",           # history carries the full conversation
            max_tokens=model.get("token_budget", 4096),
            temperature=0.2,
            thinking=model.get("thinking", False),
        )

        # Append assistant reply to history
        history = history + [{"role": "assistant", "content": raw}]

        if model.get("thinking"):
            raw_stripped = strip_thinking(raw)
        else:
            raw_stripped = raw
        code = extract_code(raw_stripped)

        sol_path = _write_temp_solution(code)
        try:
            verdict = judge_problem(criterion, sol_path, timeout_override=timeout_s)
        finally:
            sol_path.unlink(missing_ok=True)

        trajectory.append({
            "turn": turn_idx + 1,
            "class_label": class_label,
            "condition": condition,
            "verdict": verdict.overall,
            "n_passed": sum(1 for c in verdict.cases if c.verdict == "PASS"),
            "n_cases": len(verdict.cases),
        })

    return trajectory


# ── top-level entry point ──────────────────────────────────────────────────────

def run(config: dict, run_dir: Path, dataset_dir: Path) -> None:
    """Entry point called by evaluate.py when study == multiturn.

    Full enumeration of sequences × conditions is wired here once the user
    is ready. Currently raises NotImplementedError as a clear placeholder.
    """
    sequences_path = ROOT / "studies" / "multiturn" / "sequences.yaml"
    sequences_cfg = yaml.safe_load(sequences_path.read_text())

    from harness.dataset import discover_families
    families = discover_families(dataset_dir)
    ready = [f for f in families if any(
        c.reference_path.exists()
        and "NotImplementedError" not in c.reference_path.read_text()
        for c in f.criteria
    )]

    print(
        f"[multiturn] {len(ready)} families ready, "
        f"{sum(len(v) for v in sequences_cfg.values() if isinstance(v, list))} sequences defined.",
        file=sys.stderr,
    )
    raise NotImplementedError(
        "Multi-turn driver is scaffolded but not yet fully wired. "
        "See studies/multiturn/driver_notes.md to complete the implementation."
    )
