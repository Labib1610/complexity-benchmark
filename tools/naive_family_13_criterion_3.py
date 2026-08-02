#!/usr/bin/env python3
"""Realistic baseline for family 13 / criterion 3 (odd total, infeasible).

A solution that does NOT apply the parity shortcut and instead searches subsets for an
equal split (a subset S with 2*sum(S) == total). Full include/exclude enumeration,
O(2^n); with an odd total, 2*sum can never equal the odd total, so it explores the whole
tree -> TLE at scale. The reference is O(n) (sum + parity).
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]
    total = sum(d)

    found = [False]

    def rec(i, s):
        if found[0]:
            return
        if i == n:
            if 2 * s == total:
                found[0] = True
            return
        rec(i + 1, s + d[i])                    # include
        rec(i + 1, s)                           # exclude

    rec(0, 0)
    print("YES" if found[0] else "NO")


main()
