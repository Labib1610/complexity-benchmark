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

    # ---------- Edmonds' Blossom for maximum matching ----------
    N = n
    INF = 10**9
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

    def mark_path(v, b, x):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = x
            x = match[v]
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
            for to, _ in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    cur = lca(v, to)
                    blossom = [False] * N
                    mark_path(v, cur, to)
                    mark_path(to, cur, v)
                    for i in range(N):
                        if blossom[base[i]]:
                            base[i] = cur
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        # augmenting
                        v = to
                        while v != -1:
                            pv = p[v]
                            nv = match[pv] if pv != -1 else -1
                            match[v] = pv
                            match[pv] = v
                            v = nv
                        return True
                    else:
                        used[match[to]] = True
                        q.append(match[to])
        return False

    for v in range(N):
        if match[v] == -1:
            find_path(v)

    # -------------------------------------------------------------

    if any(m == -1 for m in match):
        print("NO")
        return

    # assign colors
    color = [0] * m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 1

    # build remaining graph (degree 2 each)
    adj_rem = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            adj_rem[u].append((v, idx))
            adj_rem[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # traverse component (cycle)
        cur = start
        prev_edge = -1
        col = 2
        while True:
            visited[cur] = True
            # find next edge not prev_edge
            nxt = None
            for to, eid in adj_rem[cur]:
                if eid != prev_edge:
                    nxt = (to, eid)
                    break
            if nxt is None:
                break
            to, eid = nxt
            color[eid] = col
            col = 5 - col  # toggle between 2 and 3
            prev_edge = eid
            cur = to
            if visited[cur]:
                break

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()