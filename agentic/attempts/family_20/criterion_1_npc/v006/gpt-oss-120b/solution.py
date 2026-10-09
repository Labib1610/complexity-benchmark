import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # ---- bridge detection ----
    tin = [-1]*n
    low = [0]*n
    timer = 0
    bridge = [False]*m
    def dfs(v, p_e):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_e: continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridge[eid] = True
    dfs(0, -1)
    if any(bridge):
        print("NO")
        return

    # ---- Blossom algorithm for maximum matching ----
    # implementation based on emaxx.ru
    N = n
    g = [[] for _ in range(N)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    match = [-1]*N
    p = [-1]*N
    base = list(range(N))
    q = []
    used = [False]*N
    blossom = [False]*N

    def lca(a, b):
        used_path = [False]*N
        while True:
            a = base[a]
            used_path[a] = True
            if match[a] == -1: break
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
        used = [False]*N
        p = [-1]*N
        base = list(range(N))
        q = []
        q_head = 0
        q.append(root)
        used[root] = True
        while q_head < len(q):
            v = q[q_head]; q_head += 1
            for to in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False]*N
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
                        return to
                    to_match = match[to]
                    used[to_match] = True
                    q.append(to_match)
        return -1

    def augment_path(finish):
        v = finish
        while v != -1:
            pv = p[v]
            ppv = match[pv] if pv != -1 else -1
            match[v] = pv
            match[pv] = v
            v = ppv

    for v in range(N):
        if match[v] == -1:
            finish = find_path(v)
            if finish != -1:
                augment_path(finish)

    # check perfect matching
    if any(m == -1 for m in match):
        print("NO")
        return

    # ---- contract matching edges ----
    pair_id = [-1]*n
    comp = [-1]*n
    comp_cnt = 0
    for v in range(n):
        if pair_id[v] == -1:
            u = match[v]
            pair_id[v] = pair_id[u] = comp_cnt
            comp_cnt += 1

    # build cycles graph
    cycle_adj = [[] for _ in range(comp_cnt)]
    edge_to_cycle = {}
    for idx, (u, v) in enumerate(edges):
        cu = pair_id[u]; cv = pair_id[v]
        if cu == cv:
            # this is a matching edge, will be color 3
            continue
        cycle_adj[cu].append((cv, idx))
        cycle_adj[cv].append((cu, idx))
        edge_to_cycle[idx] = (cu, cv)

    # each vertex degree should be 2
    # traverse cycles
    color = [0]*m
    for i in range(comp_cnt):
        if not cycle_adj[i]:
            continue
        # start traversal if not visited
        stack = []
        cur = i
        prev_edge = -1
        col = 1
        while True:
            # find next edge not prev
            for nxt, eid in cycle_adj[cur]:
                if eid != prev_edge:
                    break
            else:
                break
            # assign color col to this edge
            color[eid] = col
            # move
            prev_edge = eid
            # go to neighbor
            for nxt2, eid2 in cycle_adj[cur]:
                if eid2 == eid:
                    nxt = nxt2
                    break
            cur = nxt
            col = 2 if col == 1 else 1
            if cur == i:
                break

    # assign color 3 to matching edges
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            color[idx] = 3

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()