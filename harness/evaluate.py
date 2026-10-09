"""Phase-3 driver: evaluate generated solutions against test cases.

Usage:
  python -m harness.evaluate --config runs/<date>_<name>/run_config.yaml [options]

Options:
  --reset   Ignore existing verdict checkpoints and re-evaluate.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent


def _atomic_write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.parent / f".tmp_{path.name}"
    try:
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp.rename(path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def _resolve_problems(dataset_dir: Path, families_filter, criteria_filter):
    from harness.dataset import iter_problems
    problems = list(iter_problems(dataset_dir))

    if families_filter != "all":
        allowed = {str(f).zfill(2) for f in families_filter}
        problems = [p for p in problems if p.meta.get("family", "") in allowed]

    if criteria_filter != "all":
        allowed = {int(c) for c in criteria_filter}
        problems = [p for p in problems if p.meta.get("criterion") in allowed]

    return problems


def _gen_dir(run_dir: Path, model_id: str, criterion, tok_level=None) -> Path:
    base = run_dir / "generations" / model_id
    if tok_level is not None:
        base = base / f"__tok{tok_level}"
    return base / criterion.family_id / criterion.criterion_id


def _verdict_path(run_dir: Path, model_id: str, criterion, tok_level=None) -> Path:
    base = run_dir / "results" / "raw" / model_id
    if tok_level is not None:
        base = base / f"__tok{tok_level}"
    return base / criterion.family_id / criterion.criterion_id / "verdict.json"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Phase-3: evaluate generated solutions")
    parser.add_argument("--config", required=True, help="Path to run_config.yaml")
    parser.add_argument("--reset", action="store_true", help="Ignore existing verdicts")
    args = parser.parse_args(argv)

    run_dir = Path(args.config).parent
    config = yaml.safe_load(Path(args.config).read_text())
    dataset_dir = ROOT / "dataset"
    study = config.get("study", "main")

    # ── multi-turn: fully delegated ────────────────────────────────────────────
    if study == "multiturn":
        from harness.multiturn import run as multiturn_run
        multiturn_run(config, run_dir, dataset_dir)
        return

    global_timeout = config.get("evaluation", {}).get("global_timeout_s", None)

    # ── time-budget: strict per-run limit + partial scoring ───────────────────
    if study == "time_budget":
        timeout_override = config.get("time_budget", {}).get("runtime_limit_s", 2)
        import importlib.util as _ilu
        _sp = ROOT / "studies" / "time_budget" / "scoring.py"
        _spec = _ilu.spec_from_file_location("tb_scoring", _sp)
        _scoring_mod = _ilu.module_from_spec(_spec)
        _spec.loader.exec_module(_scoring_mod)
        score_case_fn = _scoring_mod.score_case
    else:
        timeout_override = global_timeout
        score_case_fn = None

    # ── token-budget: iterate over levels ─────────────────────────────────────
    if study == "token_budget":
        tok_levels = config.get("token_budget", {}).get("levels", [4096])
    else:
        tok_levels = [None]

    problems = _resolve_problems(
        dataset_dir,
        config.get("families", "all"),
        config.get("criteria", "all"),
    )

    # Only evaluate problems that have real references (skip placeholders)
    ready = [p for p in problems
             if p.reference_path.exists()
             and "NotImplementedError" not in p.reference_path.read_text()]

    # Collect model ids present in the generations folder
    gen_root = run_dir / "generations"
    if not gen_root.exists():
        print("[evaluate] No generations folder found. Run generate first.", file=sys.stderr)
        sys.exit(1)

    model_ids = sorted(d.name for d in gen_root.iterdir() if d.is_dir())
    model_ids_cfg = config.get("models", model_ids)
    model_ids = [m for m in model_ids_cfg if (gen_root / m).exists()]

    from harness.checker import judge_problem

    print(f"[evaluate] run={run_dir.name}  study={study}  models={len(model_ids)}"
          f"  problems={len(ready)}"
          + (f"  tok_levels={tok_levels}" if study == "token_budget" else ""))

    total = passed = 0

    for tok_level in tok_levels:
        for model_id in model_ids:
            for criterion in ready:
                solution_path = _gen_dir(run_dir, model_id, criterion, tok_level) / "solution.py"
                if not solution_path.exists():
                    continue

                vpath = _verdict_path(run_dir, model_id, criterion, tok_level)
                if vpath.exists() and not args.reset:
                    level_tag = f"[tok={tok_level}] " if tok_level else ""
                    print(f"  [skip] {level_tag}{model_id}/{criterion.family_id}/{criterion.criterion_id}")
                    total += 1
                    with open(vpath) as f:
                        v = json.load(f)
                    if v.get("overall") == "PASS":
                        passed += 1
                    continue

                verdict = judge_problem(criterion, solution_path,
                                        timeout_override=timeout_override)

                # Audit B1: a PASS whose slowest case exceeds the effective limit is invalid.
                over = [round(c.elapsed_s, 3) for c in verdict.cases
                        if c.verdict == "PASS" and c.elapsed_s > verdict.effective_limit_s + 1e-6]
                if verdict.overall == "PASS" and over:
                    print(f"  [WARN] {model_id}/{criterion.family_id}/{criterion.criterion_id}: "
                          f"PASS with case(s) over the {verdict.effective_limit_s}s limit: {over}",
                          file=sys.stderr)

                record = {
                    "model": model_id,
                    "family_id": criterion.family_id,
                    "family_name": criterion.meta.get("family_name", ""),
                    "criterion_id": criterion.criterion_id,
                    "class_label": verdict.class_label,
                    "overall": verdict.overall,
                    "first_failure": verdict.first_failure,
                    "declared_limit_s": verdict.declared_limit_s,   # audit B1
                    "effective_limit_s": verdict.effective_limit_s,  # never > declared
                    "n_cases": len(verdict.cases),
                    "n_passed": sum(1 for c in verdict.cases if c.verdict == "PASS"),
                    "cases": [
                        {"name": c.name, "verdict": c.verdict,
                         "elapsed_s": round(c.elapsed_s, 3), "reason": c.reason}
                        for c in verdict.cases
                    ],
                }

                # time_budget: add per-case partial scores
                if score_case_fn is not None:
                    for i, cv in enumerate(verdict.cases):
                        if i < len(criterion.tests):
                            tc = criterion.tests[i]
                            expected = tc.out_path.read_text() if tc.out_path.exists() else ""
                            input_text = tc.in_path.read_text() if tc.in_path.exists() else ""
                            from harness.runner import RunResult
                            # audit B7: score against the REAL input + REAL stdout, not the
                            # checker diagnostic string.
                            rr = RunResult(status=cv.verdict if cv.verdict in ("TLE", "RUNTIME_ERROR") else "OK",
                                           stdout=cv.stdout, elapsed_s=cv.elapsed_s)
                            score = score_case_fn(criterion, input_text, cv.stdout, expected, rr)
                            record["cases"][i]["score"] = score

                # token_budget: record the level
                if tok_level is not None:
                    record["token_level"] = tok_level

                _atomic_write_json(vpath, record)
                total += 1
                if verdict.overall == "PASS":
                    passed += 1

                level_tag = f"[tok={tok_level}] " if tok_level else ""
                status = "PASS" if verdict.overall == "PASS" else f"FAIL({verdict.overall})"
                print(f"  [{status}] {level_tag}{model_id}/{criterion.family_id}/{criterion.criterion_id}")

    print(f"[evaluate] {passed}/{total} problems passed.")

    # Aggregate
    results_dir = run_dir / "results"
    from harness.aggregate import aggregate
    aggregate(results_dir / "raw", results_dir / "summary.csv")


if __name__ == "__main__":
    main()
