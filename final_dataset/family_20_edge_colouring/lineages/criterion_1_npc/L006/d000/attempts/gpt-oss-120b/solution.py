import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    g = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        g[u].append((v, idx))
        g[v].append((u, idx))

    # ---------- bridge detection ----------
    timer = 0
    tin = [0] * n
    low = [0] * n
    bridge = False

    def dfs(v, pe):
        nonlocal timer, bridge
        timer += 1
        tin[v] = low[v] = timer
        for to, eid in g[v]:
            if eid == pe:
                continue
            if tin[to] == 0:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridge = True
            else:
                low[v] = min(low[v], tin[to])

    dfs(0, -1)
    if bridge:
        print("NO")
        return

    # ---------- Edmonds blossom (max matching) ----------
    # implementation based on emaxx.ru
    from collections import deque

    N = n
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    match = [-1] * N
    p = [-1] * N
    base = list(range(N))
    q = deque()
    used = [False] * N
    blossom = [False] * N

    def lca(a, b):
        used_path = [False] * N
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
        nonlocal used, p, base, q, blossom
        used = [False] * N
        p = [-1] * N
        for i in range(N):
            base[i] = i
        q.clear()
        q.append(root)
        used[root] = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False] * N
                    mark_path(v, curbase, to)
                    mark_path(to, curbase, v)
                    for i in range(N):
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

    for v in range(N):
        if match[v] == -1:
            find_path(v)

    if any(m == -1 for m in match):
        print("NO")
        return

    # ---------- build colouring ----------
    ans = [0] * m
    in_match = [False] * m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            ans[idx] = 3
            in_match[idx] = True

    # adjacency of the 2-regular graph (edges not in matching)
    adj2 = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not in_match[idx]:
            adj2[u].append((v, idx))
            adj2[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for to, eid in adj2[start]:
            if visited_edge[eid]:
                continue
            # walk the whole cycle
            cycle_edges = []
            cur_v = start
            cur_e = eid
            while True:
                visited_edge[cur_e] = True
                cycle_edges.append(cur_e)
                # move to the other vertex
                u, v = edges[cur_e]
                nxt_v = v if cur_v == u else u
                # find the next edge (the other incident edge not yet used)
                nxt = None
                for nb, nb_eid in adj2[nxt_v]:
                    if not visited_edge[nb_eid]:
                        nxt = (nb, nb_eid)
                        break
                if nxt is None:
                    break  # cycle closed
                cur_v, cur_e = nxt
                if cur_v == start:
                    # completed the cycle
                    visited_edge[cur_e] = True
                    cycle_edges.append(cur_e)
                    break
            # colour alternating 1,2
            col = 1
            for e in cycle_edges:
                ans[e] = col
                col = 2 if col == 1 else 1

    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()