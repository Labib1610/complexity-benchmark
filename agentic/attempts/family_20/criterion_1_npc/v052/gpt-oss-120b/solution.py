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

    # ---------- Edmonds' Blossom (max matching) ----------
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
        base = list(range(N))
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

    # -------------------------------------------------------

    # check perfect matching
    if any(mch == -1 for mch in match):
        print("NO")
        return

    # assign colors
    color = [0] * m
    # color 1 for matching edges
    for v in range(N):
        u = match[v]
        if v < u:
            # find edge index
            for to, idx in g[v]:
                if to == u:
                    color[idx] = 1
                    break

    # remaining edges form degree-2 graph
    visited_edge = [False] * m
    for idx, c in enumerate(color):
        if c == 1:
            visited_edge[idx] = True

    # build adjacency of remaining edges with edge ids
    rem_adj = [[] for _ in range(N)]
    for idx, (u, v) in enumerate(edges):
        if not visited_edge[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    # traverse cycles
    for start in range(N):
        for to, eid in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # start new cycle
            cur = start
            prev = -1
            cur_color = 2
            while True:
                # find edge not visited
                for nxt, neid in rem_adj[cur]:
                    if neid != prev and not visited_edge[neid]:
                        break
                else:
                    break
                visited_edge[neid] = True
                color[neid] = cur_color
                cur_color = 5 - cur_color  # toggle between 2 and 3
                prev = neid
                cur = nxt
                if cur == start:
                    break

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()