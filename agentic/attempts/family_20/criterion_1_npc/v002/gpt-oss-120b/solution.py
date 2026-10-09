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

    # ---------- Edmonds' blossom for maximum matching ----------
    N = n
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    match = [-1] * N
    p = [-1] * N
    base = list(range(N))
    q = []
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
        used = [False] * N
        p = [-1] * N
        base = list(range(N))
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

    # --------------------------------------------------------------

    if any(mch == -1 for mch in match):
        print("NO")
        return

    # Build contracted graph of cycles
    # each matched edge gets color 1
    edge_color = [0] * m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            edge_color[idx] = 1

    # Build adjacency of remaining edges (they form a 2-regular graph)
    # For each vertex, the two non-matching incident edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if edge_color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # traverse the cycle component
        cur = start
        prev_edge = -1
        # find a start edge
        if not rem_adj[cur]:
            continue
        # walk the cycle
        cycle_edges = []
        while True:
            visited[cur] = True
            # pick an edge not equal to prev_edge
            for to, eid in rem_adj[cur]:
                if eid != prev_edge:
                    next_edge = eid
                    nxt = to
                    break
            cycle_edges.append(next_edge)
            prev_edge = next_edge
            cur = nxt
            if cur == start:
                break
        # assign alternating colors 2 and 3
        col = 2
        for eid in cycle_edges:
            edge_color[eid] = col
            col = 5 - col  # toggle between 2 and 3

    print("YES")
    print(' '.join(str(c) for c in edge_color))

if __name__ == "__main__":
    solve()