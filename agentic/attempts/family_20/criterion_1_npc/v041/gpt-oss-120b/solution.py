import sys
sys.setrecursionlimit(10000)

# ---------- 1. bridge detection ----------
def find_bridges(n, adj):
    timer = 0
    tin = [-1] * n
    low = [0] * n
    bridges = []

    def dfs(v, p):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, _ in adj[v]:
            if to == p:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((v, to))
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return bridges

# ---------- 2. Edmonds blossom (max matching) ----------
# implementation from Stanford ACM notebook, public domain
def max_matching(n, graph):
    INF = n + 5
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    q = []
    used = [False] * n
    blossom = [False] * n

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
        nonlocal q, used, p, base, blossom
        used = [False] * n
        p = [-1] * n
        base = list(range(n))
        q = []
        q_head = 0
        q.append(root)
        used[root] = True
        while q_head < len(q):
            v = q[q_head]
            q_head += 1
            for to in graph[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False] * n
                    mark_path(v, curbase, to)
                    mark_path(to, curbase, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        # augmenting path found
                        cur = to
                        while cur != -1:
                            prev = p[cur]
                            nxt = match[prev] if prev != -1 else -1
                            match[cur] = prev
                            match[prev] = cur
                            cur = nxt
                        return True
                    else:
                        used[match[to]] = True
                        q.append(match[to])
        return False

    for v in range(n):
        if match[v] == -1:
            find_path(v)
    return match

# ---------- 3. main ----------
def solve() -> None:
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

    # bridge test
    if find_bridges(n, adj):
        print("NO")
        return

    # build simple adjacency list for matching (ignore multiple edges)
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    match = max_matching(n, g)
    if any(x == -1 for x in match):
        print("NO")
        return

    # colour edges
    colour = [0] * m
    matched = set()
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            # find the index of edge (v,u)
            for to, idx in adj[v]:
                if to == u:
                    colour[idx] = 1
                    matched.add(idx)
                    break

    # build graph of non‑matched edges
    non_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if idx in matched:
            continue
        non_adj[u].append((v, idx))
        non_adj[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for to, idx in non_adj[start]:
            if visited_edge[idx]:
                continue
            # walk the whole cycle
            cur = start
            cur_col = 2
            while True:
                # find the unused edge from cur
                for nxt, eidx in non_adj[cur]:
                    if not visited_edge[eidx]:
                        visited_edge[eidx] = True
                        colour[eidx] = cur_col
                        cur = nxt
                        cur_col = 5 - cur_col   # switch between 2 and 3
                        break
                else:
                    break
                # stop when we return to start
                if cur == start:
                    break

    print("YES")
    print(' '.join(str(colour[i]) for i in range(m)))

if __name__ == "__main__":
    solve()