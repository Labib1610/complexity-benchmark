#!/usr/bin/env python3
"""Realistic baseline for family 04 / criterion 1 (subset sum, large values).

Recursive include/exclude subset search, O(2^n), with the standard pruning a
competent model writes: never extend a partial group once its running sum would
exceed the target (all costs are positive). This is the natural solution when a
model does not think of meet-in-the-middle. On hard NO instances (target near
sum/2, parity-unreachable) the pruning barely helps and it explores ~2^n.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    costs = [int(data[1 + i]) for i in range(n)]
    T = int(data[1 + n])
    sys.setrecursionlimit(1 << 20)

    chosen = []
    ans = [None]

    def rec(i, s):
        if s == T:
            ans[0] = chosen.copy()
            return True
        if i == n or s > T:            # positive costs -> overshoot can be pruned
            return False
        # include item i (only if it does not overshoot)
        if s + costs[i] <= T:
            chosen.append(i + 1)
            if rec(i + 1, s + costs[i]):
                return True
            chosen.pop()
        # exclude item i
        return rec(i + 1, s)

    if rec(0, 0):
        print("YES")
        print(' '.join(map(str, ans[0])))
    else:
        print("NO")


main()
