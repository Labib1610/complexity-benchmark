import sys
sys.setrecursionlimit(10000)

# ---------- Blossom algorithm (Edmonds) ----------
def max_matching(n, g):
    """return list match where match[v] = matched vertex or -1"""
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

# ---------- Bridge detection ----------
def find_bridges(n, edges):
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    tin = [-1] * n
    low = [0] * n
    timer = 0
    bridges = []

    def dfs(v, p_edge):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in g[v]:
            if eid == p_edge:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append(eid)
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return bridges

# ---------- Main ----------
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))

    # bridge test
    if find_bridges(n, edges):
        print("NO")
        return

    # build adjacency for blossom (undirected simple)
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append(v)
        g[v].append(u)

    match = max_matching(n, g)
    matched = [False] * m
    edge_id_of = {}
    for v in range(n):
        if match[v] != -1 and v < match[v]:
            u = v
            w = match[v]
            # find the edge id between u and w
            for idx, (a, b) in enumerate(edges):
                if (a == u and b == w) or (a == w and b == u):
                    edge_id_of[(u, w)] = idx
                    edge_id_of[(w, u)] = idx
                    matched[idx] = True
                    break

    if sum(matched) != n // 2:
        print("NO")
        return

    colour = [0] * m
    for idx in range(m):
        if matched[idx]:
            colour[idx] = 3

    # remaining edges adjacency with edge ids
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not matched[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        cur = start
        prev = -1
        cur_colour = 1
        while True:
            visited[cur] = True
            # find next edge not coming from prev
            nxt = None
            eid = None
            for to, idd in rem_adj[cur]:
                if to != prev:
                    nxt = to
                    eid = idd
                    break
            if nxt is None:
                break  # isolated vertex (should not happen)
            colour[eid] = cur_colour
            cur_colour = 3 - cur_colour  # toggle 1<->2
            prev, cur = cur, nxt
            if cur == start:
                break

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    solve()