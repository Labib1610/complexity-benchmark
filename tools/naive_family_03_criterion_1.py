#!/usr/bin/env python3
"""Realistic baseline for family 03 / criterion 1 (Hamiltonian path).

Recursive DFS backtracking with the standard "visited" pruning: try each start
vertex in ascending order, always extend to the smallest unvisited neighbour, and
backtrack on a dead end. The first complete path found in this order IS the
lexicographically smallest one, so the output matches the reference exactly. This
is the natural O(n!) solution a competent model writes when it does not think of
bitmask DP -- not a strawman (it prunes visited vertices). On dense graphs with NO
Hamiltonian path it explores an enormous search tree before failing.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)
    for a in adj:
        a.sort()                       # ascending neighbours -> lex-smallest path first

    if n == 1:
        print("YES"); print(1); return

    visited = [False] * (n + 1)
    path = []
    sys.setrecursionlimit(1 << 20)
    found = [None]

    def dfs(u, count):
        path.append(u); visited[u] = True
        if count == n:
            found[0] = path.copy()
            visited[u] = False; path.pop()
            return True
        for w in adj[u]:
            if not visited[w] and dfs(w, count + 1):
                visited[u] = False; path.pop()
                return True
        visited[u] = False; path.pop()
        return False

    for s in range(1, n + 1):          # ascending start -> lex-smallest
        if dfs(s, 1):
            break

    if found[0] is not None:
        print("YES"); print(' '.join(map(str, found[0])))
    else:
        print("NO")


main()
