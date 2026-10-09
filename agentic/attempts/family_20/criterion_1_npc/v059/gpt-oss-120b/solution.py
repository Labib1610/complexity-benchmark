import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom algorithm (general graph maximum matching) ----------
def max_matching(n, adj):
    """return list mate where mate[v] = matched vertex or -1"""
    INF = n + 5
    mate = [-1] * n
    label = [0] * n
    parent = [-1] * n
    base = list(range(n))
    q = []

    def lca(a, b):
        used = [False] * n
        while True:
            a = base[a]
            used[a] = True
            if mate[a] == -1:
                break
            a = parent[mate[a]]
        while True:
            b = base[b]
            if used[b]:
                return b
            b = parent[mate[b]]

    def mark_path(v, b, x):
        while base[v] != b:
            blossom[base[v]] = blossom[base[mate[v]]] = True
            parent[v] = x
            x = mate[v]
            v = parent[mate[v]]

    def blossom_contraction(v, u):
        b = lca(v, u)
        blossom[:] = [False] * n
        mark_path(v, b, u)
        mark_path(u, b, v)
        for i in range(n):
            if blossom[base[i]]:
                base[i] = b
                if label[i] == 1:
                    label[i] = 0
                    q.append(i)

    def bfs(root):
        nonlocal q
        label[:] = [-1] * n
        parent[:] = [-1] * n
        for i in range(n):
            base[i] = i
        q = []
        q.append(root)
        label[root] = 0
        head = 0
        while head < len(q):
            v = q[head]
            head += 1
            for u in adj[v]:
                if label[u] == -1:
                    label[u] = 1
                    parent[u] = v
                    if mate[u] == -1:
                        # augmenting path found
                        augment(v, u)
                        return True
                    label[mate[u]] = 0
                    q.append(mate[u])
                elif label[u] == 0 and base[v] != base[u] and mate[v] != u:
                    blossom_contraction(v, u)
        return False

    def augment(v, u):
        # flip edges along the augmenting path
        while True:
            pv = parent[v]
            nv = mate[pv]
            mate[v] = pv
            mate[pv] = v
            v = nv
            if v == -1:
                break

    for v in range(n):
        if mate[v] == -1:
            bfs(v)

    return mate

# ---------- Main solving part ----------
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

    mate = max_matching(n, adj)
    matched = sum(1 for x in mate if x != -1) // 2
    if matched * 2 != n:
        print("NO")
        return

    # colour array
    col = [0] * m
    # mark edges of the perfect matching
    edge_id = {}
    for i, (u, v) in enumerate(edges):
        edge_id[(u, v)] = edge_id[(v, u)] = i

    for v in range(n):
        u = mate[v]
        if u > v:  # handle each edge once
            idx = edge_id[(v, u)]
            col[idx] = 1

    # build adjacency of remaining edges (uncoloured)
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if col[i] == 0:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # traverse each component (it is a collection of even cycles)
        stack = [start]
        visited[start] = True
        while stack:
            v = stack.pop()
            for to, idx in rem_adj[v]:
                if col[idx] != 0:
                    continue
                # assign colour alternating 2/3
                # we need to know colour of the edge we came from
                # use DFS with parity
                # store parity in a dict
                # simpler: start a new cycle walk
                # walk the whole cycle
                cycle = []
                cur = v
                prev = -1
                while True:
                    # find next unused edge
                    for nxt, eidx in rem_adj[cur]:
                        if eidx != prev and col[eidx] == 0:
                            break
                    else:
                        break
                    cycle.append((cur, nxt, eidx))
                    col[eidx] = 2  # temporary
                    prev = eidx
                    cur = nxt
                    if cur == v:
                        break
                # colour alternately
                for j, (_, _, eidx) in enumerate(cycle):
                    col[eidx] = 2 if j % 2 == 0 else 3
                # mark vertices visited
                for a, b, _ in cycle:
                    if not visited[a]:
                        visited[a] = True
                        stack.append(a)
                    if not visited[b]:
                        visited[b] = True
                        stack.append(b)

    # any still zero (isolated?) should not happen
    for i in range(m):
        if col[i] == 0:
            col[i] = 2  # fallback

    print("YES")
    print(' '.join(map(str, col)))

if __name__ == "__main__":
    solve()