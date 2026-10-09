import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj, edges):
    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
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
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def find_perfect_matching(n, adj, edges):
    # Use Blossom algorithm via networkx? Not available. 
    # We'll implement a simple augmenting path for general graph (Edmonds' Blossom).
    # For n <= 2000, we can use a simpler approach: 
    # Since graph is cubic and bridgeless, we can find a perfect matching by 
    # repeatedly finding an augmenting path in a greedy matching.
    # But to be safe, we implement Edmonds' Blossom algorithm.
    
    # We'll implement a standard blossom algorithm for maximum matching.
    match = [-1] * (n + 1)
    p = [-1] * (n + 1)
    base = list(range(n + 1))
    q = []
    used = [False] * (n + 1)
    blossom = [False] * (n + 1)

    def lca(a, b):
        used_lca = [False] * (n + 1)
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
        nonlocal used, p, base, q, blossom
        used = [False] * (n + 1)
        p = [-1] * (n + 1)
        for i in range(1, n + 1):
            base[i] = i
        q = [root]
        used[root] = True
        while q:
            v = q.pop(0)
            for to, eid in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False] * (n + 1)
                    mark_path(v, curbase, to)
                    mark_path(to, curbase, v)
                    for i in range(1, n + 1):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        return to
                    to = match[to]
                    used[to] = True
                    q.append(to)
        return -1

    for i in range(1, n + 1):
        if match[i] == -1:
            v = find_path(i)
            while v != -1:
                pv = p[v]
                nv = match[pv]
                match[v] = pv
                match[pv] = v
                v = nv

    matching_edges = []
    for i in range(1, n + 1):
        if i < match[i]:
            matching_edges.append((i, match[i]))
    return matching_edges

def solve():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for eid in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check bridges
    bridges = find_bridges(n, adj, edges)
    if bridges:
        print("NO")
        return

    # Find perfect matching
    matching_edges = find_perfect_matching(n, adj, edges)
    if len(matching_edges) * 2 != n:
        print("NO")
        return

    match_eid = set()
    for u, v in matching_edges:
        # find edge id
        for to, eid in adj[u]:
            if to == v:
                match_eid.add(eid)
                break

    # Remaining edges form disjoint cycles
    remaining_adj = [[] for _ in range(n + 1)]
    for eid, (u, v) in enumerate(edges):
        if eid not in match_eid:
            remaining_adj[u].append((v, eid))
            remaining_adj[v].append((u, eid))

    color = [0] * m
    # Color matching edges with 3
    for eid in match_eid:
        color[eid] = 3

    # Color cycles with 1 and 2
    visited = [False] * (n + 1)
    for start in range(1, n + 1):
        if not visited[start] and remaining_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                nxt, eid = remaining_adj[cur][0] if remaining_adj[cur][0][0] != prev else remaining_adj[cur][1]
                cycle_edges.append(eid)
                prev = cur
                cur = nxt
                if cur == start:
                    break
            # color alternately
            for i, eid in enumerate(cycle_edges):
                color[eid] = 1 if i % 2 == 0 else 2

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()