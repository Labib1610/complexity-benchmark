#!/usr/bin/env python3
"""Corner-case robustness audit of the reference solutions (supervisor request).

Feeds a battery of edge-case inputs -- empty graphs, complete graphs, duplicates,
self-loops, all-zeros, all-ones, negatives, out-of-range vertices, degenerate cycles --
through each criterion's reference.py and reports whether it handles them cleanly (OK),
crashes (RUNTIME_ERROR), produces nothing (EMPTY), or hangs (HANG). The key defect to catch
is a HANG (infinite loop); a clean crash on genuinely out-of-spec input is acceptable, a
correct answer on valid corner cases is required.

Standalone: depends only on the harness (no model stack / litellm).

  python tools/corner_audit.py --family 01 [--add]
"""
import argparse
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
AGENTIC = HERE.parents[1]
ROOT = HERE.parents[2]
for _p in (str(ROOT), str(AGENTIC)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from harness.runner import run_solution   # noqa: E402

SEEDS = AGENTIC / "seeds"
TESTS = AGENTIC / "tests"
CRITS = ["criterion_1_npc", "criterion_2_p", "criterion_3_infeasible"]
TIMEOUT_S = 15          # anything slower than this on a tiny input is a HANG
MEM_MB = 256


def _edges(n, pairs):
    return f"{n} {len(pairs)}\n" + "".join(f"{u} {v}\n" for u, v in pairs)


def cases():
    """(name, input_text, category) -- graph format shared by all 3 family_01 criteria."""
    def K(n):
        return [(u, v) for u in range(1, n + 1) for v in range(u + 1, n + 1)]
    return [
        # valid, well-formed corner cases (reference MUST handle correctly) --------------
        ("n=1, no conflicts",         "1 0\n",                       "valid/minimal"),
        ("n=3, empty graph",          "3 0\n",                       "valid/minimal"),
        ("triangle K3",               _edges(3, K(3)),               "valid/structure"),
        ("K4 (not 3-colorable)",      _edges(4, K(4)),               "valid/structure"),
        ("K5 (not 4-colorable)",      _edges(5, K(5)),               "valid/structure"),
        ("odd cycle C5",              _edges(5, [(1,2),(2,3),(3,4),(4,5),(5,1)]), "valid/structure"),
        ("path P4 (bipartite)",       _edges(4, [(1,2),(2,3),(3,4)]),"valid/structure"),
        ("star (1 hub, 4 leaves)",    _edges(5, [(1,2),(1,3),(1,4),(1,5)]), "valid/structure"),
        ("duplicate edges (all 1-2)", "3 3\n1 2\n1 2\n1 2\n",        "degen/duplicates"),
        # the supervisor's named cases: all-zeros / all-ones / negatives -----------------
        ("ALL ZEROS (0 0 edges)",     "3 3\n0 0\n0 0\n0 0\n",        "malformed/all-zeros"),
        ("n=0, m=0",                  "0 0\n",                       "malformed/all-zeros"),
        ("ALL ONES (self-loops 1-1)", "3 3\n1 1\n1 1\n1 1\n",        "malformed/all-ones"),
        ("NEGATIVE vertices",         "3 1\n-1 -2\n",                "malformed/negative"),
        ("negative n",                "-3 0\n",                      "malformed/negative"),
        ("vertex > n (out of range)", "3 1\n1 5\n",                  "malformed/out-of-range"),
        ("m says 3, only 1 edge",     "3 3\n1 2\n",                  "malformed/truncated"),
        ("empty input",               "",                            "malformed/empty"),
        ("garbage tokens",            "3 1\nhello world\n",          "malformed/garbage"),
    ]


def _run(ref_path, inp):
    rr = run_solution(ref_path, inp, TIMEOUT_S, MEM_MB)
    if rr.status == "TLE":
        return "HANG", ""
    if rr.status == "RUNTIME_ERROR":
        tail = (rr.stderr or "").strip().splitlines()
        return "CRASH", (tail[-1][:60] if tail else "")
    out = (rr.stdout or "").strip()
    return ("OK" if out else "EMPTY"), out[:38].replace("\n", " ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--add", action="store_true",
                    help="add valid corner cases (reference runs OK) to the corner tier")
    args = ap.parse_args()

    slug_dirs = sorted(SEEDS.glob(f"family_{args.family}_*"))
    if not slug_dirs:
        raise SystemExit(f"no seeds dir for family {args.family}")
    slug = slug_dirs[0].name
    refs = {cd: (SEEDS / slug / cd / "reference.py") for cd in CRITS}

    print(f"\n{'='*104}\nCORNER-CASE AUDIT  family_{args.family}  ({slug})\n{'='*104}")
    print(f"{'case':<30}{'category':<24}" + "".join(f"{cd.split('_')[1]:>10}" for cd in CRITS)
          + "   (c1=NPC c2=P c3=INFEAS)")
    hangs, added, details = [], 0, []
    for name, inp, cat in cases():
        row = f"{name:<30}{cat:<24}"
        for cd in CRITS:
            if not refs[cd].exists():
                row += f"{'--':>10}"; continue
            status, out = _run(refs[cd], inp)
            row += f"{status:>10}"
            details.append((name, cd, status, out))
            if status == "HANG":
                hangs.append((cd, name))
            if args.add and status == "OK" and cat.startswith(("valid", "degen")):
                store = TESTS / f"family_{args.family}" / cd
                store.mkdir(parents=True, exist_ok=True)
                h = hashlib.sha1((cd + inp).encode()).hexdigest()[:8]
                rr = run_solution(refs[cd], inp, TIMEOUT_S, MEM_MB)
                (store / f"corner_{h}.in").write_text(inp)
                (store / f"corner_{h}.out").write_text(rr.stdout)
                added += 1
        print(row)

    print("\nLegend: OK=ran & output | EMPTY=ran, no output | "
          "CRASH=nonzero exit (acceptable on malformed) | HANG=timed out (BUG)")
    # show the actual outputs on the valid structural cases (correctness spot-check)
    print("\nOutputs on valid structural cases (spot-check correctness):")
    for name, cd, status, out in details:
        if status == "OK" and any(name == n for n, _i, c in cases() if c.startswith(("valid", "degen"))):
            print(f"   {name:<28} {cd.split('_')[1]:<3} -> {out!r}")
    if hangs:
        print(f"\n*** HANGS (infinite-loop bug -- must fix): {hangs}")
    else:
        print("\nNo hangs: every reference terminates on all corner cases (good).")
    if args.add:
        print(f"\nadded {added} valid corner case(s) to the corner tier.")


if __name__ == "__main__":
    main()
