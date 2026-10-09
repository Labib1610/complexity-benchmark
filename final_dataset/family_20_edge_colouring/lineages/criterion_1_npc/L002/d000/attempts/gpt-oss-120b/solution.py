import sys
sys.setrecursionlimit(10000000)

# ---------- Edmonds' blossom (CP‑Algorithms version) ----------
def max_matching(n, g):
    """return list match where match[v] = partner or -1"""
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

# ---------- Main solving ----------
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

    match = max_matching(n, adj)
    matched = sum(1 for x in match if x != -1) // 2
    if matched != n // 2:
        print("NO")
        return

    # colour array, 0‑based colours (0,1,2) -> output +1
    col = [-1] * m
    # map edge (u,v) to its index (multiple edges not present)
    edge_id = {}
    for i, (u, v) in enumerate(edges):
        edge_id[(u, v)] = i
        edge_id[(v, u)] = i

    # colour matching edges with 0 (will output 1)
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            idx = edge_id[(v, u)]
            col[idx] = 0

    # build adjacency of remaining edges
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if col[i] == -1:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))

    visited_edge = [False] * m

    for start in range(n):
        for (to, eid) in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # start a new cycle, colour alternately 1 and 2 (output 2,3)
            cur = start
            prev = -1
            cur_col = 1  # will be colour 2 in output
            while True:
                # find the unused edge from cur not leading back to prev
                for (nxt, neid) in rem_adj[cur]:
                    if visited_edge[neid]:
                        continue
                    if nxt == prev:
                        continue
                    # this is the next edge
                    visited_edge[neid] = True
                    col[neid] = cur_col
                    cur_col = 3 - cur_col  # toggle between 1 and 2
                    prev, cur = cur, nxt
                    break
                else:
                    break
                # stop when we return to start and the edge is already visited
                if cur == start:
                    # the cycle is closed, all its edges are coloured
                    break

    # output
    print("YES")
    print(' '.join(str(c + 1) for c in col))

if __name__ == "__main__":
    solve()