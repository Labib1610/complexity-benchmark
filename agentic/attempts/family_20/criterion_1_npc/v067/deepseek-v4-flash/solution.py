import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj):
    tin = [-1] * n
    low = [-1] * n
    visited = [False] * n
    timer = 0
    bridges = []

    def dfs(v, p):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((v, to))

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def blossom_max_matching(n, adj):
    # Edmonds' Blossom algorithm for maximum cardinality matching
    match = [-1] * n
    p = [-1] * n
    base = [-1] * n
    q = []
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
        nonlocal used, p, base, q, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q = [root]
        used[root] = True
        for v in q:
            for u in adj[v]:
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
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # Check cubic
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return

    # Check bridges
    bridges = find_bridges(n, adj)
    if bridges:
        print("NO")
        return

    # Find perfect matching
    match = blossom_max_matching(n, adj)
    if match.count(-1) != 0:
        print("NO")
        return

    # Color edges
    color = [0] * m
    # Matching edges get color 3
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 3

    # Remaining graph is 2-regular (cycles)
    # Build adjacency for non-matching edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # traverse cycle
            start = i
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                # find next edge not going back to prev
                nxt = -1
                eidx = -1
                for (to, eid) in rem_adj[cur]:
                    if to != prev:
                        nxt = to
                        eidx = eid
                        break
                if nxt == -1:
                    break
                # assign color alternating 1,2
                # We need to know if we are at start
                if cur == start:
                    color[eidx] = 1
                else:
                    # alternate based on previous edge color
                    # find previous edge color
                    prev_color = None
                    for (to, eid) in rem_adj[cur]:
                        if to == prev:
                            prev_color = color[eid]
                            break
                    color[eidx] = 3 - prev_color  # 1<->2
                prev = cur
                cur = nxt
                if cur == start:
                    break

    # Verify all edges colored
    for c in color:
        if c == 0:
            print("NO")
            return

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()