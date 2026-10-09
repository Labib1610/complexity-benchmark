import sys
from collections import deque

def find_perfect_matching(n, adj):
    # Edmonds' Blossom algorithm for maximum matching in general graph
    # Returns a list mate of length n, mate[i] = partner or -1 if unmatched
    mate = [-1] * n
    p = [-1] * n
    base = list(range(n))
    used = [False] * n
    blossom = [False] * n
    q = deque()

    def lca(a, b):
        used_path = [False] * n
        while True:
            a = base[a]
            used_path[a] = True
            if mate[a] == -1:
                break
            a = p[mate[a]]
        while True:
            b = base[b]
            if used_path[b]:
                return b
            b = p[mate[b]]

    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[mate[v]]] = True
            p[v] = children
            children = mate[v]
            v = p[mate[v]]

    def find_path(root):
        nonlocal p, base, used, q, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q = deque([root])
        used[root] = True
        while q:
            v = q.popleft()
            for u in adj[v]:
                if base[v] == base[u] or mate[v] == u:
                    continue
                if u == root or (mate[u] != -1 and p[mate[u]] != -1):
                    curbase = lca(v, u)
                    blossom = [False] * n
                    mark_path(v, curbase, u)
                    mark_path(u, curbase, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[u] == -1:
                    p[u] = v
                    if mate[u] == -1:
                        return u
                    used[mate[u]] = True
                    q.append(mate[u])
        return -1

    for i in range(n):
        if mate[i] == -1:
            v = find_path(i)
            if v == -1:
                continue
            while v != -1:
                pv = p[v]
                nv = mate[pv] if pv != -1 else -1
                mate[v] = pv
                mate[pv] = v
                v = nv
    return mate

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    mate = find_perfect_matching(n, adj)
    if mate.count(-1) != 0:
        print("NO")
        return

    # Color matching edges with 1
    color = [0] * m
    match_edge = {}
    for i, (u, v) in enumerate(edges):
        if mate[u] == v:
            color[i] = 1
            match_edge[(u, v)] = i
            match_edge[(v, u)] = i

    # Remaining graph: 2-regular -> cycles
    # Build adjacency for remaining edges
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if color[i] == 0:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))

    visited = [False] * n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                nxt = -1
                nxt_edge = -1
                for to, eid in rem_adj[cur]:
                    if to != prev:
                        nxt = to
                        nxt_edge = eid
                        break
                if nxt == -1:
                    break
                cycle_edges.append(nxt_edge)
                prev, cur = cur, nxt
                if cur == start:
                    break
            # color alternately 2,3
            for k, eid in enumerate(cycle_edges):
                color[eid] = 2 if k % 2 == 0 else 3

    # Edge case: isolated vertices? Not possible in cubic graph.
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()