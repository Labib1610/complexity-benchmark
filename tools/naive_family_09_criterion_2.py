#!/usr/bin/env python3
"""Realistic baseline for family 09 / criterion 2 (bipartite independent set).

The maximum independent set of a bipartite graph is (nA+nB) - maximum matching
(König). This computes the matching with Kuhn's augmenting paths, O(V*E) -- the same
integer as the reference, but on adversarial structures (long augmenting chains) it
does the full O(V*E) work and TLEs, while Hopcroft-Karp stays O(E*sqrt V).
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    nA = int(data[idx]); idx += 1
    nB = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[] for _ in range(nA + 1)]
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        adj[a].append(b)

    match_v = [0] * (nB + 1)

    def augment(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_v[v] == 0 or augment(match_v[v], visited):
                    match_v[v] = u
                    return True
        return False

    matching = 0
    for u in range(1, nA + 1):
        if augment(u, [False] * (nB + 1)):
            matching += 1

    print((nA + nB) - matching)


main()
