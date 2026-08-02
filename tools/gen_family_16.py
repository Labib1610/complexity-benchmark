#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 16 (job-shop / flow-shop).

Usage:
    python tools/gen_family_16.py --criterion 1 --j 8 --m 3 --seed 4
    python tools/gen_family_16.py --criterion 2 --j 200000 --seed 3 --order random
    python tools/gen_family_16.py --criterion 3 --j 100000 --seed 5
"""
import argparse
import random


# --- criterion 1: job-shop (similar processing times -> many near-ties) ---------
def gen_jobshop(j, m, seed):
    """j jobs on m machines; each job visits all m machines in a random order with
    SIMILAR durations (all in a narrow band), so many orderings are near-tied and a
    branch-and-bound with a simple bound cannot prune. Total ops = j*m."""
    rng = random.Random(seed * 1_000_003 + 11)
    lines = [f"{j} {m}"]
    for _ in range(j):
        order = list(range(1, m + 1)); rng.shuffle(order)
        parts = [str(m)]
        for mc in order:
            parts.append(f"{mc} {rng.randint(4, 6)}")   # narrow band -> near-ties
        lines.append(" ".join(parts))
    return "\n".join(lines) + "\n"


# --- criterion 2: two-machine flow-shop -----------------------------------------
def gen_flowshop(j, seed, order="random"):
    """j jobs, each (p1, p2). order controls how the input is pre-sorted:
    sorted (ascending p1), reverse (descending p1), or random."""
    rng = random.Random(seed * 2_000_003 + 7)
    jobs = [(rng.randint(1, 1_000_000), rng.randint(1, 1_000_000)) for _ in range(j)]
    if order == "sorted":
        jobs.sort(key=lambda x: x[0])
    elif order == "reverse":
        jobs.sort(key=lambda x: -x[0])
    lines = [str(j)]
    lines += [f"{p1} {p2}" for (p1, p2) in jobs]
    return "\n".join(lines) + "\n"


# --- criterion 3: infeasible deadline (T < max p1) ------------------------------
def gen_infeasible_deadline(j, seed):
    rng = random.Random(seed * 3_000_003 + 5)
    jobs = [(rng.randint(1, 1000), rng.randint(1, 1000)) for _ in range(j)]
    # make one job's p1 clearly exceed the deadline
    big = rng.randint(0, j - 1)
    jobs[big] = (rng.randint(500000, 1000000), jobs[big][1])
    T = jobs[big][0] - 1                                # deadline below that job's p1
    lines = [f"{j} {T}"]
    lines += [f"{p1} {p2}" for (p1, p2) in jobs]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--j", type=int, required=True)
    p.add_argument("--m", type=int, default=3)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--order", default="random")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_jobshop(args.j, args.m, args.seed)
    elif args.criterion == 2:
        out = gen_flowshop(args.j, args.seed, order=args.order)
    else:
        out = gen_infeasible_deadline(args.j, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
