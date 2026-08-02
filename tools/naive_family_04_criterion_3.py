#!/usr/bin/env python3
"""Realistic baseline for family 04 / criterion 3 (negative target, infeasible).

A solution that does NOT notice that a negative target is trivially unreachable and
instead searches subsets for one summing to T. Full include/exclude enumeration
(no target-sign shortcut), O(2^n) -> TLEs at large n. Correct on the small anchors.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    costs = [int(data[1 + i]) for i in range(n)]
    T = int(data[1 + n])
    sys.setrecursionlimit(1 << 20)
    found = [False]

    def rec(i, s):
        if found[0]:
            return
        if i == n:
            if s == T:
                found[0] = True
            return
        rec(i + 1, s + costs[i])       # include (no sign-based pruning)
        rec(i + 1, s)                  # exclude

    rec(0, 0)
    print("YES" if found[0] else "NO")


main()
