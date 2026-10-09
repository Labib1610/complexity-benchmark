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


# --- criterion 3: INFEASIBLE deadline with a checkable certificate ---------------
def gen_infeasible_deadline(j, seed, kind="job"):
    """Every instance cannot meet the deadline T, for a checkable reason (audit B5):
      kind='job'   -> one job's own two operations sum to more than T (it is sequential, so it
                      alone finishes after T). Certificate: `JOB i`. Machine loads stay <= T.
      kind='load1' -> the total machine-1 work exceeds T (machine 1 runs serially). `LOAD 1`.
      kind='load2' -> the total machine-2 work exceeds T. `LOAD 2`.
    """
    rng = random.Random(seed * 3_000_003 + 5)
    if kind == "job":
        T = max(2000, 4 * j)
        big = int(0.6 * T)                              # big job: big+big = 1.2T > T, each <= T
        pos = rng.randint(0, j - 1)
        jobs = [(1, 1) for _ in range(j)]
        jobs[pos] = (big, big)                          # sum(p1)=big+(j-1) <= T since j-1 < 0.4T
    elif kind == "load1":
        a = 100
        T = max(300, (j * a) // 2)                      # sum(p1)=j*a=~2T > T; each p1+p2=a+1 <= T
        jobs = [(a, 1) for _ in range(j)]
    else:  # load2
        a = 100
        T = max(300, (j * a) // 2)
        jobs = [(1, a) for _ in range(j)]
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
    p.add_argument("--kind", default="job")   # criterion 3: job|load1|load2
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_jobshop(args.j, args.m, args.seed)
    elif args.criterion == 2:
        out = gen_flowshop(args.j, args.seed, order=args.order)
    else:
        out = gen_infeasible_deadline(args.j, args.seed, kind=args.kind)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
