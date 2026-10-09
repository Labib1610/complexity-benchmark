import sys
sys.setrecursionlimit(1000000)

def find_unmatched_vertex(n, match):
    for v in range(n):
        if match[v] == -1:
            return v
    return -1

def max_matching(n, graph):
    # graph is adjacency list
    match = [-1] * n
    p = [-1] * n
    base = [-1] * n
    used = [False] * n
    blossom = [False] * n

    from collections import deque

    def lca(a, b):
        used_path = [False] * n
        while True:
            a = base[a]
            used_path[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_path[b]:
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
        q = deque([root])
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

    for i in range(n):
        if match[i] == -1:
            v = find_path(i)
            if v == -1:
                continue
            while v != -1:
                pv = p[v]
                nv = match[pv] if pv != -1 else -1
                match[v] = pv
                if pv != -1:
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
        adj[u].append(v)
        adj[v].append(u)

    # Check if graph is 3-regular
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return

    # Find perfect matching
    match = max_matching(n, adj)
    if any(x == -1 for x in match):
        print("NO")
        return

    # Color matching edges with color 1
    color = [0] * m
    match_set = set()
    for u in range(n):
        v = match[u]
        if u < v:
            # find edge index
            for idx, (a, b) in enumerate(edges):
                if (a == u and b == v) or (a == v and b == u):
                    color[idx] = 1
                    match_set.add(idx)
                    break

    # Remaining graph is 2-regular -> cycles
    # Build adjacency for remaining edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    # Color cycles alternately with 2 and 3
    visited = [False] * n
    for start in range(n):
        if not visited[start]:
            # find cycle
            cycle_edges = []
            stack = [(start, -1, -1)]  # node, parent, edge_idx
            while stack:
                node, par, eidx = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                if eidx != -1:
                    cycle_edges.append(eidx)
                for nei, eid in rem_adj[node]:
                    if nei == par:
                        continue
                    stack.append((nei, node, eid))
            # color cycle edges alternately
            # We need to traverse cycle properly; easier: find degree 2 nodes
            # Let's reconstruct cycle order
            if not cycle_edges:
                continue
            # find a node in cycle
            start_node = None
            for i in range(n):
                if len(rem_adj[i]) == 2:
                    start_node = i
                    break
            if start_node is None:
                continue
            # traverse
            prev = -1
            cur = start_node
            cycle = []
            while True:
                visited[cur] = True
                nxt = None
                eid_cur = None
                for nei, eid in rem_adj[cur]:
                    if nei != prev:
                        nxt = nei
                        eid_cur = eid
                        break
                if nxt is None:
                    break
                cycle.append(eid_cur)
                prev, cur = cur, nxt
                if cur == start_node:
                    break
            # color alternately
            for i, eid in enumerate(cycle):
                color[eid] = 2 if i % 2 == 0 else 3

    # Verify
    for u in range(n):
        colors = set()
        for v in adj[u]:
            for idx, (a, b) in enumerate(edges):
                if (a == u and b == v) or (a == v and b == u):
                    colors.add(color[idx])
        if len(colors) != 3:
            print("NO")
            return

    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()