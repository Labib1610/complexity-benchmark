"""Checker — maps run results to verdicts per conventions/checker_spec.md."""

from __future__ import annotations

import importlib.util
from dataclasses import dataclass, field
from pathlib import Path

from harness.dataset import Criterion, TestCase
from harness.runner import RunResult, run_solution


@dataclass
class CaseVerdict:
    name: str
    verdict: str          # PASS | WRONG_ANSWER | TLE | RUNTIME_ERROR | MLE
    elapsed_s: float = 0.0
    reason: str = ""


@dataclass
class ProblemVerdict:
    family_id: str
    criterion_id: str
    class_label: str
    overall: str          # PASS | WRONG_ANSWER | TLE | RUNTIME_ERROR | MLE
    cases: list[CaseVerdict] = field(default_factory=list)
    first_failure: str | None = None


def normalize(s: str) -> str:
    lines = [line.rstrip() for line in s.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def judge_exact(produced: str, expected: str) -> bool:
    return normalize(produced) == normalize(expected)


def judge_custom(validator_path: Path, input_text: str, produced: str) -> tuple[bool, str]:
    spec = importlib.util.spec_from_file_location("_validator", validator_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.validate(input_text, produced)


def judge_case(
    criterion: Criterion,
    test_case: TestCase,
    run_result: RunResult,
) -> CaseVerdict:
    if run_result.status == "TLE":
        return CaseVerdict(name=test_case.name, verdict="TLE",
                           elapsed_s=run_result.elapsed_s)
    if run_result.status == "RUNTIME_ERROR":
        return CaseVerdict(name=test_case.name, verdict="RUNTIME_ERROR",
                           elapsed_s=run_result.elapsed_s,
                           reason=run_result.stderr[:300])

    judge_mode = criterion.meta.get("judge", "exact")
    produced = run_result.stdout

    if judge_mode == "exact":
        expected = test_case.out_path.read_text() if test_case.out_path.exists() else ""
        ok = judge_exact(produced, expected)
        verdict = "PASS" if ok else "WRONG_ANSWER"
        reason = "" if ok else f"expected: {normalize(expected)!r} got: {normalize(produced)!r}"
        return CaseVerdict(name=test_case.name, verdict=verdict,
                           elapsed_s=run_result.elapsed_s, reason=reason)

    if judge_mode == "custom":
        if criterion.validator_path is None:
            return CaseVerdict(name=test_case.name, verdict="RUNTIME_ERROR",
                               reason="judge=custom but no validator.py found")
        input_text = test_case.in_path.read_text()
        ok, reason = judge_custom(criterion.validator_path, input_text, produced)
        return CaseVerdict(name=test_case.name,
                           verdict="PASS" if ok else "WRONG_ANSWER",
                           elapsed_s=run_result.elapsed_s, reason=reason)

    return CaseVerdict(name=test_case.name, verdict="RUNTIME_ERROR",
                       reason=f"unknown judge mode: {judge_mode!r}")


def judge_problem(
    criterion: Criterion,
    solution_path: Path | str,
    timeout_override: float | None = None,
) -> ProblemVerdict:
    timeout = timeout_override if timeout_override is not None \
        else criterion.meta.get("time_limit_s", 10)
    memory_limit_mb = criterion.meta.get("memory_limit_mb", 256)
    class_label = criterion.meta.get("class", "UNKNOWN")

    case_verdicts: list[CaseVerdict] = []
    first_failure: str | None = None
    overall = "PASS"

    for tc in criterion.tests:
        input_text = tc.in_path.read_text()
        run_result = run_solution(solution_path, input_text, timeout, memory_limit_mb)
        cv = judge_case(criterion, tc, run_result)
        case_verdicts.append(cv)
        if cv.verdict != "PASS" and first_failure is None:
            first_failure = tc.name
            overall = cv.verdict

    if not criterion.tests:
        overall = "RUNTIME_ERROR"
        first_failure = "no_test_cases"

    return ProblemVerdict(
        family_id=criterion.family_id,
        criterion_id=criterion.criterion_id,
        class_label=class_label,
        overall=overall,
        cases=case_verdicts,
        first_failure=first_failure,
    )
