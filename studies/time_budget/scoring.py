"""Partial-credit scoring for the time-budget study.

For problems where exact pass/fail is insufficient, an optional
`objective.py` per criterion exposes `value(input_text, output_text) -> float`.
If no objective.py exists, scoring falls back to binary pass/fail (ratio 0 or 1).
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


def approx_ratio(produced_value: float, optimal_value: float, minimize: bool) -> float:
    """Return approximation ratio in [0, 1]; 1.0 == optimal.

    For minimization (e.g. bin-packing, TSP): ratio = optimal / produced.
    For maximization (e.g. knapsack value): ratio = produced / optimal.
    """
    if minimize:
        if produced_value <= 0:
            return 1.0 if optimal_value <= 0 else 0.0
        return min(1.0, optimal_value / produced_value)
    else:
        if optimal_value <= 0:
            return 1.0 if produced_value <= 0 else 0.0
        return min(1.0, produced_value / optimal_value)


def _load_objective(criterion):
    """Dynamically load criterion/objective.py if it exists, else return None."""
    obj_path = Path(criterion.dir) / "objective.py"
    if not obj_path.exists():
        return None
    spec = importlib.util.spec_from_file_location("_objective", obj_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def score_case(criterion, input_text: str, produced_output: str, optimal_output: str,
               run_result) -> dict:
    """Score one test case under the time-budget study.

    Audit B7: `input_text` is the actual test input (was previously a directory name), and
    `produced_output` is the program's real stdout (was previously a checker diagnostic).

    Returns a dict with keys:
      tle      : bool  — did the run exceed the time limit?
      exact    : bool  — did the output exactly match the expected output?
      ratio    : float — approximation quality in [0, 1]; 1.0 == optimal.
      strategy : str|None — stub for qualitative classification (filled later).
    """
    tle = run_result.status == "TLE"

    if tle:
        return {"tle": True, "exact": False, "ratio": 0.0, "strategy": None}

    if run_result.status != "OK":
        return {"tle": False, "exact": False, "ratio": 0.0, "strategy": None}

    # Exact match check (uses same normalisation as harness/checker.py)
    from harness.checker import normalize
    exact = normalize(produced_output) == normalize(optimal_output)

    if exact:
        return {"tle": False, "exact": True, "ratio": 1.0, "strategy": None}

    # Try objective-value partial credit
    objective_mod = _load_objective(criterion)
    if objective_mod is None:
        # No objective.py — binary: wrong answer earns 0
        return {"tle": False, "exact": False, "ratio": 0.0, "strategy": None}

    try:
        # objective.value(input_text, output_text) -> float, computed from the ACTUAL input.
        produced_val = objective_mod.value(input_text, produced_output)
        optimal_val = objective_mod.value(input_text, optimal_output)
        minimize = getattr(objective_mod, "MINIMIZE", True)
        ratio = approx_ratio(produced_val, optimal_val, minimize)
    except Exception:
        ratio = 0.0

    return {"tle": False, "exact": False, "ratio": ratio, "strategy": None}
