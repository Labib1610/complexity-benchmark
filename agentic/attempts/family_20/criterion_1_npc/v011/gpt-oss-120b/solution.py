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
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # ---------- bridge detection ----------
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def dfs(v, p):
        nonlocal timer, has_bridge
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
                    has_bridge = True

    dfs(0, -1)
    if has_bridge:
        print("NO")
        return

    # ---------- Edmonds blossom (max matching) ----------
    # implementation from emaxx.ru, adapted
    from collections import deque

    N = n
    g = [[] for _ in range(N)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

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
        nonlocal q, used, p, base, blossom
        used[:] = [False] * N
        p[:] = [-1] * N
        for i in range(N):
            base[i] = i
        q.clear()
        q.append(root)
        used[root] = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom[:] = [False] * N
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

    matched_edges = {}
    for v in range(N):
        if match[v] != -1 and v < match[v]:
            matched_edges[(v, match[v])] = True

    if sum(1 for x in match if x != -1) // 2 != n // 2:
        print("NO")
        return

    # ---------- build colouring ----------
    colour = [0] * m
    # colour 1 for matching edges
    for idx, (u, v) in enumerate(edges):
        if (u, v) in matched_edges or (v, u) in matched_edges:
            colour[idx] = 1

    # remaining graph: degree 2, walk cycles
    # build adjacency of remaining edges with their indices
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for to, eid in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # walk the cycle
            cycle = []
            cur = start
            prev = -1
            while True:
                # find next edge not visited
                for nxt, neid in rem_adj[cur]:
                    if neid == eid and not visited_edge[neid]:
                        break
                else:
                    break
                visited_edge[eid] = True
                cycle.append(eid)
                # move
                nxt = to if cur == start else None
                # actually we just follow the unique unused edge
                for nxt_candidate, neid in rem_adj[cur]:
                    if neid != eid and not visited_edge[neid]:
                        nxt = nxt_candidate
                        eid = neid
                        break
                prev, cur = cur, nxt
                if cur == start:
                    break
            # colour alternately 2,3
            col = 2
            for e in cycle:
                colour[e] = col
                col = 5 - col   # switch between 2 and 3

    # some edges may still be uncoloured (isolated cycles of length 2 impossible)
    # but just in case assign 2
    for i in range(m):
        if colour[i] == 0:
            colour[i] = 2

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    solve()