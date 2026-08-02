#!/usr/bin/env python3
"""Feedback-driven hardening LOOP (files 46 + 47). Each base version becomes a LINEAGE
hardened iteratively against live student behaviour until every student fails.

Per base version:
    depth 0 = base
    loop:
        run ALL students on the current statement (retired ones re-run to confirm defeat)
        active passers = still-active students that passed
        if none -> all_defeated
        summarize the single shared shortcut the passers used (verifier); it flags whether
            the affordance is mutable and whether it is a structural floor
        edit via a FALLBACK LADDER (S12_primary -> S12_secondary -> S07 -> S02_aggressive),
            each gate-validated; every teacher attempt + gate result is persisted
        failed active students are RETIRED (still re-tested, no longer steer the teacher)
        depth += 1

Fully instrumented: logs/harden_loop.log + per-attempt teacher_attempt_*.txt/.json +
gate.json on every attempt + stop_reason/stop_detail in lineage.json.

CLI: python tools/harden_loop.py --family 01 [--criterion 1] [--resume] [--reset]
        [--max-depth N] [--only-lineage L003]
"""
import argparse
import csv
import dataclasses
import json
import random
import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import backends as B
import generate_versions as GV
import gate as GT

from harness.checker import judge_problem
from harness.dataset import discover_criteria, TestCase

LINEAGES_DIR = B.AGENTIC / "lineages"
_THINK = re.compile(r"<think(?:ing)?>(.*?)</think(?:ing)?>", re.DOTALL | re.IGNORECASE)


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _log(lineage, depth, step, status, detail=""):
    B.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(B.LOGS_DIR / "harden_loop.log", "a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()} | {lineage} | d{depth} | "
                f"{step} | {status} | {detail}\n")


# --- three scoring tiers (file 48) ------------------------------------------
# anchor = seed cases 01-04 (basic correctness); corner = gen_tests universal
# store (edge cases); scaled = Phase-2 cases 05+ (intractability). They are
# scored SEPARATELY and never merged -- each measures a different thing.
SCALED_DIRNAME = "tests_scaled"
_TIERS = ("anchor", "corner", "scaled")


def _tests_from_dir(d: Path):
    out = []
    if d and d.exists():
        for inp in sorted(d.glob("*.in")):
            outp = inp.with_suffix(".out")
            if outp.exists():
                out.append(TestCase(name=inp.stem, in_path=inp, out_path=outp))
    return out


def build_scoring(family, slug, crit_dir):
    """Return (seed_criterion, tiers) where seed_criterion holds ONLY anchor tests
    (so the gate's reference check stays small) and tiers maps each tier name to
    its TestCase list, or None when that tier does not exist for this criterion."""
    sc = GT.seed_criterion(slug, crit_dir)   # anchor cases 01-04 already loaded
    if sc is None:
        return None, None
    anchor = list(sc.tests)
    corner = _tests_from_dir(B.TESTS_DIR / f"family_{family}" / crit_dir)
    scaled = _tests_from_dir(B.SEEDS_DIR / slug / crit_dir / SCALED_DIRNAME)
    tiers = {"anchor": anchor or None, "corner": corner or None, "scaled": scaled or None}
    return sc, tiers


def _tier_result(sc, tests, solution_path, want_timing=False):
    if not tests:
        return None
    crit = dataclasses.replace(sc, tests=tests)
    pv = judge_problem(crit, solution_path)
    cases = [{"name": c.name, "verdict": c.verdict, "elapsed_s": round(c.elapsed_s, 3)}
             for c in pv.cases]
    passed = sum(1 for c in pv.cases if c.verdict == "PASS")
    res = {"passed": passed, "total": len(pv.cases),
           "verdict_type": "PASS" if passed == len(pv.cases) else pv.overall,
           "verdicts": cases,
           "first_tle": next((c.name for c in pv.cases if c.verdict == "TLE"), None)}
    if want_timing:
        res["time_limit_s"] = sc.meta.get("time_limit_s", 10)
    return res


def score_tiers(sc, tiers, solution_path):
    return {t: _tier_result(sc, tiers.get(t), solution_path, want_timing=(t == "scaled"))
            for t in _TIERS}


def _tier_pass(tr):
    return bool(tr) and tr["total"] > 0 and tr["passed"] == tr["total"]


def overall_all_tiers(results):
    """Worst outcome across all tiers, in anchor->corner->scaled order (report only)."""
    for t in _TIERS:
        r = results.get(t)
        if r and r["verdict_type"] != "PASS":
            return r["verdict_type"]
    return "PASS"


def driving_verdict(results, scoring_tier):
    """The single PASS/fail-type that steers retirement, per config scoring_tier."""
    if scoring_tier == "anchor+corner":
        sel = ["anchor", "corner"]
    elif scoring_tier == "scaled":
        sel = ["scaled"] if results.get("scaled") else ["anchor", "corner"]
    else:                                        # all
        sel = [t for t in _TIERS if results.get(t)]
    sel = [t for t in sel if results.get(t)] or ["anchor"]
    if all(_tier_pass(results.get(t)) for t in sel):
        return "PASS"
    for t in sel:
        r = results.get(t)
        if r and r["verdict_type"] != "PASS":
            return r["verdict_type"]
    return "WRONG_ANSWER"


def run_student(student, statement, sc, tiers, scoring_tier, sys_tmpl, user_tmpl,
                run_cfg, exec_cfg, out_dir, reset):
    """Solve, then score against all three tiers separately. Returns the full
    verdict dict; the loop reads verdict['driving'] for PASS/retirement."""
    out_dir.mkdir(parents=True, exist_ok=True)
    vp = out_dir / "verdict.json"
    if vp.exists() and not reset:
        cached = _read_json(vp)
        if "tier_results" in cached:             # skip stale pre-file-48 verdicts
            return cached
    resp = B.chat(student, sys_tmpl, user_tmpl.replace("{STATEMENT}", statement),
                  timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
    raw = resp["text"]
    (out_dir / "raw.txt").write_text(raw)
    (out_dir / "trace.txt").write_text("\n\n".join(m.group(1).strip() for m in _THINK.finditer(raw)))
    code = B.extract_code(raw)
    (out_dir / "solution.py").write_text(code)
    if resp["error"] or not code.strip():
        results = {t: None for t in _TIERS}
        verdict = {"tier_results": results, "overall_all_tiers": "RUNTIME_ERROR",
                   "driving": "RUNTIME_ERROR",
                   "error": resp["error"] or "empty solution", "elapsed_s": resp["elapsed_s"]}
    else:
        results = score_tiers(sc, tiers, out_dir / "solution.py")
        verdict = {"tier_results": results,
                   "overall_all_tiers": overall_all_tiers(results),
                   "driving": driving_verdict(results, scoring_tier),
                   "error": resp["error"], "elapsed_s": resp["elapsed_s"]}
    (out_dir / "verdict.json").write_text(json.dumps(verdict, indent=2))
    return verdict


# --- shortcut summarizer ----------------------------------------------------
def summarize_shortcut(verifier, statement, passer_rows, sys_prompt, run_cfg, exec_cfg):
    parts = [f"PROBLEM STATEMENT:\n{statement}\n"]
    for r in passer_rows:
        parts.append(f"--- model {r['student']} SOLVED it ---")
        if r["trace"].strip():
            parts.append("reasoning trace (excerpt):\n" + r["trace"][:1200])
        parts.append("solution (excerpt):\n" + r["solution"][:600])
    resp = B.chat(verifier, sys_prompt, "\n".join(parts),
                  timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
    parsed = B.extract_json(resp["text"]) or {}
    parsed.setdefault("shortcut_found", "yes" if parsed.get("shortcut_name") else "no")
    parsed.setdefault("shortcut_name", "(unnamed)")
    parsed["_raw"] = resp["text"]
    parsed["_error"] = resp["error"]
    return parsed


# --- edit ladder (Part D) ---------------------------------------------------
def _rung_spec(rung, s12, strat_by_id, shortcut):
    """Return (strategy, intensity, shortcut_dict) for a ladder rung, or None to skip."""
    if rung == "S12_primary":
        if shortcut.get("affordance_is_mutable") == "no":
            return None                          # Part C: do not send a doomed edit
        return s12, "moderate", shortcut
    if rung == "S12_secondary":
        sec = (shortcut.get("secondary_shortcut_name") or "").strip()
        if not sec:
            return None
        return s12, "moderate", {**shortcut, "shortcut_name": sec,
                                 "affordance_in_statement": "",
                                 "removal_suggestion": f"target this shortcut instead: {sec}"}
    if rung == "S07":
        st = strat_by_id.get("S07")
        return (st, "moderate", shortcut) if st else None
    if rung == "S02_aggressive":
        st = strat_by_id.get("S02")
        return (st, "aggressive", {"shortcut_name": "general reframe",
                                   "evidence": shortcut.get("evidence", ""),
                                   "affordance_in_statement": "",
                                   "removal_suggestion": "reframe the whole scenario"}) if st else None
    return None


def _teacher_user(prompts, statement, meta, strat, intensity, shortcut, n_active, n_retired, reason):
    fb = (prompts["fb_tmpl"].replace("{N_ACTIVE}", str(n_active)).replace("{N_RETIRED}", str(n_retired))
          .replace("{SHORTCUT_NAME}", shortcut.get("shortcut_name", ""))
          .replace("{EVIDENCE}", shortcut.get("evidence", ""))
          .replace("{AFFORDANCE}", shortcut.get("affordance_in_statement", ""))
          .replace("{REMOVAL_SUGGESTION}", shortcut.get("removal_suggestion", "")))
    user = (prompts["teacher_user"].replace("{SEED_STATEMENT}", statement)
            .replace("{CLASS}", meta["class"]).replace("{INTENDED_ALGORITHM}", meta["intended_algorithm"])
            .replace("{REDUCTION_NOTE}", meta["reduction_note"])
            .replace("{STRATEGY_NAME}", strat["name"]).replace("{STRATEGY_INSTRUCTION}", strat["instruction"])
            .replace("{INTENSITY}", intensity)
            .replace("{INTENSITY_INSTRUCTION}", prompts["intensities"].get(intensity, ""))
            .replace("{FEEDBACK_BLOCK}", fb))
    if reason:
        user += (f"\n\nThe previous attempt was rejected by review: {reason}\n"
                 "Fix that and respond in the <STATEMENT>...</STATEMENT> tag format exactly.")
    return user


def run_edit_ladder(ldir, depth, statement, shortcut, meta, s12, strat_by_id, prompts,
                    n_active, n_retired, fb_cfg, seed_stmt, sc, run_cfg, exec_cfg):
    """Try ladder rungs until one gate-PASSes. Persist every teacher attempt + gate.
    Returns (result_dict | None, stop_hint)."""
    nddir = ldir / f"d{depth + 1:03d}"
    nddir.mkdir(parents=True, exist_ok=True)
    GV._atomic_write(nddir / "shortcut.json", json.dumps(shortcut, indent=2))

    ladder = fb_cfg.get("fallback_ladder", ["S12_primary"])
    cap = fb_cfg.get("ladder_attempts_per_depth", 4)
    reason = ""
    attempt_i = 0
    any_parsed = False
    any_api_error = False
    for rung in ladder:
        if attempt_i >= cap:
            break
        spec = _rung_spec(rung, s12, strat_by_id, shortcut)
        if spec is None:
            _log(ldir.name, depth, "teacher", f"skip:{rung}", "not applicable (immutable/none)")
            continue
        strat, inten, sc_use = spec
        attempt_i += 1
        user = _teacher_user(prompts, statement, meta, strat, inten, sc_use, n_active, n_retired, reason)
        resp = B.chat(prompts["teacher"], prompts["teacher_sys"], user,
                      timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
        (nddir / f"teacher_attempt_{attempt_i}.txt").write_text(resp["text"] or "")
        parsed = GV.parse_tagged_statement(resp["text"])
        ok = bool(parsed.get("statement"))
        any_parsed = any_parsed or ok
        any_api_error = any_api_error or bool(resp["error"])
        (nddir / f"teacher_attempt_{attempt_i}.json").write_text(json.dumps({
            "rung": rung, "strategy": strat["id"], "intensity": inten,
            "parsed": ok, "parse_error": None if ok else "no <STATEMENT>",
            "api_error": resp["error"], "elapsed_s": resp["elapsed_s"]}, indent=2))
        _log(ldir.name, depth, "teacher", f"{rung}:{'ok' if ok else 'noparse'}", resp["error"] or "")
        if not ok:
            reason = "previous attempt returned no <STATEMENT> tag"
            continue
        gres = GT.evaluate_statement(parsed["statement"], seed_stmt, sc, prompts["verifier"],
                                     run_cfg, prompts["verifier_sys"], prompts["verifier_user"])
        GV._atomic_write(nddir / "gate.json", json.dumps({**gres, "attempt": attempt_i, "rung": rung}, indent=2))
        _log(ldir.name, depth, "gate", gres["result"],
             f"{rung} leakage={gres['leakage_hits']} verifier={gres['verifier'].get('overall')}")
        if gres["result"] == "PASS":
            GV._atomic_write(nddir / "statement.md", parsed["statement"] + "\n")
            GV._atomic_write(nddir / "edit.json", json.dumps({
                "version": f"{ldir.name}/d{depth+1:03d}", "source": "feedback",
                "rung": rung, "strategies": [strat["id"]], "intensity": inten,
                "parent": f"d{depth:03d}", "generation": depth + 1,
                "shortcut_targeted": sc_use.get("shortcut_name"),
                "gate_attempts": attempt_i, "teacher_id": prompts["teacher"]["id"],
                "teacher_raw": resp["text"], "rationale": parsed.get("rationale", ""),
                "risk": parsed.get("risk", ""),
                "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))
            return {"statement": parsed["statement"], "rung": rung, "gate": gres}, None
        reason = f"gate={gres['result']}, leakage={gres['leakage_hits']}, verifier={gres['verifier'].get('overall')}"

    if not any_parsed:
        return None, ("teacher_api_error" if any_api_error else "teacher_parse_failure")
    return None, "ladder_exhausted"


# --- lineage ----------------------------------------------------------------
def run_lineage(ldir, base_vdir, base_strategy, family, crit_dir, sc, tiers, seed_stmt, meta,
                s12, strat_by_id, students, baseline_pass, prompts, fb_cfg, run_cfg, exec_cfg, args):
    ldir.mkdir(parents=True, exist_ok=True)
    # --reset must wipe EVERY existing depth dir first, not just overwrite the ones
    # it regenerates: a shorter new run would otherwise leave stale d0NN folders on
    # disk from a longer previous run, contradicting the fresh lineage.json.
    if args.reset:
        stale = [dd for dd in ldir.glob("d[0-9]*") if dd.is_dir()]
        for dd in stale:
            shutil.rmtree(dd, ignore_errors=True)
        if stale:
            _log(ldir.name, 0, "reset", "cleared", f"removed {len(stale)} stale depth dir(s)")
    max_depth = args.max_depth if args.max_depth is not None else fb_cfg.get("max_depth", 6)
    retire = fb_cfg.get("retire_failed_students", True)
    retest = fb_cfg.get("retest_retired", True)
    min_pass = fb_cfg.get("min_passers_to_continue", 1)
    scoring_tier = fb_cfg.get("scoring_tier", "all")

    statement = (base_vdir / "statement.md").read_text()
    all_ids = [s["id"] for s in students]
    active, retired = list(students), []
    depth_to_defeat = {sid: None for sid in all_ids}
    per_depth, outcome, stop_detail, depth = [], None, "", 0

    while True:
        ddir = ldir / f"d{depth:03d}"
        GV._atomic_write(ddir / "statement.md", statement)
        run_set = active + (retired if retest else [])
        results = {}
        for s in run_set:
            results[s["id"]] = run_student(s, statement, sc, tiers, scoring_tier,
                                           prompts["student_sys"], prompts["student_user"],
                                           run_cfg, exec_cfg, ddir / "attempts" / s["id"], args.reset)
        verdicts = {sid: r["driving"] for sid, r in results.items()}
        active_passers = [s for s in active if verdicts.get(s["id"]) == "PASS"]
        active_failers = [s for s in active if verdicts.get(s["id"]) != "PASS"]
        for s in active_failers:
            if depth_to_defeat[s["id"]] is None:
                depth_to_defeat[s["id"]] = depth
        # raw = every student run this depth, ignoring retirement (Change 1: the
        # scientific metric); active = the steering pool (retirement-affected).
        raw_passers = [sid for sid, v in verdicts.items() if v == "PASS"]
        raw_failers = [sid for sid, v in verdicts.items() if v != "PASS"]
        entry = {"depth": depth,
                 "raw_passers": raw_passers, "raw_failers": raw_failers,
                 "active_passers": [s["id"] for s in active_passers],
                 "passers": [s["id"] for s in active_passers],   # back-compat alias
                 "failers": [s["id"] for s in active_failers], "retired": [s["id"] for s in retired],
                 "n_active": len(active), "verdicts": verdicts,
                 "tier_verdicts": {sid: r["tier_results"] for sid, r in results.items()},
                 "overall_by_student": {sid: r["overall_all_tiers"] for sid, r in results.items()},
                 "shortcut_name": None, "structural_floor": None, "gate_result": None}
        per_depth.append(entry)
        _log(ldir.name, depth, "students", "done",
             f"raw_pass={raw_passers} active_pass={entry['passers']} active_fail={entry['failers']}")
        print(f"  {ldir.name} d{depth}: raw_pass={raw_passers} active_pass={entry['passers']} "
              f"retired={[s['id'] for s in retired]}")

        if retire:
            retired = retired + active_failers
            active = active_passers

        if len(active) < max(1, min_pass):
            outcome = "all_defeated"; break
        if depth >= max_depth:
            outcome = "max_depth"; break

        # resume: reuse an already-written next depth
        nddir = ldir / f"d{depth + 1:03d}"
        if (nddir / "statement.md").exists() and not args.reset:
            statement = (nddir / "statement.md").read_text(); depth += 1; continue

        passer_rows = []
        for s in active_passers:
            adir = ddir / "attempts" / s["id"]
            passer_rows.append({"student": s["id"],
                                "trace": (adir / "trace.txt").read_text() if (adir / "trace.txt").exists() else "",
                                "solution": (adir / "solution.py").read_text() if (adir / "solution.py").exists() else ""})
        shortcut = summarize_shortcut(prompts["verifier"], statement, passer_rows,
                                      prompts["shortcut_sys"], run_cfg, exec_cfg)
        entry["shortcut_name"] = shortcut.get("shortcut_name")
        entry["structural_floor"] = shortcut.get("structural_floor")   # Part E
        _log(ldir.name, depth, "summarize", shortcut.get("shortcut_found", "?"),
             f"{shortcut.get('shortcut_name')} mutable={shortcut.get('affordance_is_mutable')} "
             f"structural_floor={shortcut.get('structural_floor')}")

        if shortcut.get("shortcut_found") == "no":
            outcome = "exhausted"; stop_detail = "no_shortcut_found"; break

        result, stop_hint = run_edit_ladder(ldir, depth, statement, shortcut, meta, s12,
                                            strat_by_id, prompts, len(active), len(retired),
                                            fb_cfg, seed_stmt, sc, run_cfg, exec_cfg)
        if result is None:
            outcome = "exhausted"; stop_detail = stop_hint
            _log(ldir.name, depth, "stop", "exhausted", stop_hint); break
        entry["gate_result"] = result["gate"]["result"]
        statement = result["statement"]; depth += 1

    stop_reason = outcome if outcome in ("all_defeated", "max_depth") else (stop_detail or "exhausted")
    GV._atomic_write(ldir / "lineage.json", json.dumps({
        "lineage": ldir.name, "base_version": base_vdir.name, "base_strategy": base_strategy,
        "family": family, "criterion": crit_dir, "outcome": outcome,
        "stop_reason": stop_reason, "stop_detail": stop_detail,
        "final_depth": per_depth[-1]["depth"] if per_depth else 0,
        "depth_to_defeat": depth_to_defeat, "baseline_pass": baseline_pass,
        "per_depth": per_depth, "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))
    _log(ldir.name, per_depth[-1]["depth"] if per_depth else 0, "lineage", outcome, stop_reason)
    print(f"  {ldir.name}: outcome={outcome} stop_reason={stop_reason} depths={len(per_depth)}")


# --- seed selection ---------------------------------------------------------
def _delta_by_version(family, crit_dir):
    csv_path = B.REPORTS_DIR / f"family_{family}_summary.csv"
    rows = []
    if csv_path.exists():
        with open(csv_path) as f:
            rows = [r for r in csv.DictReader(f) if r["criterion"] == crit_dir]
    if not rows:
        abase = B.ATTEMPTS_DIR / f"family_{family}" / crit_dir
        for vdir in (sorted(abase.glob("v*")) if abase.exists() else []):
            edit = _read_json(B.VERSIONS_DIR / f"family_{family}" / crit_dir / vdir.name / "edit.json")
            for sdir in vdir.glob("*"):
                v = _read_json(sdir / "verdict.json")
                if v:
                    rows.append({"version": vdir.name, "student": sdir.name, "verdict": v.get("overall"),
                                 "source": edit.get("source", "?"),
                                 "strategies": "+".join(edit.get("strategies", []) or [])})
    base_pass = sum(1 for r in rows if r["version"] == "v000" and r["verdict"] == "PASS")
    by_ver = defaultdict(lambda: {"pass": 0})
    for r in rows:
        if r["version"] != "v000" and r["verdict"] == "PASS":
            by_ver[r["version"]]["pass"] += 1
    return {v: info["pass"] - base_pass for v, info in by_ver.items()}


def select_seeds(family, crit_dir, fb_cfg):
    vbase = B.VERSIONS_DIR / f"family_{family}" / crit_dir

    def is_pass_base(vid):
        return (_read_json(vbase / vid / "gate.json").get("result") == "PASS"
                and _read_json(vbase / vid / "edit.json").get("source") in ("grid", "sample", "composition"))

    mode = fb_cfg.get("seed_selection", "top_k")
    if mode == "explicit":
        return [v for v in fb_cfg.get("explicit", []) if (vbase / v / "statement.md").exists()]
    deltas = _delta_by_version(family, crit_dir)
    pass_ids = [v.name for v in sorted(vbase.glob("v*")) if is_pass_base(v.name)]
    if mode == "all":
        return pass_ids
    ranked = sorted([v for v in pass_ids if v in deltas], key=lambda v: deltas[v])
    top = ranked[: fb_cfg.get("top_k", 10)]
    rest = [v for v in pass_ids if v not in top]
    random.Random(1234).shuffle(rest)
    return top + rest[: fb_cfg.get("include_random", 4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2, 3])
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--max-depth", type=int, default=None)
    ap.add_argument("--only-lineage")
    args = ap.parse_args()

    run_cfg = B.load_run_config()
    models = B.load_models()
    exec_cfg = models.get("execution", {})
    fb_cfg = run_cfg.get("feedback_loop", {})
    strategies = GV.load_strategies()
    strat_by_id = {s["id"]: s for s in strategies}
    s12 = strat_by_id.get("S12")
    prompts = {
        "teacher": models["teacher"], "verifier": models["verifier"],
        "intensities": GV.load_intensities(),
        "teacher_sys": (B.PROMPTS_DIR / "teacher_system.md").read_text(),
        "teacher_user": (B.PROMPTS_DIR / "teacher_user_template.md").read_text(),
        "fb_tmpl": (B.PROMPTS_DIR / "teacher_feedback_block.md").read_text(),
        "shortcut_sys": (B.PROMPTS_DIR / "shortcut_summarizer.md").read_text(),
        "verifier_sys": (B.PROMPTS_DIR / "verifier_system.md").read_text(),
        "verifier_user": (B.PROMPTS_DIR / "verifier_user_template.md").read_text(),
        "student_sys": (B.PROMPTS_DIR / "student_system.md").read_text(),
        "student_user": (B.PROMPTS_DIR / "student_user_template.md").read_text(),
    }
    all_students = [s for s in models["students"] if s.get("enabled", True)]

    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        crits = [args.criterion] if args.criterion else run_cfg.get("criteria", [1, 2, 3])
        for c in crits:
            crit_dir = B.criterion_dirname(c)
            sc, tiers = build_scoring(family, slug, crit_dir)
            if sc is None:
                continue
            if tiers.get("scaled") is None:
                print(f"[harden] family={family} {crit_dir}: no scaled tier "
                      f"(Phase 2 never scaled this criterion) -- scaled recorded as null")
            seed_stmt = sc.statement_path.read_text()
            meta = GV._meta_fields((B.SEEDS_DIR / slug / crit_dir / "meta.yaml").read_text())

            v000 = B.ATTEMPTS_DIR / f"family_{family}" / crit_dir / "v000"
            passes_seed = {s["id"]: (_read_json(v000 / s["id"] / "verdict.json").get("overall") == "PASS"
                                     if (v000 / s["id"] / "verdict.json").exists() else True)
                           for s in all_students}
            students = ([s for s in all_students if passes_seed.get(s["id"], True)]
                        if fb_cfg.get("skip_students_failing_seed", True) else all_students)
            baseline_pass = {s["id"]: passes_seed.get(s["id"], True) for s in all_students}

            chosen = select_seeds(family, crit_dir, fb_cfg)
            base = LINEAGES_DIR / f"family_{family}" / crit_dir
            base.mkdir(parents=True, exist_ok=True)
            GV._atomic_write(base / "plan.json", json.dumps({
                "criterion": crit_dir, "seeds": chosen, "students": [s["id"] for s in students],
                "skipped_students": [s["id"] for s in all_students if s not in students],
                "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))
            print(f"[harden] family={family} {crit_dir} seeds={len(chosen)} "
                  f"students={[s['id'] for s in students]}")

            for i, vid in enumerate(chosen, start=1):
                lineage_id = f"L{i:03d}"
                if args.only_lineage and lineage_id != args.only_lineage:
                    continue
                vdir = B.VERSIONS_DIR / f"family_{family}" / crit_dir / vid
                run_lineage(base / lineage_id, vdir,
                            _read_json(vdir / "edit.json").get("strategies", ["?"]),
                            family, crit_dir, sc, tiers, seed_stmt, meta, s12, strat_by_id, students,
                            baseline_pass, prompts, fb_cfg, run_cfg, exec_cfg, args)
    print("[harden] done.")


if __name__ == "__main__":
    main()
