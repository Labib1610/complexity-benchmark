#!/usr/bin/env python3
"""Realistic baseline for family 16 / criterion 1 (job-shop makespan).

The SAME Giffler-Thompson branch-and-bound as the reference, but with a WEAKER lower
bound: only the max machine remaining-work bound, without the per-job remaining-work
bound the reference also uses. This is a competent-but-not-expert solution (no
sophisticated bounding). On instances with many near-tied orderings the weaker pruning
explores far more of the tree. Same shape as the reference, so any gap is instance
structure, not asymptotics.
"""
import sys


def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); m = int(data[idx + 1]); idx += 2
    jobs = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        ops = []
        for _ in range(o):
            mc = int(data[idx]) - 1; du = int(data[idx + 1]); idx += 2
            ops.append((mc, du))
        jobs.append(ops)

    best = [float("inf")]

    def lower_bound(nextop, mfree):
        mrem = [0] * m
        for i in range(j):
            for kk in range(nextop[i], len(jobs[i])):
                mc, du = jobs[i][kk]
                mrem[mc] += du
        lb = 0
        for c in range(m):                 # ONLY the machine-load bound (weaker)
            v = mfree[c] + mrem[c]
            if v > lb:
                lb = v
        return lb

    def rec(nextop, mfree, jfree, cur_ms):
        if cur_ms >= best[0]:
            return
        sched = []
        for i in range(j):
            p = nextop[i]
            if p < len(jobs[i]):
                mc, du = jobs[i][p]
                est = mfree[mc] if mfree[mc] > jfree[i] else jfree[i]
                sched.append((i, mc, du, est, est + du))
        if not sched:
            if cur_ms < best[0]:
                best[0] = cur_ms
            return
        if lower_bound(nextop, mfree) >= best[0]:
            return
        cstar = min(s[4] for s in sched)
        mstar = next(s[1] for s in sched if s[4] == cstar)
        conflict = [s for s in sched if s[1] == mstar and s[3] < cstar]
        for (i, mc, du, est, ect) in conflict:
            nm = mfree[:]; nj = jfree[:]; nn = nextop[:]
            nm[mc] = ect; nj[i] = ect; nn[i] += 1
            rec(nn, nm, nj, cur_ms if cur_ms > ect else ect)

    rec([0] * j, [0] * m, [0] * j, 0)
    print(best[0])


main()
