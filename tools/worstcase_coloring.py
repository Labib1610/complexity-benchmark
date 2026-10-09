#!/usr/bin/env python3
"""Worst-case (phase-transition) tier for family 01 — 3-colouring.

Motivation (audit P2/P3): normal gradeable NPC tests are capped by the gradeable ceiling — the
reference must solve a case to make its answer key, so cases can never be hard for a competent
solver. This tier escapes that ceiling for YES-instances: it emits **planted, near-threshold
3-colourable graphs** whose answer is YES *by construction* (the planted partition is a valid
colouring), so grading needs only to VERIFY the model's colouring — no reference solve, no
feasibility recompute. That makes arbitrarily large / hard instances gradeable, and empirically these
near-threshold instances (ratio ~2.3, n>=800) defeat even a strong MRV+forward-checking solver
(measured: gpt-oss-120b 100% at n<=200, 0% at n>=800).

Usage:
  python tools/worstcase_coloring.py --gen --n 800 --ratio 2.3 --seed 1 > case.in
  python tools/worstcase_coloring.py --grade case.in < solution_stdout.txt   # prints PASS/FAIL
"""
import argparse
import random
import sys


def planted_3col(n: int, ratio: float, seed: int) -> str:
    """Planted 3-colourable graph: partition vertices into 3 classes, add edges only ACROSS classes
    at target m = ratio*n. Guaranteed 3-colourable (the partition is a valid colouring). Near
    ratio~2.3 (the 3-colouring threshold) the planted colouring is hidden among many near-solutions,
    so it is the hardest colourable regime."""
    rng = random.Random(seed * 1_000_003 + 11)
    part = [rng.randint(0, 2) for _ in range(n)]
    m_target = int(ratio * n)
    edges = set()
    tries = 0
    while len(edges) < m_target and tries < 60 * m_target + 2000:
        tries += 1
        u = rng.randint(0, n - 1); v = rng.randint(0, n - 1)
        if part[u] == part[v]:
            continue
        e = (u, v) if u < v else (v, u)
        edges.add(e)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u + 1} {v + 1}" for (u, v) in sorted(edges)]
    return "\n".join(lines) + "\n"


def grade(input_text: str, output_text: str):
    """WITNESS-ONLY grading. Every instance in this tier is 3-colourable by construction, so:
      - a proper 3-colouring of all n vertices  -> PASS  (the colouring proves YES; no recompute),
      - "NO", a malformed/incomplete colouring, or any conflict -> FAIL.
    O(n + m); works at any size."""
    d = input_text.split()
    n = int(d[0]); m = int(d[1])
    adj_pairs = [(int(d[2 + 2 * i]), int(d[3 + 2 * i])) for i in range(m)]

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    if toks[0].upper() == "NO":
        return False, "reported NO but the graph is 3-colourable (planted)"
    # accept an optional leading YES
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try:
        col = [int(x) for x in nums]
    except ValueError:
        return False, "non-integer colour in output"
    if len(col) != n:
        return False, f"expected {n} colours, got {len(col)}"
    if any(c < 1 or c > 3 for c in col):
        return False, "colours must be in {1,2,3}"
    for u, v in adj_pairs:
        if col[u - 1] == col[v - 1]:
            return False, f"vertices {u} and {v} share colour {col[u - 1]}"
    return True, "valid 3-colouring"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true")
    ap.add_argument("--grade", metavar="INPUT_FILE")
    ap.add_argument("--n", type=int, default=800)
    ap.add_argument("--ratio", type=float, default=2.3)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    if args.gen:
        sys.stdout.write(planted_3col(args.n, args.ratio, args.seed))
    elif args.grade:
        inp = open(args.grade).read()
        out = sys.stdin.read()
        ok, msg = grade(inp, out)
        print("PASS" if ok else "FAIL", "--", msg)
        sys.exit(0 if ok else 1)
    else:
        ap.error("use --gen or --grade")


if __name__ == "__main__":
    main()
