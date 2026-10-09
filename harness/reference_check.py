"""Dataset self-test: validates reference solutions and checks statement leakage."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from harness.checker import judge_problem
from harness.dataset import Criterion, discover_criteria, discover_families, iter_problems


# Ground-truth (.out) generation is an offline, one-time, UNLIMITED-time cost; the
# per-problem `time_limit_s` applies only to models at evaluation, never to the
# reference. So when validating that the reference reproduces its cached .out we
# give it a generous ceiling (overridable via REFERENCE_CHECK_TIMEOUT_S), decoupled
# from the model time limit. This lets scaled NPC references (which may take many
# seconds) validate cleanly. Only the reference-validation path uses this; model
# evaluation in evaluate.py still uses the real time_limit_s.
_REFERENCE_TIMEOUT_S = float(os.environ.get("REFERENCE_CHECK_TIMEOUT_S", "3600"))


_FORBIDDEN_TERMS = re.compile(
    r"\b("
    r"NP-complete|NP-hard|NP complete|NP hard"
    r"|polynomial|P-time|bipartite"
    r"|2-SAT|3-SAT|k-SAT"
    r"|intractable|exponential"
    r"|reduction"
    r")\b",
    re.IGNORECASE,
)


def _leakage_check(criterion: Criterion) -> list[str]:
    problems = []
    if not criterion.statement_path.exists():
        problems.append(f"MISSING statement.md: {criterion.statement_path}")
        return problems
    text = criterion.statement_path.read_text()
    for m in _FORBIDDEN_TERMS.finditer(text):
        problems.append(
            f"LEAKAGE in {criterion.statement_path}: "
            f"found forbidden term {m.group()!r} at char {m.start()}"
        )
    return problems


def check_reference(criterion: Criterion) -> list[str]:
    """Run reference.py against all test cases and check the statement. Returns list of problems."""
    problems: list[str] = []

    problems.extend(_leakage_check(criterion))

    if not criterion.reference_path.exists():
        problems.append(f"MISSING reference.py: {criterion.reference_path}")
        return problems

    if not criterion.tests:
        problems.append(f"NO TEST CASES in {criterion.dir / 'tests'}")
        return problems

    for tc in criterion.tests:
        if not tc.out_path.exists():
            problems.append(f"MISSING .out for {tc.in_path}")

    # allow_expand=True: offline oracle validation may exceed the model deadline (audit B1).
    verdict = judge_problem(criterion, criterion.reference_path,
                            timeout_override=_REFERENCE_TIMEOUT_S, allow_expand=True)
    for cv in verdict.cases:
        if cv.verdict != "PASS":
            problems.append(
                f"reference FAIL on case {cv.name}: {cv.verdict}"
                + (f" — {cv.reason}" if cv.reason else "")
            )

    return problems


def _check_path(path: Path) -> int:
    """Check a single criterion dir, a family dir, or a whole dataset root. Returns exit code."""
    errors_total = 0

    # Dataset root: contains family_* subdirs -> check every family's every criterion.
    if any(path.glob("family_*")):
        criteria = list(iter_problems(path))
        label = f"dataset {path.name}"
    # Determine if path is a family or a criterion
    elif (path / "criterion_1_npc").exists() or any(path.glob("criterion_*")):
        criteria = discover_criteria(path)
        label = f"family {path.name}"
    elif (path / "meta.yaml").exists() or (path / "reference.py").exists():
        from harness.dataset import _load_meta
        meta = _load_meta(path / "meta.yaml") if (path / "meta.yaml").exists() else {}
        from harness.dataset import TestCase
        tests_dir = path / "tests"
        tests = []
        if tests_dir.exists():
            for in_path in sorted(tests_dir.glob("*.in")):
                tests.append(TestCase(name=in_path.stem, in_path=in_path,
                                      out_path=in_path.with_suffix(".out")))
        validator_path = path / "validator.py"
        c = Criterion(
            family_id=path.parent.name,
            criterion_id=path.name,
            dir=path,
            meta=meta,
            statement_path=path / "statement.md",
            reference_path=path / "reference.py",
            tests=tests,
            validator_path=validator_path if validator_path.exists() else None,
        )
        criteria = [c]
        label = f"criterion {path.name}"
    else:
        print(f"Cannot determine type of path: {path}", file=sys.stderr)
        return 1

    print(f"Checking {label} ({len(criteria)} criterion/a)...")
    for c in criteria:
        problems = check_reference(c)
        status = "OK" if not problems else "FAIL"
        print(f"  [{status}] {c.criterion_id}")
        for p in problems:
            print(f"         {p}")
            errors_total += 1

    if errors_total == 0:
        print("All checks passed.")
    else:
        print(f"{errors_total} problem(s) found.", file=sys.stderr)
    return 0 if errors_total == 0 else 1


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Validate reference solutions and check for statement leakage."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Path to the dataset root, a family directory "
             "(e.g. dataset/family_01_graph_coloring), or a single criterion directory. "
             "Defaults to the dataset/ directory (checks every family).",
    )
    args = parser.parse_args()
    path = Path(args.path) if args.path else (Path(__file__).parent.parent / "dataset")
    sys.exit(_check_path(path))


if __name__ == "__main__":
    main()
