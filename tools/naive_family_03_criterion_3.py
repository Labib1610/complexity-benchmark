#!/usr/bin/env python3
"""Realistic baseline for family 03 / criterion 3 (infeasible: isolated vertex).

A solution that does NOT spot the isolated-vertex shortcut and instead tries to
decide the delivery route by actually searching for a Hamiltonian path first, only
falling back to reporting the cut-off vertex once the search fails. The search is
exhaustive DFS backtracking (iterative, explicit stack, so deep graphs cannot cause
a recursion/stack crash -- it just runs until it times out). On the small anchors
the search exhausts instantly and it prints the correct smallest isolated vertex;
at n ~ 1e5 the search explodes and it TLEs, exactly as an exponential attempt at an
NP-hard subproblem should.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    has_edge = [False] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)
        has_edge[u] = True; has_edge[v] = True

    # Try to find a Hamiltonian path (iterative DFS with explicit stack + backtracking)
    # before concluding. With a cut-off vertex present no path exists, so on large
    # instances this exhausts astronomically -> TLE.
    def has_hamiltonian_path():
        for start in range(1, n + 1):
            visited = bytearray(n + 1)
            visited[start] = 1
            path_len = 1
            stack = [[start, 0]]           # [vertex, next neighbour index]
            while stack:
                if path_len == n:
                    return True
                top = stack[-1]
                u, i = top[0], top[1]
                advanced = False
                a = adj[u]
                while i < len(a):
                    w = a[i]; i += 1
                    if not visited[w]:
                        top[1] = i
                        visited[w] = 1
                        stack.append([w, 0]); path_len += 1
                        advanced = True
                        break
                if not advanced:
                    stack.pop(); visited[u] = 0; path_len -= 1
        return False

    has_hamiltonian_path()               # always False here (isolated vertex), but searched

    for v in range(1, n + 1):
        if not has_edge[v]:
            print(v)
            return


main()
