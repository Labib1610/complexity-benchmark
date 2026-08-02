#!/usr/bin/env python3
"""Realistic (correct but inefficient) baseline for family 02 / criterion 2 (2-SAT).

A competent model that does not know the linear implication-graph + SCC trick can
still write a correct greedy 2-SAT solver: fix variables in order, and after each
assignment propagate unit clauses to a fixpoint by re-scanning the whole clause
list. Each variable triggers at least one O(m) scan, so this is O(n*m) -- correct,
but times out at n, m ~ 1e5 / 2e5 while the O(n+m) SCC reference is instant.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    clauses = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        clauses.append((a, b))

    assign = [None] * (n + 1)

    def lit_true(l):
        v = assign[abs(l)]
        if v is None:
            return None
        return (v == 1) if l > 0 else (v == 0)

    def propagate():
        # returns False on conflict; scans all clauses each round until fixpoint
        changed = True
        while changed:
            changed = False
            for (a, b) in clauses:
                ta, tb = lit_true(a), lit_true(b)
                if ta is True or tb is True:
                    continue
                if ta is False and tb is False:
                    return False
                if ta is False:            # b forced true
                    assign[abs(b)] = 1 if b > 0 else 0
                    changed = True
                elif tb is False:          # a forced true
                    assign[abs(a)] = 1 if a > 0 else 0
                    changed = True
        return True

    ok = True
    for i in range(1, n + 1):
        if assign[i] is not None:
            continue
        snapshot = assign[:]
        assign[i] = 0
        if not propagate():
            assign[:] = snapshot
            assign[i] = 1
            if not propagate():
                ok = False
                break

    if not ok:
        print("NO")
    else:
        for i in range(1, n + 1):
            if assign[i] is None:
                assign[i] = 0
        print("YES")
        print(*[assign[i] for i in range(1, n + 1)])


main()
