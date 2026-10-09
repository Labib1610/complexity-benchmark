import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom (maximum matching) ----------
def blossom_maximum_matching(adj):
    n = len(adj)
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
            for to in adj[v]:
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

# ---------- Main ----------
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
        adj[u].append(v)
        adj[v].append(u)

    match = blossom_maximum_matching(adj)
    matched = sum(1 for x in match if x != -1) // 2
    if matched * 2 != n:
        print("NO")
        return

    # colour array, 0 = uncoloured, 1/2/3 final colours
    colour = [0] * m
    # map edge (u,v) to its index (there may be parallel edges? not in cubic graph)
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        edge_id[(u, v)] = edge_id[(v, u)] = idx

    # colour matching edges with 1
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            idx = edge_id[(v, u)]
            colour[idx] = 1

    # build adjacency of remaining edges (each vertex degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for (nbr, eid) in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # walk the cycle starting from this edge
            cur = start
            cur_eid = eid
            cur_col = 2  # start colour
            while True:
                visited_edge[cur_eid] = True
                colour[cur_eid] = cur_col
                # move to the other endpoint
                u, v = edges[cur_eid]
                nxt = v if cur == u else u
                # find the next edge in the cycle (the other unused edge incident to nxt)
                for (to, ne) in rem_adj[nxt]:
                    if not visited_edge[ne]:
                        cur = nxt
                        cur_eid = ne
                        cur_col = 5 - cur_col   # toggle between 2 and 3
                        break
                else:
                    break  # cycle finished
    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()