#!/usr/bin/env python3
"""Realistic (correct but inefficient) baseline for family 02 / criterion 3.

Find the smallest variable forced into contradiction, WITHOUT the SCC shortcut: for
each variable j in index order, assert j true and propagate to a fixpoint (re-
scanning all clauses); if that forces j false it is trapped one way, then assert j
false and propagate; if that also conflicts, j is contradicted. Each variable costs
an O(m) propagation, so the search is O(n*m) -- correct, but times out at the
stated bounds while the O(n+m) SCC reference is instant.
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
        changed = True
        while changed:
            changed = False
            for (a, b) in clauses:
                ta, tb = lit_true(a), lit_true(b)
                if ta is True or tb is True:
                    continue
                if ta is False and tb is False:
                    return False
                if ta is False:
                    assign[abs(b)] = 1 if b > 0 else 0
                    changed = True
                elif tb is False:
                    assign[abs(a)] = 1 if a > 0 else 0
                    changed = True
        return True

    for j in range(1, n + 1):
        # assert j true
        assign[:] = [None] * (n + 1)
        assign[j] = 1
        true_conflict = not propagate()
        # assert j false
        assign[:] = [None] * (n + 1)
        assign[j] = 0
        false_conflict = not propagate()
        if true_conflict and false_conflict:
            print(j)
            return


main()
