#!/usr/bin/env python3
"""Realistic baseline for family 12 / criterion 3 (empty budget, B=0).

A solution that does NOT apply the arithmetic shortcut (B=0, positive costs -> no
affordable non-empty selection) and instead searches subsets for an affordable one.
Full include/exclude enumeration, O(2^n); since every non-empty subset costs > 0 = B it
never succeeds and explores the whole tree -> TLE at scale. The reference is O(1).
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    cost = []
    for _ in range(n):
        c = int(data[idx]); idx += 2
        cost.append(c)

    found = [False]

    def rec(i, taken_any, total):
        if found[0]:
            return
        if i == n:
            if taken_any and total <= B:
                found[0] = True
            return
        rec(i + 1, taken_any, total)                    # exclude
        rec(i + 1, True, total + cost[i])               # include

    rec(0, False, 0)

    print("YES" if found[0] else "NO")


main()
