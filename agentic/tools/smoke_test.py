#!/usr/bin/env python3
"""LiteLLM smoke test -- one live call per model before a full run.

Verifies that every model in the panel (students + verifier + H5 solver) returns via
litellm with usable content AND populated usage/cost, so the full family run doesn't
discover a broken model or missing pricing 6 hours in.

  python tools/smoke_test.py --family 01 --criterion 1
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import backends as B          # noqa: E402
import gate as G              # noqa: E402


def _fmt(resp):
    return (f"in={resp.get('input_tokens')} out={resp.get('output_tokens')} "
            f"think={resp.get('thinking_tokens')} cost=${resp.get('cost')} "
            f"{resp.get('elapsed_s')}s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", default="01")
    ap.add_argument("--criterion", type=int, default=1)
    args = ap.parse_args()

    models = B.load_models()
    run_cfg = B.load_run_config()
    crit_dir = B.criterion_dirname(args.criterion)
    sc = G.seed_criterion(B.family_slug(args.family), crit_dir)
    seed_stmt = sc.statement_path.read_text()

    student_sys = (B.PROMPTS_DIR / "student_system.md").read_text()
    student_usr = (B.PROMPTS_DIR / "student_user_template.md").read_text().replace("{STATEMENT}", seed_stmt)
    verifier_sys = (B.PROMPTS_DIR / "verifier_system.md").read_text()
    verifier_usr = (B.PROMPTS_DIR / "verifier_user_template.md").read_text() \
        .replace("{SEED}", seed_stmt).replace("{CANDIDATE}", seed_stmt)

    ok = True
    total_cost = 0.0
    print(f"[smoke] family {args.family} {crit_dir} -- one call per model via litellm\n")

    # 1. students (each must emit non-empty code)
    for s in [m for m in models["students"] if m.get("enabled", True)]:
        r = B.chat(s, student_sys, student_usr,
                   timeout=run_cfg.get("request_timeout_s", 1800), retries=1)
        code = B.extract_code(B.strip_thinking(r["text"]))
        good = r["error"] is None and bool(code.strip())
        ok = ok and good
        total_cost += (r.get("cost") or 0) or 0
        print(f"  {'OK ' if good else 'FAIL'} student  {s['id']:20} code_bytes={len(code.strip()):6d} "
              f"err={r['error']} | {_fmt(r)}")

    # 2. verifier (must return parseable graded scores)
    r = B.chat(models["verifier"], verifier_sys, verifier_usr,
               timeout=run_cfg.get("request_timeout_s", 1800), retries=1)
    graded = G._parse_graded(B.strip_thinking(r["text"]))
    vgood = r["error"] is None and all(v["score"] is not None for v in graded.values())
    ok = ok and vgood
    total_cost += (r.get("cost") or 0) or 0
    scores = {k[:2]: v["score"] for k, v in graded.items()}
    print(f"  {'OK ' if vgood else 'FAIL'} verifier {models['verifier']['id']:20} "
          f"scores={scores} err={r['error']} | {_fmt(r)}")

    # 3. H5 solver (from gate config; must emit non-empty code)
    bundle = G._solver_bundle(run_cfg)
    if bundle:
        scfg, ssys, susr = bundle
        r = B.chat(scfg, ssys, susr.replace("{STATEMENT}", seed_stmt),
                   timeout=run_cfg.get("request_timeout_s", 1800), retries=1)
        code = B.extract_code(B.strip_thinking(r["text"]))
        sgood = r["error"] is None and bool(code.strip())
        ok = ok and sgood
        total_cost += (r.get("cost") or 0) or 0
        print(f"  {'OK ' if sgood else 'FAIL'} solver   {scfg.get('id'):20} code_bytes={len(code.strip()):6d} "
              f"err={r['error']} | {_fmt(r)}")
    else:
        print("  --  solver   (H5 disabled in run_config)")

    print(f"\n[smoke] total cost this run: ${round(total_cost, 6)}")
    print(f"[smoke] {'ALL MODELS OK -- safe to run the full family' if ok else 'FAILURES ABOVE -- do NOT run the full family'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
