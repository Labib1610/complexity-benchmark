import sys
sys.setrecursionlimit(10000)

# ---------- bridge detection ----------
def find_bridges(n, adj):
    timer = 0
    tin = [-1] * n
    low = [0] * n
    visited = [False] * n
    has_bridge = False

    def dfs(v, p):
        nonlocal timer, has_bridge
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, _ in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return has_bridge

# ---------- Edmonds blossom (general matching) ----------
# implementation adapted from emaxx / CP-algorithms
def blossom_maximum_matching(n, edges):
    # adjacency list of edge indices
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))

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
            for to, _ in g[v]:
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

    # bridge test
    if find_bridges(n, adj):
        print("NO")
        return

    # perfect matching
    match = blossom_maximum_matching(n, edges)
    # verify perfect
    if any(x == -1 for x in match):
        print("NO")
        return

    # colour array
    colour = [0] * m
    # colour matching edges with 1
    for v in range(n):
        u = match[v]
        if u > v:  # handle each edge once
            # find its index
            for to, idx in adj[v]:
                if to == u:
                    colour[idx] = 1
                    break

    # build adjacency of remaining edges (those not coloured)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for to, idx in rem_adj[start]:
            if visited_edge[idx]:
                continue
            # walk the whole cycle
            cycle = []
            cur_v = start
            cur_e = idx
            while True:
                visited_edge[cur_e] = True
                cycle.append(cur_e)
                # move to the other vertex
                u, v = edges[cur_e]
                nxt_v = v if cur_v == u else u
                # find next edge in the cycle (the other edge incident to nxt_v)
                for nxt, eidx in rem_adj[nxt_v]:
                    if not visited_edge[eidx] and eidx != cur_e:
                        cur_v = nxt_v
                        cur_e = eidx
                        break
                else:
                    # closed cycle
                    break
                if cur_e == idx:
                    break
            # colour alternately 2,3
            col = 2
            for e in cycle:
                colour[e] = col
                col = 5 - col   # switch between 2 and 3

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    solve()