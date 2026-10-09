import sys
from collections import deque

# Blossom algorithm for maximum matching (general graph)
def max_matching(n, edges):
    # Standard implementation of Edmonds' blossom algorithm
    # Returns a list matching where matching[i] is matched vertex or -1
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    q = deque()
    used = [False] * n
    blossom = [False] * n

    def lca(a, b):
        used_lca = [False] * n
        while True:
            a = base[a]
            used_lca[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_lca[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal p, base, used, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q.clear()
        q.append(root)
        used[root] = True
        while q:
            v = q.popleft()
            for u in graph[v]:
                if base[v] == base[u] or match[v] == u:
                    continue
                if u == root or (match[u] != -1 and p[match[u]] != -1):
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
                    if match[u] == -1:
                        return u
                    u = match[u]
                    used[u] = True
                    q.append(u)
        return -1

    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for i in range(n):
        if match[i] == -1:
            v = find_path(i)
            while v != -1:
                pv = p[v]
                nv = match[pv]
                match[v] = pv
                match[pv] = v
                v = nv

    return match

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
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # Step 1: Find perfect matching
    match = max_matching(n, edges)
    if -1 in match:
        print("NO")
        return

    # matched_edges indices
    matched = set()
    matching_edge_idx = [-1] * n
    for u, v in edges:
        pass
    # Build matching using match list
    matching_edge_set = set()
    for i in range(n):
        if match[i] != -1 and i < match[i]:
            # find the edge index
            for eidx, (a,b) in enumerate(edges):
                if (a == i and b == match[i]) or (a == match[i] and b == i):
                    matching_edge_set.add(eidx)
                    break

    # Step 2: Remaining graph is 2-regular (cycles)
    color = [0] * m
    visited_vertex = [False] * n

    for start in range(n):
        if not visited_vertex[start]:
            if match[start] == -1:
                continue
            # walk the cycle that does not use matching edges
            cycle_vertices = []
            cur = start
            prev = -1
            while True:
                visited_vertex[cur] = True
                cycle_vertices.append(cur)
                # find non-matching neighbor
                nxt = -1
                for v, eidx in adj[cur]:
                    if eidx not in matching_edge_set and v != prev:
                        nxt = v
                        break
                if nxt == -1:
                    break
                prev, cur = cur, nxt
                if cur == start:
                    break
            if len(cycle_vertices) % 2 == 1:
                # odd cycle -> fail
                print("NO")
                return
            # color alternates on cycle edges
            for i in range(len(cycle_vertices)):
                u = cycle_vertices[i]
                v = cycle_vertices[(i+1)%len(cycle_vertices)]
                for eidx, (a,b) in enumerate(edges):
                    if (a==u and b==v) or (a==v and b==u):
                        if i % 2 == 0:
                            color[eidx] = 1
                        else:
                            color[eidx] = 2
                        break

    # Assign color 3 to matching edges
    for eidx in matching_edge_set:
        color[eidx] = 3

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()