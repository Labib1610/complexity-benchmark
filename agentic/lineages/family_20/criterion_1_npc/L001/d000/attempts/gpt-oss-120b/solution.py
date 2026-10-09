import sys
sys.setrecursionlimit(10000)

# ---------- bridge detection ----------
def find_bridges(n, adj):
    tin = [-1] * n
    low = [0] * n
    timer = 0
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

# ---------- Edmonds' blossom (max matching) ----------
def blossom_maximum_matching(n, g):
    # g: adjacency list of vertices (list of lists)
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
        for i in range(n):
            base[i] = i
        q = []
        q_head = 0
        q.append(root)
        used[root] = True
        while q_head < len(q):
            v = q[q_head]
            q_head += 1
            for to in g[v]:
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
                        # augmenting
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

# ---------- main ----------
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

    # 1) bridge test
    if find_bridges(n, adj):
        print("NO")
        return

    # 2) build simple adjacency for matching (ignore parallel edges – none in cubic)
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    match = blossom_maximum_matching(n, g)
    matched = sum(1 for x in match if x != -1) // 2
    if matched != n // 2:
        print("NO")
        return

    # 3) colour edges
    ans = [0] * m
    # colour 1 for matching edges
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            # find edge id
            for to, eid in adj[v]:
                if to == u:
                    ans[eid] = 1
                    break

    # remaining edges: build adjacency of remaining graph (each vertex degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if ans[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        cur = start
        prev_edge = -1
        colour = 2
        while True:
            visited[cur] = True
            # pick the edge not equal to prev_edge
            for to, eid in rem_adj[cur]:
                if eid != prev_edge:
                    break
            ans[eid] = colour
            colour = 5 - colour          # switch between 2 and 3
            prev_edge = eid
            cur = to
            if visited[cur]:
                break

    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()