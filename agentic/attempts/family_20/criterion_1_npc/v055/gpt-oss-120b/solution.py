import sys
sys.setrecursionlimit(10000)

# ---------- 1. bridge detection ----------
def find_bridges(n, adj):
    tin = [0]*n
    low = [0]*n
    timer = 1
    bridges = []

    def dfs(v, p_edge):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if tin[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append(eid)
    for i in range(n):
        if not tin[i]:
            dfs(i, -1)
    return bridges

# ---------- 2. Edmonds blossom (CP‑algorithm version) ----------
def blossom_maximum_matching(n, edges):
    # adjacency list with edge ids
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))

    match = [-1]*n
    p = [-1]*n
    base = list(range(n))
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

    def mark_path(v, b, child):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = child
            child = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal q, used, p, base, blossom
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
            for to, _ in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    cur = lca(v, to)
                    blossom = [False]*n
                    mark_path(v, cur, to)
                    mark_path(to, cur, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = cur
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        # augmenting path found
                        return to
                    to_match = match[to]
                    used[to_match] = True
                    q.append(to_match)
        return -1

    for v in range(n):
        if match[v] == -1:
            to = find_path(v)
            if to == -1:
                continue
            # augment
            cur = to
            while cur != -1:
                prev = p[cur]
                nxt = match[prev] if prev != -1 else -1
                match[cur] = prev
                match[prev] = cur
                cur = nxt
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

    # perfect matching
    match = blossom_maximum_matching(n, edges)
    matched_edges = set()
    for v in range(n):
        if match[v] != -1 and v < match[v]:
            u = v
            w = match[v]
            # find edge id between u and w
            for to, eid in adj[u]:
                if to == w:
                    matched_edges.add(eid)
                    break

    if len(matched_edges) != n // 2:
        print("NO")
        return

    colour = [0]*m
    for eid in matched_edges:
        colour[eid] = 1

    # build graph of remaining edges (degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False]*m
    for start in range(n):
        # each vertex belongs to exactly one cycle, start if there is an unused edge
        for to, eid in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # walk the whole cycle
            cur = start
            cur_colour = 2
            while True:
                # take the unused edge from cur
                for nxt, neid in rem_adj[cur]:
                    if not visited_edge[neid]:
                        break
                visited_edge[neid] = True
                colour[neid] = cur_colour
                cur_colour = 5 - cur_colour   # toggle between 2 and 3
                cur = nxt
                if cur == start:
                    break

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()