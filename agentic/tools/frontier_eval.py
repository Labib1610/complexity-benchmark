#!/usr/bin/env python3
"""Frontier evaluation of final statements (file 51).

Independently assess whether the hardened statements are well-formed and hard, using two
strong models that were NOT in the student panel. By default we evaluate only the FINAL
(hardest) statement of each lineage -- d<final_depth> -- i.e. one problem per lineage
(42 lineages -> 42 problems x 2 evaluators = 84 calls). Pass --depths seed,final to also
evaluate the d000 baseline.

Key method: TLE is NOT a verdict, and there is NO time cap on measurement. Each solution
runs to completion and we record its full wall-clock time per case -- a frontier solution
may take as long as it needs; the elapsed time IS the difficulty signal. A large runaway
guard (--ceiling, default 3600 s; 0 = unbounded) only exists to kill genuine infinite
loops, not to cut off legitimately-slow-but-finishing solutions.

  python tools/frontier_eval.py --family 01 [--models gpt-5.6-sol gemini-3.7-flash-frontier]
                                [--depths final] [--ceiling 3600] [--only-lineage L001] [--reset]

Guardrails (file 51): reads lineages/ + seeds/ read-only; writes only frontier_eval/ and
reports/frontier_eval_meta.json; never reuses the teacher as an evaluator.
"""
import argparse
import dataclasses
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import backends as B
import gate as GT

from harness.checker import normalize, judge_custom
from harness.dataset import TestCase
from harness.runner import run_solution

LINEAGES_DIR = B.AGENTIC / "lineages"
FRONTIER_DIR = B.AGENTIC / "frontier_eval"
SCALED_DIRNAME = "tests_scaled"
DEFAULT_CEILING_S = 3600   # runaway guard only (kills infinite loops); NOT a time limit.
                           # 0 = unbounded. The real signal is the recorded elapsed_s.
_TIERS = ("anchor", "corner", "scaled")


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _tests_from_dir(d: Path):
    out = []
    if d and d.exists():
        for inp in sorted(d.glob("*.in")):
            outp = inp.with_suffix(".out")
            if outp.exists():
                out.append(TestCase(name=inp.stem, in_path=inp, out_path=outp))
    return out


def build_tiers(family, slug, crit_dir, sc):
    return {"anchor": list(sc.tests),
            "corner": _tests_from_dir(B.TESTS_DIR / f"family_{family}" / crit_dir),
            "scaled": _tests_from_dir(B.SEEDS_DIR / slug / crit_dir / SCALED_DIRNAME)}


# --- evaluator resolution + contamination guard -----------------------------
def resolve_evaluators(models: dict, run_cfg: dict, only_ids):
    evals = models.get("frontier_evaluators", []) or []
    if only_ids:
        evals = [e for e in evals if e["id"] in only_ids]
    if not evals:
        raise SystemExit("no frontier_evaluators resolved (check models.yaml / --models)")

    # forbidden roles: teacher, verifier, students, held-out, H5 solver
    forbidden_ids, forbidden_strings = set(), set()
    for key in ("teacher", "verifier"):
        m = models.get(key, {})
        forbidden_ids.add(m.get("id")); forbidden_strings.add(m.get("model_string"))
    for grp in ("students", "held_out"):
        for m in models.get(grp, []) or []:
            forbidden_ids.add(m.get("id")); forbidden_strings.add(m.get("model_string"))
    sr = (run_cfg.get("gate", {}) or {}).get("solver_roundtrip", {}) or {}
    forbidden_ids.add(sr.get("model_id")); forbidden_strings.add(sr.get("model_string"))

    for e in evals:
        if e["id"] in forbidden_ids or e["model_string"] in forbidden_strings:
            raise SystemExit(f"evaluator {e['id']} ({e['model_string']}) is used in another "
                             f"role (teacher/verifier/student/held-out/solver) -- not independent")
    return evals


# --- per-case execution: timing, not TLE ------------------------------------
def run_case(criterion, tc, solution_path, ceiling) -> dict:
    input_text = tc.in_path.read_text()
    mem = int(criterion.meta.get("memory_limit_mb", 256))
    # ceiling 0 -> no timeout (run to completion, however long); else runaway guard only.
    rr = run_solution(solution_path, input_text, (ceiling or None), mem)
    if rr.status == "TLE":     # only fires if a ceiling was set and hit -> runaway loop
        return {"name": tc.name, "verdict": "EXCEEDED_CEILING", "elapsed_s": round(rr.elapsed_s, 3)}
    if rr.status == "RUNTIME_ERROR":
        return {"name": tc.name, "verdict": "RUNTIME_ERROR", "elapsed_s": round(rr.elapsed_s, 3),
                "reason": (rr.stderr or "")[:200]}
    mode = criterion.meta.get("judge", "exact")
    if mode == "custom" and criterion.validator_path is not None:
        ok, _ = judge_custom(criterion.validator_path, input_text, rr.stdout)
    else:
        expected = tc.out_path.read_text() if tc.out_path.exists() else ""
        ok = normalize(rr.stdout) == normalize(expected)
    return {"name": tc.name, "verdict": "PASS" if ok else "WRONG_ANSWER",
            "elapsed_s": round(rr.elapsed_s, 3)}


def eval_statement(stmt_text, model_cfg, sc, tiers, sys_tmpl, user_tmpl,
                   run_cfg, exec_cfg, out_dir, header, ceiling) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    resp = B.chat(model_cfg, sys_tmpl, user_tmpl.replace("{STATEMENT}", stmt_text),
                  timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
    (out_dir / "raw.txt").write_text(resp["text"] or "")
    code = B.extract_code(B.strip_thinking(resp["text"]))
    (out_dir / "solution.py").write_text(code)

    tiers_out, max_e, tot_e, solved_all = {}, 0.0, 0.0, True
    if resp["error"] or not code.strip():
        for t in _TIERS:
            tiers_out[t] = None
        solved_all = False
    else:
        sol = out_dir / "solution.py"
        for t in _TIERS:
            tests = tiers.get(t)
            if not tests:
                tiers_out[t] = None
                continue
            crit = dataclasses.replace(sc, tests=tests)
            cases = [run_case(crit, tc, sol, ceiling) for tc in tests]
            passed = sum(1 for c in cases if c["verdict"] == "PASS")
            tiers_out[t] = {"passed": passed, "total": len(cases), "cases": cases}
            if passed < len(cases):
                solved_all = False
            for c in cases:
                max_e = max(max_e, c["elapsed_s"]); tot_e += c["elapsed_s"]

    result = {**header, "model": model_cfg["id"],
              "gen_elapsed_s": resp["elapsed_s"], "gen_error": resp["error"],
              **B.usage_of(resp), "tiers": tiers_out,
              "solved_all": solved_all, "max_elapsed_s": round(max_e, 3),
              "total_elapsed_s": round(tot_e, 3),
              "timestamp": datetime.now(timezone.utc).isoformat()}
    (out_dir / "result.json").write_text(json.dumps(result, indent=2))
    return result


def iter_criteria(family):
    base = LINEAGES_DIR / f"family_{family}"
    for cd in sorted(d.name for d in base.glob("criterion_*")) if base.exists() else []:
        yield cd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--models", nargs="+", help="evaluator ids (default: all frontier_evaluators)")
    ap.add_argument("--depths", default="final",
                    help="'final' (default: hardest statement only) or 'seed,final'")
    ap.add_argument("--ceiling", type=int, default=DEFAULT_CEILING_S,
                    help="runaway guard in seconds (0 = unbounded; NOT a time limit)")
    ap.add_argument("--only-lineage")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    models = B.load_models()
    run_cfg = B.load_run_config()
    exec_cfg = models.get("execution", {})
    evaluators = resolve_evaluators(models, run_cfg, args.models)
    depths = [d.strip() for d in args.depths.split(",") if d.strip()]

    sys_tmpl = (B.PROMPTS_DIR / "student_system.md").read_text()
    user_tmpl = (B.PROMPTS_DIR / "student_user_template.md").read_text()

    # record exact strings + dates (guardrail)
    B.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (B.REPORTS_DIR / "frontier_eval_meta.json").write_text(json.dumps({
        "family": args.family, "generated_at": datetime.now(timezone.utc).isoformat(),
        "ceiling_s": args.ceiling, "ceiling_note": "runaway guard only; 0 = unbounded",
        "tiers": list(_TIERS), "depths": depths,
        "evaluators": [{"id": e["id"], "model_string": e["model_string"],
                        "base_url": e.get("base_url")} for e in evaluators],
        "note": "TLE ignored; run to completion under the ceiling; time recorded per case."},
        indent=2))
    print(f"[frontier] evaluators={[e['id'] for e in evaluators]} depths={depths}")

    for crit_dir in iter_criteria(args.family):
        slug = B.family_slug(args.family)
        sc = GT.seed_criterion(slug, crit_dir)
        if sc is None:
            continue
        tiers = build_tiers(args.family, slug, crit_dir, sc)
        lbase = LINEAGES_DIR / f"family_{args.family}" / crit_dir
        for ldir in sorted(lbase.glob("L*")):
            if args.only_lineage and ldir.name != args.only_lineage:
                continue
            lj = _read_json(ldir / "lineage.json")
            if not lj:
                continue
            fd = lj.get("final_depth", 0)
            which_depth = {"seed": 0, "final": fd}
            for which in depths:
                depth = which_depth.get(which)
                if depth is None:
                    continue
                stmt_path = ldir / f"d{depth:03d}" / "statement.md"
                if not stmt_path.exists():
                    continue
                header = {"lineage": ldir.name, "criterion": crit_dir,
                          "which": which, "depth": depth}
                stmt = stmt_path.read_text()
                for e in evaluators:
                    out_dir = FRONTIER_DIR / f"family_{args.family}" / crit_dir / ldir.name / which / e["id"]
                    res_path = out_dir / "result.json"
                    # dedupe: if final == seed (final_depth 0) reuse the seed result
                    if which == "final" and fd == 0:
                        seed_res = (FRONTIER_DIR / f"family_{args.family}" / crit_dir /
                                    ldir.name / "seed" / e["id"])
                        if (seed_res / "result.json").exists() and not args.reset:
                            out_dir.mkdir(parents=True, exist_ok=True)
                            for f in ("result.json", "solution.py", "raw.txt"):
                                if (seed_res / f).exists():
                                    shutil.copy2(seed_res / f, out_dir / f)
                            print(f"  [copy seed=final] {crit_dir}/{ldir.name}/{e['id']}")
                            continue
                    if res_path.exists() and not args.reset:
                        print(f"  [skip] {crit_dir}/{ldir.name}/{which}/{e['id']}")
                        continue
                    r = eval_statement(stmt, e, sc, tiers, sys_tmpl, user_tmpl,
                                       run_cfg, exec_cfg, out_dir, header, args.ceiling)
                    print(f"  [{crit_dir}/{ldir.name}/{which}/{e['id']}] solved_all={r['solved_all']} "
                          f"max={r['max_elapsed_s']}s gen={r['gen_elapsed_s']}s cost=${r.get('cost')}")
    print("[frontier] done.")


if __name__ == "__main__":
    main()
