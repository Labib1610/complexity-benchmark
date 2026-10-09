#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 06 (bin packing).

REBUILT per the audit (MD files/COMPLEXITY_BENCHMARK_AUDIT.md), blocker B4: the family now uses one
INDIVISIBLE OPTIMISATION contract across conditions -- minimise the number of fixed-capacity
containers to load all items, reporting the count and one assignment. Previously criterion 1 was an
indivisible feasibility decision (with a k budget) and criterion 2 was DIVISIBLE (fractional) bin
packing without k -- a different task, output, and schema. Now:

  * Criterion 1 (NPC): general min-bins (items cluster near C/2 -> a hard perfect-packing search).
  * Criterion 2 (P):   every item weighs MORE THAN C/3, so at most two fit per container; the optimum
                       is a two-pointer greedy (pair the heaviest with the lightest that still fits).
  * Criterion 3 (INFEASIBLE): an item heavier than C (fits in no container) -- certificate arm.

Unified schema (all three): line 1 = "n C", line 2 = n item weights.

Usage:
    python tools/gen_family_06.py --criterion 1 --k 12 --C 1000 --seed 4
    python tools/gen_family_06.py --criterion 2 --n 100000 --C 1000 --seed 3
    python tools/gen_family_06.py --criterion 3 --n 100000 --C 1000 --seed 5 --at high
"""
import argparse
import random


# --- criterion 1: hard min-bins (perfect-packing pairs near C/2) ----------------
def gen_binpack_hard(k, C, seed):
    """n = 2k items forming k complementary pairs (x, C-x) with x near C/2, total exactly k*C, so
    the minimum is exactly k containers (a perfect packing). Weights cluster near C/2 with
    duplicates, so a search without symmetry breaking explores astronomically many equivalent
    orderings before finding the perfect packing."""
    rng = random.Random(seed * 1_000_003 + 11)
    lo = max(1, C // 2 - C // 10)
    hi = max(lo, C // 2)
    items = []
    for _ in range(k):
        x = rng.randint(lo, hi)
        items.append(x)
        items.append(C - x)
    rng.shuffle(items)
    n = len(items)
    return f"{n} {C}\n{' '.join(map(str, items))}\n"


# --- criterion 2: every item > C/3 (at most two per container) ------------------
def gen_thirds(n, C, seed):
    """n items each strictly greater than C/3 (and <= C), so no container holds more than two. The
    optimum is a two-pointer greedy; a general bin-packing search is unnecessary but a model must
    recognise the structure. Weights are spread across (C/3, C] so both 'pair' and 'alone' happen."""
    rng = random.Random(seed * 2_000_003 + 7)
    lo = C // 3 + 1
    w = [rng.randint(lo, C) for _ in range(n)]
    return f"{n} {C}\n{' '.join(map(str, w))}\n"


# --- criterion 3: an oversized item ---------------------------------------------
def gen_oversized(n, C, seed, at="high"):
    """n items, capacity C, with one item heavier than C at a high (or given) index; every other
    item fits. The answer is the smallest oversized index."""
    rng = random.Random(seed * 3_000_003 + 5)
    if at == "high":
        at_idx = n
    elif at == "low":
        at_idx = 1
    else:
        at_idx = int(at)
    w = []
    lo = max(1, C // 2 - C // 10)
    for i in range(1, n + 1):
        if i == at_idx:
            w.append(C + rng.randint(1, C))
        else:
            w.append(rng.randint(lo, C // 2 if C >= 2 else 1))
    return f"{n} {C}\n{' '.join(map(str, w))}\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, default=0)          # criterion 2/3
    p.add_argument("--k", type=int, default=0)          # criterion 1: number of pairs (n = 2k)
    p.add_argument("--C", type=int, default=1000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--at", default="high")               # criterion 3
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_binpack_hard(args.k, args.C, args.seed)
    elif args.criterion == 2:
        out = gen_thirds(args.n, args.C, args.seed)
    else:
        out = gen_oversized(args.n, args.C, args.seed, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
