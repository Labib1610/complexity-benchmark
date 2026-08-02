#!/usr/bin/env python3
"""Automated gate for generated statement versions. Writes gate.json per version.

Checks (deterministic ones first, model check last):
  1. I/O contract unchanged  -- version's Input/Output sections match the seed.
  2. Reference still passes   -- seed reference.py passes the seed's small tests
                                 (confirms the harness path is intact).
  3. Leakage scan            -- reject forbidden complexity-class terms / hints.
  4. Verifier check          -- a separate model restates the task and judges whether
                                it is the same task, unambiguous, solvable, and its
                                examples are consistent (returns overall pass/flag/fail).

Result: PASS | FLAG (verifier unsure / could not verify -> human review)
        | FAIL (contract broken, leakage, or verifier fail).
Per run_config stop_on_gate_fail=false, failures are recorded, never deleted.

CLI: python tools/gate.py --family 01 [--criterion 1] [--version v003]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import backends as B

from harness.checker import judge_problem
from harness.dataset import discover_criteria
from harness.reference_check import _FORBIDDEN_TERMS

# forbidden terms the harness regex misses (file 42/43 list): structural reveals + hints
_EXTRA_FORBIDDEN = re.compile(
    r"\b(tree|DAG|acyclic|matching|clique|cover|knapsack|"
    r"brute[- ]force is fine|easy variant|hard variant|trivially)\b", re.IGNORECASE)


def _section(statement: str, header: str) -> str:
    lines = statement.splitlines()
    out, capture = [], False
    for ln in lines:
        s = ln.strip()
        if s.lower().startswith("## ") or (s.startswith("#") and s.lstrip("#").strip()):
            capture = s.lstrip("#").strip().lower().startswith(header.lower())
            continue
        if capture:
            out.append(ln.rstrip())
    return "\n".join(out).strip()


def seed_criterion(slug: str, crit_dir: str):
    for c in discover_criteria(B.SEEDS_DIR / slug):
        if c.criterion_id == crit_dir:
            return c
    return None


def leakage_hits(text: str) -> list[str]:
    hits = [m.group() for m in _FORBIDDEN_TERMS.finditer(text)]
    hits += [m.group() for m in _EXTRA_FORBIDDEN.finditer(text)]
    return sorted(set(h.lower() for h in hits))


def evaluate_statement(version_stmt: str, seed_stmt: str, seed_crit, verifier_cfg,
                       run_cfg, verifier_system: str, verifier_user_tmpl: str) -> dict:
    """Run all gate checks on a candidate statement (text) and return the result dict.
    Used both by gate_version (from a file) and by the feedback inner loop (in memory)."""
    # 1. Structural: the rewrite must still be a well-formed problem statement
    #    (Input + Output sections and at least one worked example). The teacher is
    #    explicitly allowed to REWORD Input/Output, so we do NOT require verbatim
    #    text -- semantic "same task / same contract" is judged by the verifier
    #    below. We keep a verbatim-diff flag purely as an informational signal.
    has_input = bool(_section(version_stmt, "Input"))
    has_output = bool(_section(version_stmt, "Output"))
    has_example = "```" in version_stmt or bool(_section(version_stmt, "Example"))
    structural_ok = has_input and has_output and has_example
    io_text_identical = {
        sect: " ".join(_section(seed_stmt, sect).split())
              == " ".join(_section(version_stmt, sect).split())
        for sect in ("Input", "Output")
    }

    # 2. Reference still passes the seed's small tests (harness path intact)
    reference_ok = judge_problem(seed_crit, seed_crit.reference_path).overall == "PASS"

    # 3. Leakage
    hits = leakage_hits(version_stmt)

    # 4. Verifier (model) -- the semantic authority on "same task / same contract"
    user = verifier_user_tmpl.replace("{SEED}", seed_stmt).replace("{CANDIDATE}", version_stmt)
    resp = B.chat(verifier_cfg, verifier_system, user,
                  timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=B.load_models().get("execution", {}).get("retries", 3))
    parsed = B.extract_json(resp["text"])
    v_overall = (parsed.get("overall") or "").lower() if parsed else ""
    same_task = (parsed.get("same_task") or "").lower() if parsed else ""
    verifier = {"called": True, "error": resp["error"], "raw": resp["text"],
                "parsed": parsed, "overall": v_overall}

    # decision (deterministic FAILs first, then the verifier's judgement)
    if hits or not structural_ok or not reference_ok:
        result = "FAIL"
    elif resp["error"] or not parsed:
        result = "FLAG"                      # could not verify -> human review
    elif v_overall == "fail" or same_task == "no":
        result = "FAIL"                      # verifier says not the same task
    elif v_overall == "pass" and same_task in ("yes", ""):
        result = "PASS"
    else:
        result = "FLAG"                      # verifier 'flag'/unsure -> human review

    return {
        "result": result,
        "structural_ok": structural_ok,
        "io_text_identical": io_text_identical,   # informational only
        "reference_passes": reference_ok,
        "leakage_hits": hits,
        "verifier": verifier,
    }


def gate_version(vdir: Path, seed_stmt: str, seed_crit, verifier_cfg, run_cfg,
                 verifier_system: str, verifier_user_tmpl: str) -> dict:
    res = evaluate_statement((vdir / "statement.md").read_text(), seed_stmt, seed_crit,
                             verifier_cfg, run_cfg, verifier_system, verifier_user_tmpl)
    return {"version": vdir.name, **res}


def iter_version_dirs(family, criterion, version):
    base = B.VERSIONS_DIR / f"family_{family}"
    crits = [B.criterion_dirname(criterion)] if criterion else \
        [d.name for d in sorted(base.glob("criterion_*"))]
    for cd in crits:
        cbase = base / cd
        if not cbase.exists():
            continue
        vers = [cbase / version] if version else sorted(cbase.glob("v*"))
        for v in vers:
            if (v / "statement.md").exists():
                yield cd, v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    ap.add_argument("--criterion", type=int, choices=[1, 2, 3])
    ap.add_argument("--version")
    args = ap.parse_args()

    models = B.load_models()
    run_cfg = B.load_run_config()
    verifier_cfg = models["verifier"]
    verifier_system = (B.PROMPTS_DIR / "verifier_system.md").read_text()
    verifier_user_tmpl = (B.PROMPTS_DIR / "verifier_user_template.md").read_text()

    total = {"PASS": 0, "FLAG": 0, "FAIL": 0}
    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        for crit_dir, vdir in iter_version_dirs(family, args.criterion, args.version):
            sc = seed_criterion(slug, crit_dir)
            if sc is None:
                print(f"ERROR: no seed criterion for {crit_dir}", file=sys.stderr)
                continue
            res = gate_version(vdir, sc.statement_path.read_text(), sc, verifier_cfg,
                               run_cfg, verifier_system, verifier_user_tmpl)
            (vdir / "gate.json").write_text(json.dumps(res, indent=2))
            total[res["result"]] += 1
            extra = f" leakage={res['leakage_hits']}" if res["leakage_hits"] else ""
            vov = res["verifier"].get("overall") or ("err" if res["verifier"]["error"] else "?")
            print(f"  [{res['result']}] family_{family}/{crit_dir}/{vdir.name} "
                  f"struct={res['structural_ok']} verifier={vov}{extra}")
    print(f"[gate] {total}")


if __name__ == "__main__":
    main()
