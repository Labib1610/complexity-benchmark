#!/usr/bin/env python3
"""Run the student panel's saved solutions against the family-01 worst-case (phase-transition) tier
and report pass rate. Witness-only grading (worstcase_coloring.grade) -- no reference solve.

Usage:
  python tools/run_worstcase.py [--limit 2.0] [--version v000]
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import worstcase_coloring as WC

WC_DIR = ROOT / "dataset/family_01_graph_coloring/criterion_1_npc/worstcase"
ATTEMPTS = ROOT / "agentic/attempts/family_01/criterion_1_npc"
STUDENTS = ["gpt-oss-120b", "deepseek-v4-flash", "qwen3-coder", "glm-5"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=float, default=2.0, help="per-case wall-clock limit (s)")
    ap.add_argument("--version", default="v000", help="which saved solution version to use")
    args = ap.parse_args()

    cases = sorted(WC_DIR.glob("*.in"))
    inputs = {c.stem: c.read_text() for c in cases}
    print(f"worst-case tier: {len(cases)} instances, limit={args.limit}s, solution={args.version}\n")

    header = f"{'model':<20}" + "".join(f"{c.stem:>5}" for c in cases) + f"{'PASS%':>8}"
    print(header); print("-" * len(header))
    for mdl in STUDENTS:
        sol = ATTEMPTS / args.version / mdl / "solution.py"
        if not sol.exists():
            print(f"{mdl:<20}  (no saved {args.version} solution)")
            continue
        cells = []; npass = 0
        for c in cases:
            inp = inputs[c.stem]
            t0 = time.monotonic()
            try:
                out = subprocess.run([sys.executable, str(sol)], input=inp,
                                     capture_output=True, text=True, timeout=args.limit).stdout
                dt = time.monotonic() - t0
                ok, _ = WC.grade(inp, out)
                mark = "Y" if ok else "."
                if ok:
                    npass += 1
            except subprocess.TimeoutExpired:
                mark = "T"   # TLE
            cells.append(mark)
        pct = 100 * npass // len(cases)
        print(f"{mdl:<20}" + "".join(f"{m:>5}" for m in cells) + f"{pct:>7}%")
    print("\nlegend: Y=solved  .=wrong/incomplete  T=TLE (>limit)")


if __name__ == "__main__":
    main()
