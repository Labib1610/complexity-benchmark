#!/usr/bin/env python3
"""Feedback-driven hardening (strategy S12): make a version harder for ALL models,
one problem at a time, with an inner loop that the VERIFIER stops.

For each target version (one the models still solve):
  1. Aggregate EVERY student's behaviour on it (verdict + reasoning trace + solution).
  2. A summarizer names the single shared shortcut/gap they exploited.
  3. INNER LOOP: the teacher (S12 + that feedback) rewrites the statement to remove the
     shortcut; the verifier checks it; if it is still a valid, unambiguous, same-task
     statement it is SAVED and the loop hardens it again (one generation deeper); the
     moment the verifier warns it has become ambiguous / not-the-same-task (or leakage
     appears, or max_generation is reached), the loop stops and moves to the next problem.

Every generated statement is saved as its own version (statement.md + edit.json +
gate.json) so nothing is lost.

Run order:  run_students -> feedback -> run_students -> report   (repeat)

CLI: python tools/feedback.py --family 01 [--criterion 1] [--version v012]
        [--max-targets 10] [--min-pass 1] [--rounds 3] [--intensity moderate]
        [--dry-run] [--reset]
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import backends as B
import generate_versions as GV
import gate as GT

_SUMMARY_SYSTEM = (
    "You analyse how several AI models attempted one programming problem. In 2-4 "
    "sentences, name the SINGLE shared shortcut, surface cue, or pattern-match that let "
    "them recognise or solve it without doing the intended reasoning. Be concrete and "
    "specific to this problem. If they mostly failed, say what little signal the passers "
    "used. Output plain prose only -- no preamble, no JSON."
)


def _read(p: Path, default=""):
    try:
        return p.read_text()
    except Exception:
        return default


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def collect_attempts(family, crit_dir, vid):
    adir = B.ATTEMPTS_DIR / f"family_{family}" / crit_dir / vid
    rows = []
    if not adir.exists():
        return rows
    for sdir in sorted(adir.glob("*")):
        v = _read_json(sdir / "verdict.json")
        if not v:
            continue
        rows.append({"student": sdir.name, "verdict": v.get("overall", "?"),
                     "n_passed": v.get("n_passed", 0), "n_cases": v.get("n_cases", 0),
                     "trace": _read(sdir / "trace.txt"), "solution": _read(sdir / "solution.py")})
    return rows


def summarize_shortcut(summarizer_cfg, version_stmt, attempts, run_cfg, exec_cfg):
    parts = []
    for a in attempts:
        parts.append(f"--- model {a['student']} | verdict {a['verdict']} "
                     f"({a['n_passed']}/{a['n_cases']} cases) ---")
        if a["trace"].strip():
            parts.append("reasoning trace (excerpt):\n" + a["trace"][:1000])
        parts.append("solution (excerpt):\n" + a["solution"][:600])
    user = (f"PROBLEM STATEMENT:\n{version_stmt}\n\nMODEL BEHAVIOUR ({len(attempts)} models):\n"
            + "\n".join(parts) + "\n\nName the single shared shortcut the passing models used.")
    resp = B.chat(summarizer_cfg, _SUMMARY_SYSTEM, user,
                  timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=exec_cfg.get("retries", 3))
    return (resp["text"].strip() or "(no clear shared pattern extracted)"), resp["error"]


def select_targets(out_base, family, crit_dir, min_pass, max_gen):
    cands = []
    for vdir in sorted(out_base.glob("v*")):
        if _read_json(vdir / "gate.json").get("result") in ("FAIL", "REJECT"):
            continue
        gen = _read_json(vdir / "edit.json").get("generation", 0)
        if gen >= max_gen:
            continue
        att = collect_attempts(family, crit_dir, vdir.name)
        if not att:
            continue
        n_pass = sum(1 for a in att if a["verdict"] == "PASS")
        if n_pass < min_pass:
            continue
        cands.append((n_pass, vdir, att, gen))
    cands.sort(key=lambda x: -x[0])   # easiest for the field first
    return cands


def _harden_once(teacher, system, user_tmpl, fb_tmpl, meta, s12, base_stmt,
                 intensity, intensity_text, n, n_pass, summary, run_cfg, exec_cfg):
    feedback_block = (fb_tmpl.replace("{N}", str(n)).replace("{N_PASSED}", str(n_pass))
                      .replace("{TRACE_SUMMARY}", summary))
    user = (user_tmpl.replace("{SEED_STATEMENT}", base_stmt)
            .replace("{CLASS}", meta["class"]).replace("{INTENDED_ALGORITHM}", meta["intended_algorithm"])
            .replace("{REDUCTION_NOTE}", meta["reduction_note"])
            .replace("{STRATEGY_NAME}", s12["name"]).replace("{STRATEGY_INSTRUCTION}", s12["instruction"])
            .replace("{INTENSITY}", intensity).replace("{INTENSITY_INSTRUCTION}", intensity_text)
            .replace("{FEEDBACK_BLOCK}", feedback_block))
    resp = B.chat(teacher, system, user, timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=exec_cfg.get("retries", 3))
    parsed = GV.parse_tagged_statement(resp["text"])
    if not parsed.get("statement"):
        resp = B.chat(teacher, system, user + "\n\nUse the <STATEMENT>...</STATEMENT> tag format exactly.",
                      timeout=run_cfg.get("request_timeout_s", 1800), retries=exec_cfg.get("retries", 3))
        parsed = GV.parse_tagged_statement(resp["text"])
    return parsed, resp


def run_criterion(family, criterion, args, run_cfg, models, strategies, intensities,
                  verifier_system, verifier_user_tmpl):
    teacher = models["teacher"]
    verifier = models["verifier"]
    summarizer = verifier                       # cheap model to summarize traces
    exec_cfg = models.get("execution", {})
    slug = B.family_slug(family)
    crit_dir = B.criterion_dirname(criterion)
    seed_crit = GT.seed_criterion(slug, crit_dir)
    if seed_crit is None:
        return
    seed_stmt = seed_crit.statement_path.read_text()
    meta = GV._meta_fields((B.SEEDS_DIR / slug / crit_dir / "meta.yaml").read_text())
    s12 = next((s for s in strategies if s["id"] == "S12"), None)
    intensity_text = intensities.get(args.intensity, "")
    system = (B.PROMPTS_DIR / "teacher_system.md").read_text()
    user_tmpl = (B.PROMPTS_DIR / "teacher_user_template.md").read_text()
    fb_tmpl = (B.PROMPTS_DIR / "teacher_feedback_block.md").read_text()
    out_base = B.VERSIONS_DIR / f"family_{family}" / crit_dir
    max_gen = run_cfg.get("max_generation", 2)

    targets = select_targets(out_base, family, crit_dir, args.min_pass, max_gen)
    if args.version:
        targets = [t for t in targets if t[1].name == args.version]
    targets = targets[:args.max_targets]
    print(f"[feedback] family={family} {crit_dir} class={meta['class']} targets={len(targets)} "
          f"rounds={args.rounds} intensity={args.intensity} dry_run={args.dry_run}")

    made = 0
    for (n_pass, pdir, att, gen) in targets:
        n = len(att)
        summary, serr = ((f"(dry-run) would summarize {n} model traces", None) if args.dry_run
                         else summarize_shortcut(summarizer, (pdir / "statement.md").read_text(),
                                                 att, run_cfg, exec_cfg))
        base_stmt = (pdir / "statement.md").read_text()
        parent = pdir.name
        cur_gen = gen
        print(f"  target {parent} (passers {n_pass}/{n}) -> hardening")
        for r in range(args.rounds):
            if cur_gen >= max_gen:
                print(f"    stop: reached max_generation={max_gen}")
                break
            if args.dry_run:
                print(f"    [dry] round {r+1}: would harden {parent} (gen {cur_gen+1}) with S12")
                break
            parsed, resp = _harden_once(teacher, system, user_tmpl, fb_tmpl, meta, s12,
                                        base_stmt, args.intensity, intensity_text,
                                        n, n_pass, summary, run_cfg, exec_cfg)
            new_stmt = (parsed.get("statement") or "").strip()
            if not new_stmt:
                print(f"    stop: teacher returned no statement ({resp['error']})")
                break
            # allocate the version dir first so H5 can persist solver_attempt.txt into it
            vid = f"v{GV._max_version_num(out_base) + 1:03d}"
            vdir = out_base / vid
            vdir.mkdir(parents=True, exist_ok=True)
            # verifier gates the candidate; it decides when to stop
            gres = GT.evaluate_statement(new_stmt, seed_stmt, seed_crit, verifier,
                                         run_cfg, verifier_system, verifier_user_tmpl,
                                         strategies=["S12"],
                                         s09_constraint=parsed.get("added_constraint"),
                                         out_dir=vdir)
            GV._atomic_write(vdir / "statement.md", new_stmt + "\n")
            GV._atomic_write(vdir / "edit.json", json.dumps({
                "version": vid, "family": family, "criterion": criterion,
                "source": "feedback", "strategies": ["S12"], "intensity": args.intensity,
                "parent": parent, "generation": cur_gen + 1,
                "feedback": {"n_models": n, "n_passed": n_pass, "summary": summary,
                             "summary_error": serr, "round": r + 1,
                             "students": [{"student": a["student"], "verdict": a["verdict"]} for a in att]},
                "rationale": parsed.get("rationale", ""), "risk": parsed.get("risk", ""),
                "preserved_answer": parsed.get("preserved_answer", ""),
                "preserved_class": parsed.get("preserved_class", ""),
                "teacher_id": teacher["id"], "teacher_raw": resp["text"],
                "parse_ok": True, "error": resp["error"], **B.usage_of(resp),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }, indent=2))
            GV._atomic_write(vdir / "gate.json", json.dumps({"version": vid, **gres}, indent=2))
            made += 1
            print(f"    round {r+1}: {vid} gen={cur_gen+1} verifier={gres['result']}"
                  + (f" leakage={gres['leakage_hits']}" if gres['leakage_hits'] else ""))
            if gres["result"] == "ACCEPT":
                # still valid and unambiguous -> keep hardening this problem, deeper
                base_stmt, parent, cur_gen = new_stmt, vid, cur_gen + 1
            else:
                # gate FLAG/REJECT (ambiguous, not-same-task, leakage, or hard fail) -> next
                print(f"    stop: gate said {gres['result']} -> move to next problem")
                break
    print(f"[feedback] family={family} {crit_dir} -> {made} new version(s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2, 3])
    ap.add_argument("--version")
    ap.add_argument("--max-targets", type=int, default=10)
    ap.add_argument("--min-pass", type=int, default=1)
    ap.add_argument("--rounds", type=int, default=3, help="max hardening iterations per problem")
    ap.add_argument("--intensity", default="moderate")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    run_cfg = B.load_run_config()
    models = B.load_models()
    strategies = GV.load_strategies()
    intensities = GV.load_intensities()
    verifier_system = (B.PROMPTS_DIR / "verifier_system.md").read_text()
    verifier_user_tmpl = (B.PROMPTS_DIR / "verifier_user_template.md").read_text()
    crits = [args.criterion] if args.criterion else run_cfg.get("criteria", [1, 2, 3])
    for family in B.list_families(args.family):
        for c in crits:
            run_criterion(family, c, args, run_cfg, models, strategies, intensities,
                          verifier_system, verifier_user_tmpl)
    print("[feedback] done.")


if __name__ == "__main__":
    main()
