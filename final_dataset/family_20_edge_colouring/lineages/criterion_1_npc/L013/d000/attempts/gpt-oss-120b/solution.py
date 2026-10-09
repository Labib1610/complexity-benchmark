import sys
import random
sys.setrecursionlimit(10000)

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        edges.append((u, v))
        g[u].append((v, i))
        g[v].append((u, i))

    # find bridges
    tin = [-1]*n
    low = [0]*n
    timer = 0
    bridge = [False]*m
    def dfs(v, p_e):
        nonlocal timer
        tin[v] = low[v] = timer; timer += 1
        for to, ei in g[v]:
            if ei == p_e: continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, ei)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridge[ei] = True
    dfs(0, -1)
    if any(bridge):
        print("NO")
        return

    # Blossom algorithm for maximum matching (Edmonds)
    N = n
    adj = [[] for _ in range(N)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append(v)
        adj[v].append(u)

    match = [-1]*N
    base = list(range(N))
    p = [-1]*N
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
        nonlocal p, base, used, q, blossom
        p = [-1]*N
        used = [False]*N
        base = list(range(N))
        q = []
        q_head = 0
        q.append(root)
        used[root] = True
        while q_head < len(q):
            v = q[q_head]; q_head += 1
            for to in adj[v]:
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

    # now we have a perfect matching (since cubic and no bridges)
    # build unmatched adjacency
    unmatched_adj = [[] for _ in range(N)]
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        edge_id[(u, v)] = edge_id[(v, u)] = idx
        if match[u] == v:
            continue
        unmatched_adj[u].append((v, idx))
        unmatched_adj[v].append((u, idx))

    visited = [False]*N
    cycles = []
    edge_in_cycle = [False]*m
    for v in range(N):
        if not visited[v]:
            cur = v
            cycle = []
            while not visited[cur]:
                visited[cur] = True
                for to, eid in unmatched_adj[cur]:
                    if not edge_in_cycle[eid]:
                        edge_in_cycle[eid] = True
                        cycle.append(eid)
                        cur = to
                        break
            cycles.append(cycle)

    # assign colors
    colors = [0]*m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            colors[idx] = 1
    col2, col3 = 2, 3
    for cyc in cycles:
        curcol = col2
        for eid in cyc:
            colors[eid] = curcol
            curcol = col3 if curcol == col2 else col2

    print("YES")
    print(' '.join(map(str, colors)))

if __name__ == "__main__":
    solve()