#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 04 (subset sum / budget).

Usage:
    python tools/gen_family_04.py --criterion 1 --n 34 --seed 4 --reach no
    python tools/gen_family_04.py --criterion 2 --n 1000 --seed 3 --reach yes
    python tools/gen_family_04.py --criterion 3 --n 1000 --seed 5

Format for all three: line 1 = n, line 2 = n costs, line 3 = target T.
"""
import argparse
import random


def _emit(n, costs, T):
    return f"{n}\n{' '.join(map(str, costs))}\n{T}\n"


# --- criterion 1: large values (rules out pseudo-poly DP), meet-in-the-middle ---
def gen_subsetsum_large(n, seed, reachable=None):
    """Values up to 1e9, target up to 4e10.

    reachable=False -> hardest NO: all-even values and an ODD target near sum/2, so
        no subset can reach it (parity), and pruning by "running sum > T" barely helps
        because T sits at the middle -> naive include/exclude explores ~2^n.
    reachable=True  -> plant a random non-empty subset and set T to its sum (YES).
    reachable=None  -> random values, random T in [0, sum].
    """
    rng = random.Random(seed * 1_000_003 + 11)
    if reachable is False:
        costs = [2 * rng.randint(1, 499_999_999) for _ in range(n)]   # even, <= ~1e9
        total = sum(costs)
        T = (total // 2) | 1                                          # odd -> unreachable
    elif reachable is True:
        costs = [rng.randint(1, 1_000_000_000) for _ in range(n)]
        k = rng.randint(1, n)
        subset = rng.sample(range(n), k)
        T = sum(costs[i] for i in subset)
    else:
        costs = [rng.randint(1, 1_000_000_000) for _ in range(n)]
        T = rng.randint(0, sum(costs))
    return _emit(n, costs, T)


# --- criterion 2: small values/target (DP is genuinely polynomial) --------------
def gen_subsetsum_small(n, seed, reachable=True):
    """Costs in [1,100], target in [0,500].

    reachable=True  -> plant a subset whose sum is a valid target <= 500 (YES).
    reachable=False -> SMALL even costs and an ODD target -> unreachable (NO). Small
        values are deliberate: the "running sum > T" pruning a naive search uses is
        useless when many items fit under T, so the pruned subset search still
        explores exponentially, whereas the O(n*T) DP stays polynomial.
    """
    rng = random.Random(seed * 2_000_003 + 7)
    if reachable is False:
        costs = [2 * rng.randint(1, 4) for _ in range(n)]            # even, in [2,8]
        T = 2 * rng.randint(1, 249) + 1                               # odd, in [3,499]
        return _emit(n, costs, T)
    # reachable=True: build costs, then plant a subset summing to a target <= 500
    costs = [rng.randint(1, 100) for _ in range(n)]
    order = list(range(n)); rng.shuffle(order)
    target_cap = rng.randint(50, 500)
    s = 0
    for i in order:
        if s + costs[i] <= target_cap:
            s += costs[i]
        if s >= target_cap - 1:
            break
    T = s                                                            # exactly a subset sum
    return _emit(n, costs, T)


# --- criterion 3: negative target (trivially infeasible) ------------------------
def gen_negative_target(n, seed):
    rng = random.Random(seed * 3_000_003 + 5)
    costs = [rng.randint(1, 1_000_000_000) for _ in range(n)]
    T = -rng.randint(1, 1_000_000_000)
    return _emit(n, costs, T)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--reach", default="")           # yes / no / (blank=random)
    args = p.parse_args()

    if args.criterion == 1:
        r = {"yes": True, "no": False, "": None}[args.reach]
        out = gen_subsetsum_large(args.n, args.seed, reachable=r)
    elif args.criterion == 2:
        r = {"yes": True, "no": False, "": True}[args.reach]
        out = gen_subsetsum_small(args.n, args.seed, reachable=r)
    else:
        out = gen_negative_target(args.n, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
