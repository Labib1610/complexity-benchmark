#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 06 (bin packing).

Usage:
    python tools/gen_family_06.py --criterion 1 --k 10 --C 1000 --seed 4 --feasible yes
    python tools/gen_family_06.py --criterion 2 --n 200000 --seed 3
    python tools/gen_family_06.py --criterion 3 --n 200000 --seed 5 --at high
"""
import argparse
import random


# --- criterion 1: hard bin packing (perfect-packing + duplicates + symmetry) ---
def gen_binpack_hard(k, C, seed, feasible=True):
    """n = 2k items forming k complementary pairs (x, C-x) with x near C/2, total
    exactly k*C so a solution must pack every bin to the brim (a perfect packing).
    Weights cluster near C/2 with duplicates, so a search WITHOUT symmetry breaking
    explores astronomically many equivalent bin orderings.

    feasible=True  -> the k pairs do partition perfectly (YES).
    feasible=False -> perturb two items by +1/-1 so no perfect packing exists while the
        total stays k*C (a subtle NO that still forces exhaustive search).
    """
    rng = random.Random(seed * 1_000_003 + 11)
    lo = max(1, C // 2 - C // 10)
    hi = C // 2
    items = []
    for _ in range(k):
        x = rng.randint(lo, hi)
        items.append(x)
        items.append(C - x)
    if not feasible and k >= 2:
        # shift weight between two different bins' items so totals still sum to k*C
        # but the multiset no longer partitions into k bins of exactly C.
        items[0] += 1
        items[3] -= 1
    rng.shuffle(items)
    n = len(items)
    return f"{n} {k} {C}\n{' '.join(map(str, items))}\n"


# --- criterion 2: fractional bin packing (answer = ceil(sum/C)) -----------------
def gen_fractional(n, C, seed, exact=False):
    """n batches with LARGE absolute weights (up to 1e9), capacity C. When C is small
    relative to the weights, the answer ceil(sum/C) is enormous, so a naive bin-by-bin
    simulator that closes one container at a time does ~sum/C iterations and TLEs,
    while the reference is O(n) ceil division. exact=True -> total is an exact multiple
    of C (tests the ceil edge)."""
    rng = random.Random(seed * 2_000_003 + 7)
    w = [rng.randint(10 ** 8, 10 ** 9) for _ in range(n)]
    if exact:
        total = sum(w)
        w[-1] += (-total) % C            # round total up to a multiple of C
    return f"{n} {C}\n{' '.join(map(str, w))}\n"


# --- criterion 3: an oversized item ---------------------------------------------
def gen_oversized(n, C, seed, at="high"):
    """n items, capacity C, with an item heavier than C planted at a high (or given)
    index; every other item fits (weight <= C). The answer is the smallest oversized
    index. The non-oversized items are tight duplicates near C/2 so a packing search
    (the naive baseline) explores exponentially before reaching the oversized one."""
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
            w.append(C + rng.randint(1, C))      # oversized (> C, <= 2C bound)
        else:
            x = rng.randint(lo, C // 2)
            w.append(x)
    return f"{n} {C}\n{' '.join(map(str, w))}\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, default=0)          # criterion 2/3
    p.add_argument("--k", type=int, default=0)          # criterion 1 bins
    p.add_argument("--C", type=int, default=1000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--feasible", default="yes")          # criterion 1
    p.add_argument("--exact", action="store_true")       # criterion 2
    p.add_argument("--at", default="high")               # criterion 3
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_binpack_hard(args.k, args.C, args.seed,
                               feasible=(args.feasible.lower() in ("yes", "y", "1", "true")))
    elif args.criterion == 2:
        out = gen_fractional(args.n, args.C, args.seed, exact=args.exact)
    else:
        out = gen_oversized(args.n, args.C, args.seed, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
