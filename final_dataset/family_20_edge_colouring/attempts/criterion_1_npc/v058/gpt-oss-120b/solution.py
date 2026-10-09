import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds blossom (implementation from emaxx) ----------
def blossom_maximum_matching(n, edges):
    # n : number of vertices (0..n-1)
    # edges : list of (u,v) with u<v
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append(v)
        g[v].append(u)

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

# ---------- Bridge detection ----------
def has_bridge(n, edges):
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    tin = [-1] * n
    low = [0] * n
    timer = 0
    visited_edge = [False] * len(edges)
    def dfs(v, parent):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in g[v]:
            if eid == parent:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    raise StopIteration  # bridge found
    try:
        for i in range(n):
            if tin[i] == -1:
                dfs(i, -1)
        return False
    except StopIteration:
        return True

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

    if has_bridge(n, edges):
        print("NO")
        return

    match = blossom_maximum_matching(n, edges)
    matched = [False] * m
    colour = [0] * m

    # map edge to its index
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        edge_id[(u, v)] = idx
        edge_id[(v, u)] = idx

    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            idx = edge_id[(v, u)]
            colour[idx] = 1
            matched[idx] = True

    # build adjacency of remaining edges
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not matched[idx]:
            adj[u].append((v, idx))
            adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        cur = start
        prev_edge = -1
        cur_colour = 2
        while True:
            visited[cur] = True
            # find the next edge not equal to prev_edge
            for to, eid in adj[cur]:
                if eid != prev_edge:
                    break
            else:
                break  # should not happen
            colour[eid] = cur_colour
            # move forward
            prev_edge = eid
            cur = to
            cur_colour = 5 - cur_colour  # toggle between 2 and 3
            if visited[cur]:
                break

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()