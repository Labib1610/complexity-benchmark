#!/usr/bin/env python3
"""Realistic baseline for family 05 / criterion 2 (bipartite assignment).

Kuhn's augmenting-path matching, O(V*E): for each worker run a DFS that reassigns
already-matched workers along an augmenting path. This is the standard, competent
solution -- but on adversarial structures (long augmenting chains) it does the full
O(V*E) work and TLEs, while the Hopcroft-Karp reference stays O(E*sqrt(V)).
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    e = int(data[idx]); idx += 1
    adj = [[] for _ in range(k + 1)]
    for _ in range(e):
        x = int(data[idx]); y = int(data[idx + 1]); idx += 2
        adj[x].append(y)

    match_y = [0] * (k + 1)
    match_x = [0] * (k + 1)

    def try_augment(x, visited):
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                if match_y[y] == 0 or try_augment(match_y[y], visited):
                    match_y[y] = x; match_x[x] = y
                    return True
        return False

    matched = 0
    for x in range(1, k + 1):
        if try_augment(x, [False] * (k + 1)):
            matched += 1

    if matched < k:
        sys.stdout.write("NO\n"); return
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(match_x[x]) for x in range(1, k + 1)) + "\n")


main()
