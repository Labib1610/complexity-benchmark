#!/usr/bin/env python3
"""Complexity probe: does the GROUND-TRUTH reference actually behave like its class?

Sweeps input size (small -> large, and beyond the statement bound) and measures how long
`reference.py` takes on each. Pure execution -- no LLM, no API.

Expected (the scientific check the supervisor asked for):
  * P / INFEASIBLE references  -> stay fast at every size (polynomial).
  * NP-complete references      -> fast on small inputs, but time must blow up on large
                                   inputs (exponential). If an NPC reference stays fast even
                                   at large sizes, STOP: the reference may be a heuristic, the
                                   instances may be too small, or the problem is not really NPC.

  python tools/complexity_probe.py --family 01 [--criterion 1] [--timeout 60] [--max-n N]
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve()
AGENTIC = HERE.parents[1]
ROOT = HERE.parents[2]
for _p in (str(ROOT), str(AGENTIC)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from harness.runner import run_solution   # noqa: E402

SEEDS = AGENTIC / "seeds"
CRITS = ["criterion_1_npc", "criterion_2_p", "criterion_3_infeasible"]


def _class_of(seed_crit_dir: Path) -> str:
    meta = (seed_crit_dir / "meta.yaml").read_text() if (seed_crit_dir / "meta.yaml").exists() else ""
    for line in meta.splitlines():
        if line.strip().lower().startswith("class:"):
            return line.split(":", 1)[1].strip().upper()
    return "?"


def _size_sweep(klass, max_n):
    """Sizes to probe per class. NPC pushes past the bound to find the blow-up point; P and
    INFEASIBLE sweep large sizes to confirm they stay fast."""
    if klass == "NPC":
        base = [8, 12, 16, 20, 24, 28, 32, 36, 40, 50, 64, 80, 100, 150, 200, 300, 500]
    elif klass == "P":
        base = [100, 1000, 5000, 20000, 50000, 100000, 200000]
    else:  # INFEASIBLE
        base = [50, 200, 500, 1000, 2000, 4000]
    return [n for n in base if n <= max_n]


def _gen(gen_path, criterion, n, seed):
    """Generate one input of size n via the family generator (hard mode for NPC)."""
    m = max(1, int(2.35 * n))          # generator ignores --m for c1 (uses its own ratio)
    cmd = [sys.executable, str(gen_path), "--criterion", str(criterion),
           "--n", str(n), "--m", str(m), "--seed", str(seed), "--mode", "hard"]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=120, text=True)
        return r.stdout if r.returncode == 0 and r.stdout.strip() else None
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    ap.add_argument("--timeout", type=int, default=60, help="per-run reference timeout (s)")
    ap.add_argument("--max-n", type=int, default=500, help="largest size to probe")
    ap.add_argument("--seeds", type=int, default=3, help="inputs per size (report the max time)")
    args = ap.parse_args()

    slug = sorted(SEEDS.glob(f"family_{args.family}_*"))[0].name
    gen_path = ROOT / "tools" / f"gen_family_{args.family}.py"
    if not gen_path.exists():
        raise SystemExit(f"no generator {gen_path}")
    todo = ([c for c in CRITS if c.startswith(f"criterion_{args.criterion}_")]
            if args.criterion else CRITS)

    for cd in todo:
        cdir = SEEDS / slug / cd
        klass = _class_of(cdir)
        ref = cdir / "reference.py"
        mem = 256
        cnum = int(cd.split("_")[1])
        print(f"\n{'='*70}\n{cd}   class={klass}\n{'='*70}")
        print(f"{'n':>8}{'ref_time':>12}{'status':>14}")
        blew_up = False
        max_ok_n = 0
        for n in _size_sweep(klass, args.max_n):
            worst = 0.0
            status = "OK"
            for s in range(args.seeds):
                inp = _gen(gen_path, cnum, n, 100 + s)
                if inp is None:
                    status = "gen-failed"
                    break
                rr = run_solution(ref, inp, args.timeout, mem)
                if rr.status == "TLE":
                    status = f"TIMEOUT>{args.timeout}s"; worst = args.timeout; break
                if rr.status == "RUNTIME_ERROR":
                    status = "CRASH"; break
                worst = max(worst, rr.elapsed_s)
            tstr = f"{worst:.2f}s" if status == "OK" else ""
            print(f"{n:>8}{tstr:>12}{status:>14}")
            if status.startswith("TIMEOUT"):
                blew_up = True
                break
            if status == "OK":
                max_ok_n = n
        # verdict
        print("-" * 36)
        if klass == "NPC":
            if blew_up:
                print(f"VERDICT: exponential blow-up CONFIRMED (reference times out by n>{max_ok_n}). "
                      "Genuinely NP-complete.")
            else:
                print(f"VERDICT: *** NO BLOW-UP up to n={max_ok_n} in {args.timeout}s *** -- "
                      "reference stays fast on large NPC inputs. INVESTIGATE: heuristic reference, "
                      "instances too small, or not truly NP-complete.")
        else:
            print(f"VERDICT: stayed fast up to n={max_ok_n} (expected for {klass}).")


if __name__ == "__main__":
    main()
