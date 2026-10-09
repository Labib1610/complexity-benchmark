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

    # ---------- Edmonds' blossom (maximum matching) ----------
    # implementation adapted from emaxx.ru / CP-algorithms
    N = n
    g = [[] for _ in range(N)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

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

    # -----------------------------------------------------------

    if sum(1 for x in match if x != -1) // 2 != n // 2:
        print("NO")
        return

    # colour array
    colour = [0] * m
    in_matching = [False] * m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            colour[idx] = 1
            in_matching[idx] = True

    # build graph of remaining edges (degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not in_matching[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # each component must be a cycle
        # walk the cycle
        cur = start
        prev = -1
        cycle_edges = []
        while True:
            visited[cur] = True
            # pick the edge not coming from prev
            nxt = None
            eidx = None
            for to, ei in rem_adj[cur]:
                if to != prev:
                    nxt = to
                    eidx = ei
                    break
            if nxt is None:   # dead end -> not a cycle
                print("NO")
                return
            cycle_edges.append(eidx)
            prev, cur = cur, nxt
            if cur == start:
                break
        # assign alternating colours 2,3
        col = 2
        for ei in cycle_edges:
            colour[ei] = col
            col = 5 - col   # switch between 2 and 3

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()