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

    # ---------- Edmonds' blossom (max matching) ----------
    # implementation from emaxx.ru / cp-algorithms
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
        nonlocal p, base, used, blossom, q
        p = [-1] * N
        used = [False] * N
        base = list(range(N))
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

    for v in range(N):
        if match[v] == -1:
            find_path(v)

    # -------------------------------------------------------

    # check perfect matching
    if any(match[v] == -1 for v in range(N)):
        print("NO")
        return

    # colour array
    col = [0] * m
    # colour matching edges with 1
    for v in range(N):
        if v < match[v]:
            u = match[v]
            # find edge id between v and u
            for nb, eid in adj[v]:
                if nb == u:
                    col[eid] = 1
                    break

    # build graph of remaining edges (degree 2)
    rem_adj = [[] for _ in range(N)]
    for idx, (u, v) in enumerate(edges):
        if col[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m

    for start in range(N):
        for nb, eid in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # walk the cycle
            cycle = []
            cur_v = start
            cur_e = eid
            while True:
                visited_edge[cur_e] = True
                cycle.append(cur_e)
                # move to the other endpoint
                u, v = edges[cur_e]
                nxt_v = v if cur_v == u else u
                # find next edge (the one not used yet)
                nxt = None
                for to, ne in rem_adj[nxt_v]:
                    if not visited_edge[ne]:
                        nxt = (to, ne)
                        break
                if nxt is None:
                    break  # cycle closed
                cur_v, cur_e = nxt_v, nxt[1]
            # colour alternately 2,3
            for i, e_id in enumerate(cycle):
                col[e_id] = 2 if i % 2 == 0 else 3

    print("YES")
    print(' '.join(str(c) for c in col))

if __name__ == "__main__":
    solve()