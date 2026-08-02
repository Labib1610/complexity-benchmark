#!/usr/bin/env python3
"""Realistic baseline for family 16 / criterion 3 (impossible deadline).

A solution that does NOT check the max-p1 lower bound and instead tries to actually
schedule the jobs to meet the deadline -- enumerating every ordering and simulating the
pipeline, looking for one whose makespan is <= T. Since some job's p1 alone exceeds T,
no ordering works, so it explores all j! orderings -> TLE. Only then does it print NO.
The reference's O(j) max check is instant.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); T = int(data[idx + 1]); idx += 2
    jobs = []
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        jobs.append((p1, p2))

    feasible = False
    for order in itertools.permutations(range(j)):
        t1 = 0; t2 = 0
        for k in order:
            p1, p2 = jobs[k]
            t1 += p1
            t2 = (t2 if t2 > t1 else t1) + p2
        if t2 <= T:
            feasible = True
            break

    print("YES" if feasible else "NO")


main()
