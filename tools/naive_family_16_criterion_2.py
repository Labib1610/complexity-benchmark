#!/usr/bin/env python3
"""Realistic baseline for family 16 / criterion 2 (two-machine flow-shop).

A solution that does NOT know Johnson's rule and instead tries EVERY ordering of the
jobs, simulating the two-machine pipeline for each and keeping the minimum makespan.
This is O(j! * j) and dies by j~11, while Johnson's rule is O(j log j). Output matches
(both find the optimal makespan) on the small instances where it finishes.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    jobs = []
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        jobs.append((p1, p2))

    best = float("inf")
    for order in itertools.permutations(range(j)):
        t1 = 0; t2 = 0
        for k in order:
            p1, p2 = jobs[k]
            t1 += p1
            t2 = (t2 if t2 > t1 else t1) + p2
        if t2 < best:
            best = t2
    print(best)


main()
