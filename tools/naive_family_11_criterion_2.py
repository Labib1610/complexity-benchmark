#!/usr/bin/env python3
"""Realistic baseline for family 11 / criterion 2 (paired-skill = edge cover).

Consultants are edges; the minimum edge cover is (uA+uB) - maximum matching (Gallai).
This computes the matching with Kuhn's augmenting paths, O(V*E) -- the same integer as
the reference -- but on adversarial structures (long augmenting chains) it does the full
O(V*E) work and TLEs, while Hopcroft-Karp stays O(E*sqrt V).
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    uA = int(data[idx]); uB = int(data[idx + 1]); s = int(data[idx + 2]); idx += 3
    adj = [[] for _ in range(uA + 1)]
    seen = set()
    for _ in range(s):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        if (a, b) not in seen:
            seen.add((a, b)); adj[a].append(b)

    match_v = [0] * (uB + 1)

    def augment(u_, visited):
        for v in adj[u_]:
            if not visited[v]:
                visited[v] = True
                if match_v[v] == 0 or augment(match_v[v], visited):
                    match_v[v] = u_
                    return True
        return False

    matching = 0
    for u_ in range(1, uA + 1):
        if augment(u_, [False] * (uB + 1)):
            matching += 1

    print((uA + uB) - matching)


main()
