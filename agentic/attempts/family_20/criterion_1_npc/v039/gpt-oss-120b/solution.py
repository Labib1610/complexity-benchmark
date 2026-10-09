import sys
sys.setrecursionlimit(10000)

# ---------- bridge detection ----------
def find_bridges(n, adj):
    tin = [0]*n
    low = [0]*n
    timer = 1
    bridges = []

    def dfs(v, p):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if to == p:
                continue
            if tin[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append(eid)
    for i in range(n):
        if not tin[i]:
            dfs(i, -1)
    return bridges

# ---------- Edmonds blossom (max matching) ----------
def blossom_maximum_matching(n, graph):
    # graph: adjacency list of vertices, each entry list of neighbours
    # implementation from emaxx.ru, O(n^3)
    INF = n + 5
    match = [-1]*n
    base = list(range(n))
    p = [-1]*n
    q = []
    used = [False]*n
    blossom = [False]*n

    def lca(a, b):
        used_path = [False]*n
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
        nonlocal q, p, used, base, blossom
        used = [False]*n
        p = [-1]*n
        for i in range(n):
            base[i] = i
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
                    blossom = [False]*n
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

    # bridge test
    if find_bridges(n, adj):
        print("NO")
        return

    # build simple adjacency for blossom (ignore multiple edges, they are allowed)
    simple_adj = [[] for _ in range(n)]
    for u, v in edges:
        simple_adj[u].append(v)
        simple_adj[v].append(u)

    match = blossom_maximum_matching(n, simple_adj)
    # verify perfect
    if any(x == -1 for x in match):
        print("NO")
        return

    # map each vertex to its matched neighbour
    matched_edge = {}
    for v in range(n):
        u = match[v]
        if v < u:
            # find edge id
            for to, eid in adj[v]:
                if to == u:
                    matched_edge[(v, u)] = eid
                    matched_edge[(u, v)] = eid
                    break

    # build contracted graph (vertices are original vertices, edges are the two
    # non‑matched incident edges)
    contract_adj = [[] for _ in range(n)]   # each entry: (neighbour, edge_id)
    for v in range(n):
        cnt = 0
        for to, eid in adj[v]:
            if (v, to) in matched_edge:
                continue
            contract_adj[v].append((to, eid))
            cnt += 1
        # cnt must be 2
    # colour answer
    ans = [0]*m
    for eid in matched_edge.values():
        ans[eid] = 1

    visited = [False]*n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        cur = start
        prev = -1
        colour = 2
        while True:
            visited[cur] = True
            # pick the edge not coming from prev
            for to, eid in contract_adj[cur]:
                if to == prev:
                    continue
                break
            ans[eid] = colour
            colour = 5 - colour          # toggle between 2 and 3
            prev, cur = cur, to
            if visited[cur]:
                break

    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()