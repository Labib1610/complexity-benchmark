#!/usr/bin/env python3
"""Worst-case (witness-graded, TLE-inducing) probe for family 05 — 3-D matching.
Mirrors the family-01 colouring probe. For each model: read the seed statement, ask it to solve, then
grade on two tiers (all YES by construction; grading = verify the matching, O(k), no reference solve):
  - SEED tier  : small k (easy; sanity that the model solves the base task)
  - WORST tier : k>=60 near the 3DM threshold -> finding the matching needs search -> TLE.
Run from your terminal (API calls, ~6 generations):

    cd complexity-benchmark
    nohup python threedm_worstcase_probe.py > threedm_worstcase.log 2>&1 &
    tail -f threedm_worstcase.log
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "agentic/tools"))
sys.path.insert(0, str(ROOT / "tools"))
import backends as B
import worstcase_3dm as M

STATEMENT = (ROOT / "dataset/family_05_three_dim_matching/criterion_1_npc/statement.md").read_text()

# SEED: small, easy region (sanity that the base task is solvable). WORST: high-ratio (>=6) regime
# where the branching factor explodes -> every current solver TLEs though a planted witness exists.
SEED = [M.plant(k, r, s) for (k, r, s) in
        [(8, 3, 11), (12, 3, 12), (15, 3, 13), (18, 3, 14),
         (20, 3, 15), (22, 3, 16), (20, 4, 17), (22, 4, 18)]]
WORST = [M.plant(k, r, s) for (k, r, s) in
         [(100, 6.0, 21), (100, 7.0, 22), (120, 6.0, 23), (120, 8.0, 24),
          (150, 6.0, 25), (150, 8.0, 26), (200, 6.0, 27), (200, 8.0, 28)]]
LIM = 2.0


def grade_tier(sol_path, instances):
    npass = 0
    for inp in instances:
        try:
            out = subprocess.run([sys.executable, str(sol_path)], input=inp,
                                 capture_output=True, text=True, timeout=LIM).stdout
            ok, _ = M.grade(inp, out)
            npass += bool(ok)
        except subprocess.TimeoutExpired:
            pass
    return npass, len(instances)


def main():
    models = B.load_models()
    panel = [s for s in models["students"] if s.get("enabled", True)] + \
            models.get("frontier_evaluators", [])
    sys_t = (B.PROMPTS_DIR / "student_system.md").read_text()
    usr_t = (B.PROMPTS_DIR / "student_user_template.md").read_text()
    outdir = ROOT / "agentic/attempts/family_05/worstcase_probe"
    print(f"3-D MATCHING WORST-CASE PROBE | {len(panel)} models | "
          f"seed={len(SEED)} worst={len(WORST)} | limit {LIM}s\n", flush=True)
    print(f"{'model':<26}{'SEED tier':>12}{'WORST tier':>12}", flush=True)
    print("-" * 50, flush=True)
    for mdl in panel:
        d = outdir / mdl["id"]; d.mkdir(parents=True, exist_ok=True)
        sol = d / "solution.py"
        if not sol.exists():
            resp = B.chat(mdl, sys_t, usr_t.replace("{STATEMENT}", STATEMENT),
                          timeout=600, retries=2)
            sol.write_text(B.extract_code(B.strip_thinking(resp["text"])))
        sp, st = grade_tier(sol, SEED)
        wp, wt = grade_tier(sol, WORST)
        print(f"{mdl['id']:<26}{f'{100*sp//st}% ({sp}/{st})':>12}"
              f"{f'{100*wp//wt}% ({wp}/{wt})':>12}", flush=True)
    print("\nWORST low => 3DM near-threshold forces search -> TLE (the SOTA-resistant tier).\n"
          "SEED should stay high (base task is easy at small k).", flush=True)


if __name__ == "__main__":
    main()
