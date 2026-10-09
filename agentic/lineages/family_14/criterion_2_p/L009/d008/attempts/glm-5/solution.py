import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    E = int(data[idx]); idx += 1
    F = int(data[idx]); idx += 1

    targets = []
    for _ in range(F):
        targets.append(int(data[idx]) - 1)
        idx += 1

    edges = []
    for _ in range(E):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))

    if F <= 1:
        print(0)
        return

    parent = list(range(N))
    rank = [0] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    edges.sort(key=lambda e: e[2])

    mst_adj = [[] for _ in range(N)]
    for u, v, w in edges:
        if union(u, v):
            mst_adj[u].append((v, w))
            mst_adj[v].append((u, w))

    LOG = max(1, (N).bit_length())
    up = [[-1] * N for _ in range(LOG)]
    max_edge = [[0] * N for _ in range(LOG)]
    depth = [0] * N

    stack = [(targets[0], -1, 0, 0)]
    visited = [False] * N
    visited[targets[0]] = True
    order = []

    while stack:
        node, par, d, mx = stack.pop()
        depth[node] = d
        up[0][node] = par
        max_edge[0][node] = mx
        order.append(node)
        for nxt, w in mst_adj[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, node, d + 1, w))

    for j in range(1, LOG):
        for v in order:
            p = up[j-1][v]
            if p != -1:
                up[j][v] = up[j-1][p]
                max_edge[j][v] = max(max_edge[j-1][v], max_edge[j-1][p])
            else:
                up[j][v] = -1
                max_edge[j][v] = max_edge[j-1][v]

    def get_max_edge(u, v):
        if u == v:
            return 0
        res = 0
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        j = 0
        while diff:
            if diff & 1:
                res = max(res, max_edge[j][u])
                u = up[j][u]
            diff >>= 1
            j += 1
        if u == v:
            return res
        for j in range(LOG - 1, -1, -1):
            if up[j][u] != up[j][v]:
                res = max(res, max_edge[j][u], max_edge[j][v])
                u = up[j][u]
                v = up[j][v]
        res = max(res, max_edge[0][u], max_edge[0][v])
        return res

    edges_needed = []
    for i in range(F):
        for j in range(i + 1, F):
            u = targets[i]
            v = targets[j]
            edges_needed.append((get_max_edge(u, v), u, v))

    edges_needed.sort(key=lambda e: e[0])

    parent2 = list(range(N))
    rank2 = [0] * N

    def find2(x):
        while parent2[x] != x:
            parent2[x] = parent2[parent2[x]]
            x = parent2[x]
        return x

    def union2(x, y):
        rx = find2(x)
        ry = find2(y)
        if rx == ry:
            return False
        if rank2[rx] < rank2[ry]:
            parent2[rx] = ry
        elif rank2[rx] > rank2[ry]:
            parent2[ry] = rx
        else:
            parent2[ry] = rx
            rank2[rx] += 1
        return True

    total = 0
    for w, u, v in edges_needed:
        if union2(u, v):
            total += w

    print(total)

solve()