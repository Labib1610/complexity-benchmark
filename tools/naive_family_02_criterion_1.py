#!/usr/bin/env python3
"""Realistic baseline for family 02 / criterion 1 (3-SAT).

DPLL: decide variables in index order (0 then 1), with unit propagation between
decisions. This is the competent, standard solution a good model would write --
not a strawman. Near the m/n ~ 4.26 phase transition, UNSAT instances force
exhaustive refutation and this blows up exponentially.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    clauses = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); c = int(data[idx + 2]); idx += 3
        clauses.append((a, b, c))

    assign = [None] * (n + 1)

    def lit_true(l):
        v = assign[abs(l)]
        if v is None:
            return None
        return (v == 1) if l > 0 else (v == 0)

    sys.setrecursionlimit(1 << 20)

    def dpll(nextv):
        forced = []
        # unit propagation to fixpoint
        changed = True
        while changed:
            changed = False
            for cl in clauses:
                unassigned = None
                cnt_unassigned = 0
                sat = False
                for l in cl:
                    tv = lit_true(l)
                    if tv is True:
                        sat = True
                        break
                    if tv is None:
                        cnt_unassigned += 1
                        unassigned = l
                if sat:
                    continue
                if cnt_unassigned == 0:
                    for v in forced:
                        assign[v] = None
                    return False
                if cnt_unassigned == 1:
                    assign[abs(unassigned)] = 1 if unassigned > 0 else 0
                    forced.append(abs(unassigned))
                    changed = True

        v = nextv
        while v <= n and assign[v] is not None:
            v += 1
        if v > n:
            return True

        for val in (0, 1):
            assign[v] = val
            if dpll(v + 1):
                return True
            assign[v] = None
        for u in forced:
            assign[u] = None
        return False

    if dpll(1):
        print("YES")
        print(*[assign[i] if assign[i] is not None else 0 for i in range(1, n + 1)])
    else:
        print("NO")


main()
