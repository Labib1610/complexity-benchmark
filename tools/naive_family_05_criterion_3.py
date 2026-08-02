#!/usr/bin/env python3
"""Realistic baseline for family 05 / criterion 3 (an unassignable worker).

A solution that does NOT notice the empty compatibility row and instead tries to
build a full assignment by backtracking (assign worker 1 a task, worker 2 a distinct
task, ...), only reporting the partnerless worker once the search fails. The
backtracking is exponential; when the partnerless worker sits at a HIGH index the
search assigns the earlier workers in exponentially many ways before hitting the
dead end, so it TLEs at scale. The reference's O(E) row scan is instant.
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    e = int(data[idx]); idx += 1
    adj = [[] for _ in range(k + 1)]
    has_partner = [False] * (k + 1)
    for _ in range(e):
        x = int(data[idx]); y = int(data[idx + 1]); idx += 2
        adj[x].append(y); has_partner[x] = True

    used = [False] * (k + 1)

    def assign(x):
        if x > k:
            return True
        for y in adj[x]:
            if not used[y]:
                used[y] = True
                if assign(x + 1):
                    return True
                used[y] = False
        return False

    assign(1)                            # exhaustive attempt (always fails: empty row)

    for x in range(1, k + 1):
        if not has_partner[x]:
            print(x); return


main()
