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
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
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


_LOG_LOCK = threading.Lock()   # lineages may run concurrently; serialize log appends


def _log(lineage, depth, step, status, detail=""):
    B.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with _LOG_LOCK, open(B.LOGS_DIR / "harden_loop.log", "a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()} | {lineage} | d{depth} | "
                f"{step} | {status} | {detail}\n")


_CRIT_MEM_LOCK = threading.Lock()   # criterion_memory.json is shared across parallel lineages
_DISCOVERED_LOCK = threading.Lock()


# --- file 52 change 1: defeat = correctness failure, not slowness -----------
def is_defeated(verdict_type: str, target: str) -> bool:
    """Defeat rule (file 52, revised). wrong_answer_only: WRONG_ANSWER/RUNTIME_ERROR only
    (a slow-but-correct TLE is a survivor). wrong_or_slow: ALSO defeat on TLE (a correct
    exponential solution that cannot finish within tle_ceiling_s -- the NP-hard signal).
    all_failures: any non-PASS."""
    if target == "wrong_answer_only":
        return verdict_type in ("WRONG_ANSWER", "RUNTIME_ERROR", "MLE")
    if target == "wrong_or_slow":
        return verdict_type in ("WRONG_ANSWER", "RUNTIME_ERROR", "MLE", "TLE")
    return verdict_type != "PASS"


# --- file 52 change 2: agentic memory ---------------------------------------
def _fresh_memory(lineage, crit_dir):
    return {"lineage": lineage, "criterion": crit_dir, "depth_history": [],
            "student_profiles": {}, "strategies_tried": [], "dead_ends": [], "regressions": []}


def update_lineage_memory(mem, ldir, depth, strat_label, shortcut, gate_composite,
                          defeated_before, defeated_after, regained, survivor_profiles):
    """Append this depth to the lineage memory and rewrite memory.json (file 52 change 2)."""
    newly = [s for s in defeated_after if s not in defeated_before]
    outcome = (f"{len(newly)} newly defeated" if newly else "no new defeat")
    if regained:
        outcome += f"; REGRESSION restored {regained}"
    mem["depth_history"].append({
        "depth": depth, "strategy": strat_label,
        "shortcut_targeted": shortcut.get("common_affordance") or shortcut.get("shortcut_name"),
        "edit_summary": shortcut.get("recommended_edit") or shortcut.get("removal_suggestion", ""),
        "defeated_before": defeated_before, "defeated_after": defeated_after,
        "regained": regained, "gate_composite": gate_composite, "outcome": outcome})
    # strategies_tried: net effect of this strategy label
    net = len(newly) - len(regained)
    mem["strategies_tried"].append({"name": strat_label, "depth": depth,
                                    "net_defeated": net,
                                    "verdict": "strong" if net >= 2 else "weak" if net >= 1 else "dead"})
    if net <= 0 and strat_label:
        mem["dead_ends"].append(f"{strat_label} at depth {depth} - net effect {net}")
    if regained:
        mem["regressions"].append({"depth": depth, "restored": regained, "strategy": strat_label})
    # per-student profiles for survivors (running record)
    for sid, prof in survivor_profiles.items():
        p = mem["student_profiles"].setdefault(sid, {"times_defeated": 0, "defeated_by": [],
                                                      "resistant_to": [], "characteristic_failure": "",
                                                      "never_defeated_by_depth": depth})
        p["never_defeated_by_depth"] = depth
        sc_txt = _as_text(prof.get("shortcut"))
        if sc_txt and sc_txt not in p["resistant_to"]:
            p["resistant_to"].append(sc_txt)
    for sid in newly:
        p = mem["student_profiles"].setdefault(sid, {"times_defeated": 0, "defeated_by": [],
                                                     "resistant_to": [], "characteristic_failure": "",
                                                     "never_defeated_by_depth": None})
        p["times_defeated"] = p.get("times_defeated", 0) + 1
        by = _as_text(shortcut.get("common_affordance") or shortcut.get("shortcut_name"))
        if by and by not in p["defeated_by"]:
            p["defeated_by"].append(by)
    GV._atomic_write(ldir / "memory.json", json.dumps(mem, indent=2))


def merge_criterion_memory(base_dir, mem):
    """Aggregate lineage memory into criterion_memory.json under a lock (parallel-safe)."""
    path = base_dir / "criterion_memory.json"
    with _CRIT_MEM_LOCK:
        cm = _read_json(path) or {"criterion": mem["criterion"],
                                  "defeated_by_strategy": {}, "never_defeated": {}, "lineages": []}
        if mem["lineage"] not in cm["lineages"]:
            cm["lineages"].append(mem["lineage"])
        for st in mem["strategies_tried"]:
            if st["net_defeated"] > 0:
                cm["defeated_by_strategy"].setdefault(st["name"], 0)
                cm["defeated_by_strategy"][st["name"]] += st["net_defeated"]
        for sid, p in mem["student_profiles"].items():
            if p.get("never_defeated_by_depth") is not None and not p.get("times_defeated"):
                cm["never_defeated"][sid] = cm["never_defeated"].get(sid, 0) + 1
        GV._atomic_write(path, json.dumps(cm, indent=2))


def render_memory_block(mem, survivors, defeated, regressions, survivor_profiles, max_tokens):
    """Build the capped {MEMORY_BLOCK} for the teacher (file 52 change 2)."""
    hist = mem["depth_history"]
    worked = [f"- {h['strategy']}: {h['outcome']}" for h in hist if "newly defeated" in h["outcome"]
              and not h["outcome"].startswith("0")]
    dead = mem["dead_ends"][-6:]
    prof_lines = []
    for sid in survivors:
        p = mem["student_profiles"].get(sid, {})
        sc = _as_text(survivor_profiles.get(sid, {}).get("shortcut", ""))
        resist = ", ".join(_as_text(x) for x in p.get("resistant_to", [])[:3])
        prof_lines.append(f"- {sid}: relies on {sc or '(unknown)'}; "
                          f"resistant to {resist or 'nothing yet'}")
    reg = "; ".join(f"d{r['depth']} restored {r['restored']}" for r in regressions[-3:]) or "none"
    block = ("PRIOR ATTEMPTS ON THIS PROBLEM\n"
             "------------------------------\n"
             f"Depths so far: {len(hist)}\n"
             f"Currently defeated: {defeated or 'none'}\n"
             f"Still solving it: {survivors or 'none'}\n\n"
             "What has already worked:\n" + ("\n".join(worked[-4:]) or "- (nothing yet)") + "\n\n"
             "What has already failed - do not repeat these:\n" + ("\n".join(f"- {d}" for d in dead) or "- (none yet)") + "\n\n"
             "Per-student profile of the survivors:\n" + ("\n".join(prof_lines) or "- (none)") + "\n\n"
             "Warning: an edit that defeats a survivor must not restore any student already "
             "defeated.\n"
             f"Previous regressions: {reg}\n")
    budget = max_tokens * 4          # ~4 chars/token
    if len(block) > budget:
        block = block[:budget].rsplit("\n", 1)[0] + "\n[memory truncated]\n"
    return block


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


def _tier_result(sc, tests, solution_path, want_timing=False, ceiling=None):
    if not tests:
        return None
    crit = dataclasses.replace(sc, tests=tests)
    # file 52 change 1: do NOT enforce the problem's time_limit_s; use the runaway ceiling
    # only. A TLE here means "hit the runaway guard", not "too slow for the intended limit".
    pv = judge_problem(crit, solution_path, timeout_override=ceiling)
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


def score_tiers(sc, tiers, solution_path, ceiling=None):
    return {t: _tier_result(sc, tiers.get(t), solution_path, want_timing=(t == "scaled"),
                            ceiling=ceiling)
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
                run_cfg, exec_cfg, out_dir, reset, ceiling=None, target="wrong_answer_only"):
    """Solve, then score against all three tiers separately. Returns the full verdict dict;
    the loop reads verdict['driving'] for the verdict type and verdict['defeated'] for
    retirement (file 52 change 1)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    vp = out_dir / "verdict.json"
    if vp.exists() and not reset:
        cached = _read_json(vp)
        if "defeated" in cached:                 # skip stale pre-file-52 verdicts
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
        driving = "RUNTIME_ERROR"
        verdict = {"tier_results": results, "overall_all_tiers": "RUNTIME_ERROR",
                   "driving": driving, "defeated": is_defeated(driving, target),
                   "error": resp["error"] or "empty solution", **B.usage_of(resp)}
    else:
        results = score_tiers(sc, tiers, out_dir / "solution.py", ceiling=ceiling)
        driving = driving_verdict(results, scoring_tier)
        verdict = {"tier_results": results,
                   "overall_all_tiers": overall_all_tiers(results),
                   "driving": driving, "defeated": is_defeated(driving, target),
                   "error": resp["error"], **B.usage_of(resp)}
    (out_dir / "verdict.json").write_text(json.dumps(verdict, indent=2))
    return verdict


# --- shortcut summarizer ----------------------------------------------------
def summarize_shortcut(verifier, statement, all_rows, sys_prompt, run_cfg, exec_cfg):
    """file 52 change 3: the summarizer reads EVERY student (survivors AND defeated), so it
    can find the single common affordance to defeat all survivors at once and flag edits
    that would restore an already-defeated student."""
    parts = [f"PROBLEM STATEMENT:\n{statement}\n"]
    for r in all_rows:
        state = "STILL SOLVING (survivor)" if not r.get("defeated") else f"already DEFEATED ({r.get('verdict')})"
        parts.append(f"--- model {r['student']}: {state} ---")
        if r.get("trace", "").strip():
            parts.append("reasoning trace (excerpt):\n" + r["trace"][:1200])
        parts.append("solution (excerpt):\n" + r.get("solution", "")[:600])
    resp = B.chat(verifier, sys_prompt, "\n".join(parts),
                  timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
    parsed = B.extract_json(resp["text"]) or {}
    parsed.setdefault("shortcut_found", "yes" if parsed.get("shortcut_name") else "no")
    parsed.setdefault("shortcut_name", "(unnamed)")
    parsed.setdefault("common_affordance", None)
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


_AGGRESSIVE_BLOCK = """AGGRESSIVE MODE

The standard strategy library has not defeated the remaining models. You are no longer
restricted to it. Devise your own approach.

You may combine, extend, or invent methods freely. All hard constraints still apply
without exception: identical answers for every input, unchanged complexity class,
unchanged I/O contract, unambiguous statement, no complexity-class vocabulary.

You MUST name and describe your method. Report:

<METHOD_NAME>a short label for the technique you invented</METHOD_NAME>
<METHOD_DESCRIPTION>what it does and why you expect it to defeat the survivors</METHOD_DESCRIPTION>
<METHOD_NOVEL>yes if this is not one of S01-S12, no if it is a variant</METHOD_NOVEL>"""


def _gate_feedback_block(fb):
    if not fb:
        return ""
    lines = ["GATE FEEDBACK (the gate rejected your last attempt; revise using this. The gate",
             "validates your NEW text independently -- it does not write any text for you.)",
             f"Rejected because: {', '.join(fb.get('rejected_because', [])) or 'format'}"]
    for k, v in fb.items():
        if k.endswith("_detail"):
            lines.append(f"- {k[:-7]}: {v}")
    lines.append(f"Do this: {fb.get('actionable_advice', '')}")
    if fb.get("do_not_change"):
        lines.append(f"Do NOT disturb (these scored well): {', '.join(fb['do_not_change'])}")
    return "\n".join(lines)


def _parse_method(text):
    def g(tag):
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(1).strip() if m else ""
    name = g("METHOD_NAME")
    return {"name": name, "description": g("METHOD_DESCRIPTION"),
            "novel": g("METHOD_NOVEL")} if name else None


def _persist_discovered(discovered_dir, resp, shortcut, depth, lineage, aggressive):
    """file 52 change 4: save an invented method to strategies/discovered/<criterion>/."""
    if not aggressive:
        return None
    method = _parse_method(resp["text"] or "")
    if not method:
        return None
    slug = re.sub(r"[^a-z0-9]+", "-", method["name"].lower()).strip("-")[:60] or "method"
    with _DISCOVERED_LOCK:
        discovered_dir.mkdir(parents=True, exist_ok=True)
        path = discovered_dir / f"{slug}.json"
        rec = _read_json(path) or {"name": method["name"], "description": method["description"],
                                   "novel": method["novel"], "uses": []}
        rec["uses"].append({"lineage": lineage, "depth": depth + 1,
                            "targeted_survivors": [s.get("student") for s in shortcut.get("survivor_shortcuts", [])],
                            "timestamp": datetime.now(timezone.utc).isoformat()})
        GV._atomic_write(path, json.dumps(rec, indent=2))
    return method["name"]


# --- expert co-author (3-way negotiation) -----------------------------------
# Three non-overlapping roles: TEACHER writes all statement text (sole author); EXPERT
# critiques the draft and proposes concrete alternatives but never writes final text; GATE
# validates only (pass/fail + diagnostics, never constructive edits).
def _provider(base_url: str) -> str:
    b = base_url or ""
    if "openrouter.ai" in b:
        return "openrouter"
    if "generativelanguage" in b:
        return "gemini"
    if "api.openai.com" in b:
        return "openai"
    return b


def resolve_expert(models, run_cfg):
    """Return the expert model cfg, or None if disabled. Enforces role separation: the
    expert must not be the teacher, verifier, H5 solver, any student, or the held-out
    model, and must be a different provider than the teacher."""
    ex = models.get("expert")
    if not ex or not ex.get("enabled"):
        return None
    forbidden_ids, forbidden_strings = set(), set()
    for key in ("teacher", "verifier"):
        m = models.get(key, {}) or {}
        forbidden_ids.add(m.get("id")); forbidden_strings.add(m.get("model_string"))
    for grp in ("students", "held_out"):
        for m in models.get(grp, []) or []:
            forbidden_ids.add(m.get("id")); forbidden_strings.add(m.get("model_string"))
    sr = (run_cfg.get("gate", {}) or {}).get("solver_roundtrip", {}) or {}
    forbidden_ids.add(sr.get("model_id")); forbidden_strings.add(sr.get("model_string"))
    if ex.get("id") in forbidden_ids or ex.get("model_string") in forbidden_strings:
        raise SystemExit(f"expert {ex.get('id')} ({ex.get('model_string')}) collides with another "
                         "role (teacher/verifier/H5 solver/student/held-out) -- role separation violated. "
                         "The held-out model (kimi-k3) in particular must never author, or its "
                         "transfer check is invalidated.")
    if _provider(ex.get("base_url", "")) == _provider(models.get("teacher", {}).get("base_url", "")):
        raise SystemExit("expert must be a different provider than the teacher")
    return ex


def expert_critique(expert_cfg, expert_sys, seed_stmt, draft_stmt, gate_fb, run_cfg, exec_cfg):
    """The expert critiques a rejected draft and proposes concrete fixes -- never rewrites."""
    user = (f"SEED (canonical task the rewrite must preserve):\n{seed_stmt}\n\n"
            f"TEACHER'S DRAFT (rejected by the gate):\n{draft_stmt}\n\n"
            f"GATE DIAGNOSTICS:\n{json.dumps(gate_fb, indent=2)}\n\n"
            "Critique the draft and propose concrete fixes. Do NOT rewrite the statement.")
    resp = B.chat(expert_cfg, expert_sys, user,
                  timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
    return {"critique": (resp["text"] or "").strip(), "error": resp["error"], **B.usage_of(resp)}


def _expert_feedback_block(text):
    if not text:
        return ""
    return ("EXPERT REVIEW (an independent expert critiqued your draft and proposed fixes. The\n"
            "expert does NOT write the statement -- you do. Incorporate what is useful.)\n" + text)


def _as_text(x):
    """Coerce a model-produced field to a string. The summarizer sometimes returns a field
    (evidence, affordance, ...) as a list or dict; str.replace() then raises TypeError."""
    if x is None:
        return ""
    if isinstance(x, str):
        return x
    if isinstance(x, (list, tuple)):
        return "; ".join(_as_text(i) for i in x)
    if isinstance(x, dict):
        return "; ".join(f"{k}: {_as_text(v)}" for k, v in x.items())
    return str(x)


def _teacher_user(prompts, statement, meta, strat, intensity, shortcut, n_active, n_retired,
                  gate_feedback=None, memory_block="", aggressive=False, expert_feedback=None):
    # file 52 change 3: when a common affordance exists it is the priority target.
    eff_name = shortcut.get("common_affordance") or shortcut.get("shortcut_name", "")
    eff_removal = shortcut.get("recommended_edit") or shortcut.get("removal_suggestion", "")
    fb = (prompts["fb_tmpl"].replace("{N_ACTIVE}", str(n_active)).replace("{N_RETIRED}", str(n_retired))
          .replace("{SHORTCUT_NAME}", _as_text(eff_name))
          .replace("{EVIDENCE}", _as_text(shortcut.get("evidence", "")))
          .replace("{AFFORDANCE}", _as_text(shortcut.get("affordance_in_statement", "")))
          .replace("{REMOVAL_SUGGESTION}", _as_text(eff_removal)))
    user = (prompts["teacher_user"].replace("{SEED_STATEMENT}", statement)
            .replace("{CLASS}", meta["class"]).replace("{INTENDED_ALGORITHM}", meta["intended_algorithm"])
            .replace("{REDUCTION_NOTE}", meta["reduction_note"])
            .replace("{STRATEGY_NAME}", strat["name"]).replace("{STRATEGY_INSTRUCTION}", strat["instruction"])
            .replace("{INTENSITY}", intensity)
            .replace("{INTENSITY_INSTRUCTION}", prompts["intensities"].get(intensity, ""))
            .replace("{FEEDBACK_BLOCK}", fb)
            .replace("{MEMORY_BLOCK}", memory_block or ""))
    if aggressive:
        user += "\n\n" + _AGGRESSIVE_BLOCK
    efb = _expert_feedback_block(expert_feedback)
    if efb:
        user += "\n\n" + efb
    gfb = _gate_feedback_block(gate_feedback)
    if gfb:
        user += ("\n\n" + gfb +
                 "\nRespond with the corrected statement in the <STATEMENT>...</STATEMENT> tag format exactly.")
    return user


def run_edit_negotiation(ldir, depth, statement, shortcut, meta, s12, strat_by_id, prompts,
                         n_active, n_retired, fb_cfg, seed_stmt, sc, run_cfg, exec_cfg,
                         memory_block, discovered_dir):
    """file 52 changes 4+5: generate candidate rewrites (one per usable ladder rung, up to
    candidates_per_depth ACCEPTED). Each candidate is a NEGOTIATION -- the teacher writes,
    the gate returns actionable feedback on rejection, the teacher revises, a FRESH gate
    call re-validates, up to gate_negotiation_rounds. From aggressive_from_depth the teacher
    may invent its own method (persisted). Keep the highest-composite accepted candidate.
    Returns (result_dict | None, stop_hint). The gate NEVER writes statement text."""
    nddir = ldir / f"d{depth + 1:03d}"
    nddir.mkdir(parents=True, exist_ok=True)
    GV._atomic_write(nddir / "shortcut.json", json.dumps(shortcut, indent=2))

    ladder = fb_cfg.get("fallback_ladder", ["S12_primary"])
    want = fb_cfg.get("candidates_per_depth", 1)
    rounds = fb_cfg.get("gate_negotiation_rounds", 4)
    aggressive = depth >= fb_cfg.get("aggressive_from_depth", 3)
    expert = prompts.get("expert")                    # 3-way negotiation; None if disabled
    accepted, transcript = [], []
    any_parsed = any_api_error = False
    cand_i = 0
    for rung in ladder:
        if len(accepted) >= want:
            break
        spec = _rung_spec(rung, s12, strat_by_id, shortcut)
        if spec is None:
            _log(ldir.name, depth, "teacher", f"skip:{rung}", "not applicable (immutable/none)")
            continue
        strat, inten, sc_use = spec
        cand_i += 1
        gate_fb = None
        expert_fb = None
        for rnd in range(1, rounds + 1):
            # TEACHER drafts/revises (sole author), using memory + gate reasons + expert review
            user = _teacher_user(prompts, statement, meta, strat, inten, sc_use, n_active,
                                 n_retired, gate_feedback=gate_fb, memory_block=memory_block,
                                 aggressive=aggressive, expert_feedback=expert_fb)
            resp = B.chat(prompts["teacher"], prompts["teacher_sys"], user,
                          timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
            (nddir / f"cand{cand_i}_round{rnd}.txt").write_text(resp["text"] or "")
            parsed = GV.parse_tagged_statement(resp["text"])
            ok = bool(parsed.get("statement"))
            any_parsed = any_parsed or ok
            any_api_error = any_api_error or bool(resp["error"])
            expert_fb = None                          # consumed; only re-set on a gate reject
            if not ok:
                gate_fb = {"rejected_because": ["FORMAT"],
                           "actionable_advice": "return the full statement inside <STATEMENT>...</STATEMENT> tags"}
                transcript.append({"candidate": cand_i, "round": rnd, "rung": rung,
                                   "role": "teacher", "parsed": False, "api_error": resp["error"]})
                _log(ldir.name, depth, "negotiate", "noparse", f"cand{cand_i} round{rnd} {rung}")
                continue
            # GATE validates (pass/fail + diagnostics only; never writes/critiques)
            gres = GT.evaluate_statement(parsed["statement"], seed_stmt, sc, prompts["verifier"],
                                         run_cfg, prompts["verifier_sys"], prompts["verifier_user"],
                                         strategies=[strat["id"]],
                                         s09_constraint=parsed.get("added_constraint"),
                                         out_dir=nddir, solver_log_name=f"solver_cand{cand_i}_round{rnd}.txt")
            fb = None if gres["result"] == "ACCEPT" else GT.negotiation_feedback(gres)
            transcript.append({"candidate": cand_i, "round": rnd, "rung": rung, "role": "teacher",
                               "result": gres["result"], "composite": gres.get("composite"),
                               "teacher_raw": resp["text"], "gate_feedback": fb, **B.usage_of(resp)})
            _log(ldir.name, depth, "negotiate", gres["result"],
                 f"cand{cand_i} round{rnd} {rung} composite={gres.get('composite')}")
            if gres["result"] == "ACCEPT":
                method = _persist_discovered(discovered_dir, resp, shortcut, depth, ldir.name, aggressive)
                accepted.append({"statement": parsed["statement"], "rung": rung, "strat": strat,
                                 "inten": inten, "sc_use": sc_use, "resp": resp, "parsed": parsed,
                                 "gres": gres, "candidate": cand_i, "rounds_used": rnd, "method": method})
                break
            gate_fb = fb                              # revise next round using the gate's reasons
            # EXPERT is consulted only when needed (a draft was rejected and rounds remain)
            if expert and rnd < rounds:
                ec = expert_critique(expert, prompts.get("expert_sys", ""), seed_stmt,
                                     parsed["statement"], fb, run_cfg, exec_cfg)
                expert_fb = ec["critique"] or None
                transcript.append({"candidate": cand_i, "round": rnd, "rung": rung, "role": "expert",
                                   "expert_id": expert.get("id"), "expert_critique": ec["critique"],
                                   "error": ec.get("error"), **{k: ec.get(k) for k in
                                   ("input_tokens", "output_tokens", "thinking_tokens", "cost", "elapsed_s")}})
                _log(ldir.name, depth, "expert", expert.get("id"),
                     f"cand{cand_i} round{rnd} critiqued rejected draft")

    if fb_cfg.get("negotiation_transcript", True):
        GV._atomic_write(nddir / "negotiation.json", json.dumps(transcript, indent=2))

    if accepted:
        best = max(accepted, key=lambda c: (c["gres"].get("composite") or -1.0))
        gres, parsed, resp = best["gres"], best["parsed"], best["resp"]
        strat, inten, sc_use = best["strat"], best["inten"], best["sc_use"]
        GV._atomic_write(nddir / "gate.json", json.dumps(
            {**gres, "candidate": best["candidate"], "rung": best["rung"],
             "rounds_used": best["rounds_used"]}, indent=2))
        GV._atomic_write(nddir / "statement.md", best["statement"] + "\n")
        GV._atomic_write(nddir / "edit.json", json.dumps({
            "version": f"{ldir.name}/d{depth+1:03d}", "source": "feedback",
            "rung": best["rung"], "strategies": [strat["id"]], "intensity": inten,
            "parent": f"d{depth:03d}", "generation": depth + 1,
            "shortcut_targeted": sc_use.get("common_affordance") or sc_use.get("shortcut_name"),
            "aggressive": aggressive, "discovered_method": best.get("method"),
            "rounds_used": best["rounds_used"], "candidates_accepted": len(accepted),
            "composite": gres.get("composite"), "teacher_id": prompts["teacher"]["id"],
            "teacher_raw": resp["text"], "rationale": parsed.get("rationale", ""),
            "risk": parsed.get("risk", ""),
            "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))
        _log(ldir.name, depth, "select", best["rung"],
             f"best composite={gres.get('composite')} of {len(accepted)} accepted "
             f"(rounds={best['rounds_used']})")
        return {"statement": best["statement"], "rung": best["rung"], "gate": gres,
                "method": best.get("method")}, None

    if not any_parsed:
        return None, ("teacher_api_error" if any_api_error else "teacher_parse_failure")
    return None, "negotiation_failed"


# --- lineage ----------------------------------------------------------------
def run_lineage(ldir, base_vdir, base_strategy, family, crit_dir, sc, tiers, seed_stmt, meta,
                s12, strat_by_id, students, baseline_pass, prompts, fb_cfg, run_cfg, exec_cfg, args):
    ldir.mkdir(parents=True, exist_ok=True)
    tiers = dict(tiers)   # lineage-local view; the corner tier grows on the shared disk store
                          # (content-addressed, safe for parallel lineages) and we refresh here

    # --- checkpoint / resume (per lineage) ---------------------------------------------
    # progress.json is the checkpoint stamp for THIS run's design. Three cases on entry:
    #   --reset            -> wipe all depth dirs, start fresh.
    #   --resume + complete -> skip (already finished this run).
    #   --resume + in_progress -> keep depths whose students finished (progress.depths_done),
    #                             wipe anything beyond (possibly-partial), continue.
    #   no progress.json (stale old-run dirs, or never started) -> treat as fresh (wipe),
    #                             so a stale hybrid can never be mistaken for a checkpoint.
    def _wipe_depths(above=-1):
        for dd in ldir.glob("d[0-9]*"):
            try:
                dn = int(dd.name[1:])
            except ValueError:
                continue
            if dd.is_dir() and dn > above:
                shutil.rmtree(dd, ignore_errors=True)

    # Any non-reset run is checkpoint-aware (re-run to continue; --reset to restart). The
    # --resume flag is accepted as an explicit synonym but is no longer required.
    prog = _read_json(ldir / "progress.json")
    if args.reset:
        # clear the WHOLE lineage -- depth dirs AND memory.json / old lineage.json /
        # progress.json / shortcut caches -- so a rerun is never a mix of old and new.
        for item in list(ldir.iterdir()):
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            else:
                try:
                    item.unlink()
                except OSError:
                    pass
        prog = {}
        _log(ldir.name, 0, "reset", "cleared", "whole lineage wiped")
    elif prog.get("status") == "complete":
        print(f"  {ldir.name}: [checkpoint] already complete -- skipped")
        _log(ldir.name, 0, "resume", "skip", "already complete")
        return
    elif prog.get("status") == "in_progress":
        last = max(prog.get("depths_done", [-1]) or [-1])
        _wipe_depths(above=last)          # drop the partial tail; keep finished depths
        print(f"  {ldir.name}: [checkpoint] resuming from depth {last + 1}")
        _log(ldir.name, 0, "resume", "continue", f"from depth {last + 1}")
    else:
        _wipe_depths(); prog = {}         # no checkpoint (stale/foreign dirs) -> fresh & safe

    def _checkpoint(depths_done, status="in_progress"):
        GV._atomic_write(ldir / "progress.json", json.dumps(
            {"lineage": ldir.name, "status": status, "depths_done": sorted(depths_done),
             "hardening_target": fb_cfg.get("hardening_target"),
             "updated_at": datetime.now(timezone.utc).isoformat()}, indent=2))

    _checkpoint([], "in_progress")
    max_depth = args.max_depth if args.max_depth is not None else fb_cfg.get("max_depth", 10)
    retire = fb_cfg.get("retire_failed_students", True)
    retest = fb_cfg.get("retest_retired", True)
    min_pass = fb_cfg.get("min_passers_to_continue", 1)
    scoring_tier = fb_cfg.get("scoring_tier", "all")
    # Audit B1/B8: score at the DECLARED task deadline, not a 300s runaway guard. The checker
    # also enforces min(declared, ceiling), so this is belt-and-suspenders and keeps runs fast.
    ceiling = sc.meta.get("time_limit_s", 2)
    target = fb_cfg.get("hardening_target", "wrong_answer_only")
    mem_cap = fb_cfg.get("memory_block_max_tokens", 1500)     # change 2
    discovered_dir = B.STRATEGIES_DIR / "discovered" / crit_dir   # change 4

    statement = (base_vdir / "statement.md").read_text()
    all_ids = [s["id"] for s in students]
    active, retired = list(students), []
    depth_to_defeat = {sid: None for sid in all_ids}
    per_depth, outcome, stop_detail, depth = [], None, "", 0
    mem = _fresh_memory(ldir.name, crit_dir)                  # change 2
    prev_raw_defeated, all_regressions, last_edit = set(), [], None

    while True:
        ddir = ldir / f"d{depth:03d}"
        GV._atomic_write(ddir / "statement.md", statement)
        # Audit B8: run the WHOLE panel every depth. Defeat is judged from the current raw
        # panel (not cumulative retirement), so a model that regains PASS is automatically
        # active again next depth -- no permanent retirement.
        run_set = list(students)
        results = {}
        for s in run_set:
            results[s["id"]] = run_student(s, statement, sc, tiers, scoring_tier,
                                           prompts["student_sys"], prompts["student_user"],
                                           run_cfg, exec_cfg, ddir / "attempts" / s["id"], args.reset,
                                           ceiling=ceiling, target=target)
        verdicts = {sid: r["driving"] for sid, r in results.items()}
        defeated_flag = {sid: bool(r.get("defeated")) for sid, r in results.items()}
        # change 1: retirement is DEFEAT-driven (WRONG_ANSWER/RUNTIME_ERROR), not slowness.
        active_defeated = [s for s in active if defeated_flag.get(s["id"])]
        survivors = [s for s in active if not defeated_flag.get(s["id"])]
        for s in active_defeated:
            if depth_to_defeat[s["id"]] is None:
                depth_to_defeat[s["id"]] = depth
        # raw = every student run this depth (retirement-independent scientific metric)
        raw_defeated = {sid for sid, r in results.items() if r.get("defeated")}
        raw_passers = [sid for sid, v in verdicts.items() if v == "PASS"]
        raw_survivors = [sid for sid in verdicts if sid not in raw_defeated]
        regained = sorted(prev_raw_defeated - raw_defeated)   # change 3: regression tracking
        if regained:
            all_regressions.append({"depth": depth, "restored": regained})
            _log(ldir.name, depth, "regression", "restored", str(regained))

        # change 2: record the effect of the edit that produced THIS depth
        if last_edit is not None:
            update_lineage_memory(mem, ldir, depth, last_edit["strat_label"], last_edit["shortcut"],
                                  last_edit["composite"], sorted(prev_raw_defeated),
                                  sorted(raw_defeated), regained, last_edit["survivor_profiles"])
            merge_criterion_memory(LINEAGES_DIR / f"family_{family}" / crit_dir, mem)

        entry = {"depth": depth, "raw_passers": raw_passers,
                 "raw_defeated": sorted(raw_defeated), "raw_survivors": sorted(raw_survivors),
                 "raw_failers": [sid for sid, v in verdicts.items() if v != "PASS"],  # back-compat
                 "active_survivors": [s["id"] for s in survivors],
                 "passers": [s["id"] for s in survivors],           # back-compat alias
                 "defeated_now": [s["id"] for s in active_defeated],
                 "failers": [s["id"] for s in active_defeated],      # back-compat
                 "retired": [s["id"] for s in retired], "regained": regained,
                 "n_active": len(active), "verdicts": verdicts, "defeated_flags": defeated_flag,
                 "tier_verdicts": {sid: r["tier_results"] for sid, r in results.items()},
                 "overall_by_student": {sid: r["overall_all_tiers"] for sid, r in results.items()},
                 "shortcut_name": None, "common_affordance": None,
                 "structural_floor": None, "gate_result": None}
        per_depth.append(entry)
        _checkpoint([e["depth"] for e in per_depth])   # depth d's students are scored -> safe to resume here
        _log(ldir.name, depth, "students", "done",
             f"raw_defeated={sorted(raw_defeated)} survivors={[s['id'] for s in survivors]}")
        print(f"  {ldir.name} d{depth}: defeated={sorted(raw_defeated)} "
              f"survivors={[s['id'] for s in survivors]} regained={regained}")

        # Audit B8: a lineage is defeated ONLY when the current raw panel has zero passers
        # within the declared limit (simultaneous defeat). Cumulative-retirement stopping is
        # removed -- the loop keeps going while any model still solves it raw.
        simultaneous = bool(all_ids) and all(sid in raw_defeated for sid in all_ids)
        prev_raw_defeated = raw_defeated

        if simultaneous:
            outcome = "all_defeated_simultaneously"; break
        if depth >= max_depth:
            outcome = "max_depth"; break

        # resume: reuse an already-written next depth
        nddir = ldir / f"d{depth + 1:03d}"
        if (nddir / "statement.md").exists() and not args.reset:
            statement = (nddir / "statement.md").read_text(); last_edit = None; depth += 1; continue

        # change 3: the summarizer reads EVERY student (survivors AND defeated)
        all_rows = []
        for s in run_set:
            adir = ddir / "attempts" / s["id"]
            all_rows.append({"student": s["id"], "defeated": defeated_flag.get(s["id"]),
                             "verdict": verdicts.get(s["id"]),
                             "trace": (adir / "trace.txt").read_text() if (adir / "trace.txt").exists() else "",
                             "solution": (adir / "solution.py").read_text() if (adir / "solution.py").exists() else ""})
        shortcut = summarize_shortcut(prompts["verifier"], statement, all_rows,
                                      prompts["shortcut_sys"], run_cfg, exec_cfg)
        entry["shortcut_name"] = shortcut.get("shortcut_name")
        entry["common_affordance"] = shortcut.get("common_affordance")
        entry["structural_floor"] = shortcut.get("structural_floor")
        _log(ldir.name, depth, "summarize", shortcut.get("shortcut_found", "?"),
             f"common_affordance={shortcut.get('common_affordance')} name={shortcut.get('shortcut_name')} "
             f"structural_floor={shortcut.get('structural_floor')}")

        # Adversarial corner attack: differential-test the current survivors and add the
        # inputs they get WRONG (or too-slow) into the corner tier, so the NEXT depth scores
        # everyone on them. This is the defeat lever for P/INFEASIBLE and, when the wording
        # floor is hit (structural_floor), the PIVOT that keeps the remaining depth productive
        # instead of re-hitting the floor. (file 52 follow-up.)
        adv = fb_cfg.get("adversarial_corner", {}) or {}
        floor = shortcut.get("structural_floor") == "yes"
        if adv.get("enabled") and survivors and (not floor or adv.get("on_structural_floor", True)):
            sols = [str(ddir / "attempts" / s["id"] / "solution.py") for s in survivors
                    if (ddir / "attempts" / s["id"] / "solution.py").exists()]
            try:
                import gen_adversarial as ADV
                k = ADV.generate(family, crit_dir,
                                 keep=adv.get("cases_per_survivor", 4) * max(1, len(survivors)),
                                 pool=adv.get("candidate_pool", 40), seed=1000 + depth,
                                 against=sols, ceiling=ceiling)
                entry["adversarial_added"] = k
                _log(ldir.name, depth, "adversarial", f"added={k}",
                     f"pivot={floor} survivors={[s['id'] for s in survivors]}")
                # refresh the corner tier so later depths in THIS lineage see the new cases
                tiers["corner"] = _tests_from_dir(B.TESTS_DIR / f"family_{family}" / crit_dir)
            except Exception as ex:      # never let adversarial gen crash the lineage
                _log(ldir.name, depth, "adversarial", "error", str(ex)[:150])

        # A wording floor is no longer a stop -- the corner attack above IS the pivot. Only
        # stop if the summarizer found nothing to target AND no common affordance AND we
        # could not add any adversarial cases this depth.
        if (shortcut.get("shortcut_found") == "no" and not shortcut.get("common_affordance")
                and not entry.get("adversarial_added")):
            outcome = "exhausted"; stop_detail = "no_shortcut_found"; break

        survivor_profiles = {s.get("student"): s for s in shortcut.get("survivor_shortcuts", [])}
        memory_block = render_memory_block(mem, [s["id"] for s in survivors], sorted(raw_defeated),
                                           all_regressions, survivor_profiles, mem_cap)

        result, stop_hint = run_edit_negotiation(ldir, depth, statement, shortcut, meta, s12,
                                                 strat_by_id, prompts, len(active), len(retired),
                                                 fb_cfg, seed_stmt, sc, run_cfg, exec_cfg,
                                                 memory_block, discovered_dir)
        if result is None:
            outcome = "exhausted"; stop_detail = stop_hint
            _log(ldir.name, depth, "stop", stop_hint, stop_hint); break
        entry["gate_result"] = result["gate"]["result"]
        last_edit = {"strat_label": result.get("method") or result.get("rung"),
                     "shortcut": shortcut, "composite": result["gate"].get("composite"),
                     "survivor_profiles": survivor_profiles}
        statement = result["statement"]; depth += 1

    stop_reason = outcome if outcome in ("all_defeated", "max_depth",
                                         "all_defeated_simultaneously") else (stop_detail or "exhausted")
    GV._atomic_write(ldir / "lineage.json", json.dumps({
        "lineage": ldir.name, "base_version": base_vdir.name, "base_strategy": base_strategy,
        "family": family, "criterion": crit_dir, "outcome": outcome,
        "simultaneous_defeat": outcome == "all_defeated_simultaneously",
        "stop_reason": stop_reason, "stop_detail": stop_detail,
        "final_depth": per_depth[-1]["depth"] if per_depth else 0,
        "depth_to_defeat": depth_to_defeat, "baseline_pass": baseline_pass,
        "regressions": all_regressions, "hardening_target": target,
        "per_depth": per_depth, "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))
    _checkpoint([e["depth"] for e in per_depth], status="complete")   # lineage finished
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
        return (_read_json(vbase / vid / "gate.json").get("result") in ("PASS", "ACCEPT")
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
    chosen = top + rest[: fb_cfg.get("include_random", 4)]
    # Normalize to a fixed lineage count across families (comparability). If ranking had too
    # little student-delta data to fill top_k, top up with more accepted variants at random.
    target = fb_cfg.get("target_lineages")
    if target:
        if len(chosen) < target:
            extra = [v for v in pass_ids if v not in chosen]
            random.Random(4321).shuffle(extra)
            chosen += extra[: target - len(chosen)]
        chosen = chosen[:target]
    return chosen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    ap.add_argument("--resume", action="store_true",
                    help="explicit synonym for the default: continue from the per-lineage "
                         "checkpoint (progress.json). Any non --reset run already resumes.")
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--max-depth", type=int, default=None)
    ap.add_argument("--only-lineage")
    ap.add_argument("--lineage-workers", type=int, default=None,
                    help="concurrent lineages (default: feedback_loop.lineage_workers or 4)")
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
    # Expert co-author (3-way negotiation). resolve_expert enforces role separation and
    # raises if the expert collides with the teacher/verifier/solver/student/held-out.
    expert_cfg = resolve_expert(models, run_cfg)
    prompts["expert"] = expert_cfg
    ex_prompt = B.PROMPTS_DIR / "expert_system.md"
    prompts["expert_sys"] = ex_prompt.read_text() if ex_prompt.exists() else ""
    if expert_cfg:
        print(f"[harden] expert co-author: {expert_cfg['id']} ({expert_cfg['model_string']}) "
              f"invoke_when={expert_cfg.get('invoke_when', 'on_reject')}")
    all_students = [s for s in models["students"] if s.get("enabled", True)]

    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        crits = [args.criterion] if args.criterion else run_cfg.get("criteria", [1, 2])
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
            if args.reset:
                # full reset: also drop the aggregated criterion memory and the adversarial
                # adv_* corner cases from prior runs (the 12 hand-made corner cases stay), so
                # the corner tier and memory start clean -- no mixed state.
                (base / "criterion_memory.json").unlink(missing_ok=True)
                store = B.TESTS_DIR / f"family_{family}" / crit_dir
                removed = 0
                for p in store.glob("adv_*") if store.exists() else []:
                    try:
                        p.unlink(); removed += 1
                    except OSError:
                        pass
                if removed:
                    print(f"[harden] reset: cleared {removed} adversarial corner file(s) for {crit_dir}")
            GV._atomic_write(base / "plan.json", json.dumps({
                "criterion": crit_dir, "seeds": chosen, "students": [s["id"] for s in students],
                "skipped_students": [s["id"] for s in all_students if s not in students],
                "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))
            print(f"[harden] family={family} {crit_dir} seeds={len(chosen)} "
                  f"students={[s['id'] for s in students]}")

            # Lineages are fully independent (each writes only its own L*/ dir), so run
            # them concurrently. lineage_workers (config feedback_loop.lineage_workers,
            # default 4; --lineage-workers overrides) is the single largest speedup.
            tasks = []
            for i, vid in enumerate(chosen, start=1):
                lineage_id = f"L{i:03d}"
                if args.only_lineage and lineage_id != args.only_lineage:
                    continue
                vdir = B.VERSIONS_DIR / f"family_{family}" / crit_dir / vid
                tasks.append((lineage_id, vdir))

            def _run(task):
                lineage_id, vdir = task
                run_lineage(base / lineage_id, vdir,
                            _read_json(vdir / "edit.json").get("strategies", ["?"]),
                            family, crit_dir, sc, tiers, seed_stmt, meta, s12, strat_by_id, students,
                            baseline_pass, prompts, fb_cfg, run_cfg, exec_cfg, args)

            lw = args.lineage_workers if args.lineage_workers is not None \
                else fb_cfg.get("lineage_workers", 4)
            if lw <= 1 or len(tasks) <= 1:
                for t in tasks:
                    _run(t)
            else:
                print(f"[harden] running {len(tasks)} lineages with {lw} workers")
                with ThreadPoolExecutor(max_workers=lw) as ex:
                    list(ex.map(_run, tasks))
    print("[harden] done.")


if __name__ == "__main__":
    main()
