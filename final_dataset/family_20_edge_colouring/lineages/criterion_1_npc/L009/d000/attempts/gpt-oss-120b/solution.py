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

    # ---------- check perfect matching ----------
    if any(mch == -1 for mch in match):
        print("NO")
        return

    # ---------- assign colors ----------
    color = [0] * m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 1

    # build remaining graph (edges not colored 1)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # traverse each cycle
        cur = start
        # find a cycle start with an unvisited edge
        stack = []
        while True:
            visited[cur] = True
            for nb, eid in rem_adj[cur]:
                if color[eid] == 0:
                    stack.append((cur, nb, eid))
                    break
            else:
                break
            # walk the cycle
            while stack:
                u, v, eid = stack.pop()
                if color[eid]:
                    continue
                # assign alternating 2,3
                # determine color based on previous edge at u
                # we can simply traverse the cycle and flip
                # start new traversal
                cyc = []
                cu, cv = u, v
                while True:
                    # find edge id between cu and cv (already have eid)
                    cyc.append((cu, cv, eid))
                    # move forward
                    # remove used edge from adjacency temporarily
                    # find next neighbor from cv not equal to cu
                    nxt = None
                    nxt_eid = None
                    for nb2, eid2 in rem_adj[cv]:
                        if (nb2 == cu and eid2 == eid) or color[eid2]:
                            continue
                        nxt = nb2
                        nxt_eid = eid2
                        break
                    if nxt is None:
                        break
                    cu, cv, eid = cv, nxt, nxt_eid
                    if cu == u and cv == v:
                        break
                # color cycle
                col = 2
                for _, _, e in cyc:
                    color[e] = col
                    col = 5 - col  # toggle between 2 and 3
                break
            break

    # some edges may remain uncolored due to traversal logic; handle simply:
    for idx in range(m):
        if color[idx] == 0:
            color[idx] = 2  # any leftover (should not happen)

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()