import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom algorithm (general graph maximum matching) ----------
def max_matching(n, adj):
    """return mate list, size of maximum matching"""
    INF = n + 5
    mate = [-1] * n
    label = [0] * n
    parent = [-1] * n
    orig = list(range(n))
    aux = [-1] * n

    def lca(v, w):
        aux_id = lca.aux_id
        aux_id += 1
        lca.aux_id = aux_id
        while True:
            if v != -1:
                if aux[v] == aux_id:
                    return v
                aux[v] = aux_id
                if mate[v] == -1:
                    v = -1
                else:
                    v = orig[parent[mate[v]]]
            v, w = w, v
    lca.aux_id = 0

    def blossom(v, w, a):
        while orig[v] != a:
            parent[v] = w
            w = mate[v]
            if label[w] == 1:
                label[w] = 0
                q.append(w)
            orig[v] = orig[w] = a
            v = parent[w]

    def augment(v):
        while v != -1:
            pv = parent[v]
            nv = mate[pv] if pv != -1 else -1
            mate[v] = pv
            mate[pv] = v
            v = nv

    for root in range(n):
        if mate[root] != -1:
            continue
        # BFS
        label = [-1] * n
        parent = [-1] * n
        orig = list(range(n))
        q = []
        label[root] = 0
        q.append(root)
        found = -1
        for qi in range(len(q)):
            v = q[qi]
            for u in adj[v]:
                if label[u] == -1:
                    label[u] = 1
                    parent[u] = v
                    if mate[u] == -1:
                        found = u
                        break
                    label[mate[u]] = 0
                    q.append(mate[u])
                elif label[u] == 0 and orig[v] != orig[u]:
                    a = lca(orig[v], orig[u])
                    blossom(v, u, a)
                    blossom(u, v, a)
            if found != -1:
                break
        if found != -1:
            augment(found)
    size = sum(1 for x in mate if x != -1) // 2
    return mate, size

# ------------------------------- Main solution ---------------------------------
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

    mate, sz = max_matching(n, adj)
    if sz * 2 != n:          # not a perfect matching
        print("NO")
        return

    # colour array, 0..2 -> output 1..3
    colour = [0] * m
    # map each vertex to its partner in the matching
    partner = mate

    # give colour 1 to matching edges
    for v in range(n):
        u = partner[v]
        if u != -1 and v < u:
            # find edge index
            for idx, (a, b) in enumerate(edges):
                if (a == v and b == u) or (a == u and b == v):
                    colour[idx] = 1
                    break

    # build contracted graph: each matched pair becomes a super vertex
    super_id = [-1] * n
    cur = 0
    for v in range(n):
        if super_id[v] == -1:
            u = partner[v]
            super_id[v] = super_id[u] = cur
            cur += 1
    super_adj = [[] for _ in range(cur)]
    # for each original edge not in matching, add to super graph
    for idx, (u, v) in enumerate(edges):
        if colour[idx] != 0:
            continue
        su = super_id[u]
        sv = super_id[v]
        super_adj[su].append((sv, idx))
        super_adj[sv].append((su, idx))

    visited = [False] * cur
    for start in range(cur):
        if visited[start]:
            continue
        # walk the cycle
        v = start
        prev_edge = -1
        cur_col = 2  # start with colour 2
        while True:
            visited[v] = True
            # find next edge not equal to prev_edge
            for (to, eidx) in super_adj[v]:
                if eidx != prev_edge:
                    break
            else:
                break  # should not happen
            colour[eidx] = cur_col
            # move
            prev_edge = eidx
            v = to
            cur_col = 5 - cur_col   # toggle between 2 and 3
            if visited[v]:
                # cycle closed
                break

    # output
    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()