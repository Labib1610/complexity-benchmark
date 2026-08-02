#!/usr/bin/env python3
"""SECONDARY baseline for family 10 / criterion 2: the CORRECT tree DP but implemented
RECURSIVELY. It gives the right answer on shallow trees (star, balanced) but hits
Python's recursion limit / C-stack on a deep path (n ~ 2e5) and dies with a
RuntimeError / crash -- a distinct, realistic failure mode from a model that recognised
the structure but did not linearise the traversal. The reference avoids it with an
explicit post-order stack.
"""
import sys


def main():
    sys.setrecursionlimit(10000)               # a typical, insufficient bump
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    children = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        c = int(data[idx]); p = int(data[idx + 1]); idx += 2
        children[p].append(c)

    INF = float("inf")

    def dp(v):
        # returns (has_sensor, covered_by_child, needs_parent)
        if not children[v]:
            return (1, INF, 0)
        s0 = 1; base = 0; best_delta = INF; has0 = False
        for c in children[v]:
            a, b, d = dp(c)
            s0 += min(a, b, d)
            base += min(a, b)
            if a <= b:
                has0 = True
            else:
                best_delta = min(best_delta, a - b)
        d1 = base if has0 else base + best_delta
        return (s0, d1, base)

    a, b, _ = dp(1)
    print(min(a, b))


main()
