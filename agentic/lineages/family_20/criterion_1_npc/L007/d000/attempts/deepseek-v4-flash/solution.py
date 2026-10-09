import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj, edges):
    # adj: list of list of (neighbor, edge_id)
    visited = [False] * (n+1)
    tin = [-1] * (n+1)
    low = [-1] * (n+1)
    timer = 0
    bridges = set()

    def dfs(v, p_edge):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

# Edmonds' blossom algorithm for maximum matching
def max_matching(n, adj):
    # adj: list of list of neighbors (1-indexed)
    match = [0] * (n+1)
    p = [0] * (n+1)
    base = [0] * (n+1)
    used = [0] * (n+1)
    q = [0] * (n+1)
    blossom = [0] * (n+1)

    def lca(a, b):
        used_path = [False] * (n+1)
        while True:
            a = base[a]
            used_path[a] = True
            if match[a] == 0:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_path[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, child):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = child
            child = match[v]
            v = p[match[v]]

    def find_path(root):
        used = [False] * (n+1)
        p = [0] * (n+1)
        base = list(range(n+1))
        q = [0] * (n+1)
        qh = 0
        qt = 0
        q[qt] = root
        qt += 1
        used[root] = True
        while qh < qt:
            v = q[qh]; qh += 1
            for to in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != 0 and p[match[to]] != 0):
                    curbase = lca(v, to)
                    blossom = [False] * (n+1)
                    mark_path(v, curbase, to)
                    mark_path(to, curbase, v)
                    for i in range(1, n+1):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q[qt] = i; qt += 1
                elif p[to] == 0:
                    p[to] = v
                    if match[to] == 0:
                        return to, p
                    to = match[to]
                    used[to] = True
                    q[qt] = to; qt += 1
        return 0, p

    for i in range(1, n+1):
        if match[i] == 0:
            v, p = find_path(i)
            if v:
                while v:
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
    adj = [[] for _ in range(n+1)]
    for eid in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check for bridges
    bridges = find_bridges(n, adj, edges)
    if bridges:
        print("NO")
        return

    # Build adjacency for matching (neighbors only)
    adj_match = [[] for _ in range(n+1)]
    for u, v in edges:
        adj_match[u].append(v)
        adj_match[v].append(u)

    match = max_matching(n, adj_match)

    # Check perfect matching
    for i in range(1, n+1):
        if match[i] == 0:
            print("NO")
            return

    # Color edges: first find matching edges -> color 1
    color = [0] * m
    match_edge = {}
    for eid, (u, v) in enumerate(edges):
        if match[u] == v:
            color[eid] = 1
            match_edge[(u, v)] = eid
            match_edge[(v, u)] = eid

    # Remaining graph: 2-regular, color cycles with 2 and 3
    # Build adjacency for remaining edges (not in matching)
    rem_adj = [[] for _ in range(n+1)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == 0:
            rem_adj[u].append((v, eid))
            rem_adj[v].append((u, eid))

    visited = [False] * (n+1)
    for start in range(1, n+1):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                nxt = -1
                for to, eid in rem_adj[cur]:
                    if eid != prev:
                        nxt = to
                        cycle_edges.append(eid)
                        prev = eid
                        break
                if nxt == -1:
                    break
                cur = nxt
                if cur == start:
                    break
            # color alternately 2 and 3
            for i, eid in enumerate(cycle_edges):
                if i % 2 == 0:
                    color[eid] = 2
                else:
                    color[eid] = 3

    # Output
    print("YES")
    print(' '.join(str(color[i]) for i in range(m)))

if __name__ == "__main__":
    solve()