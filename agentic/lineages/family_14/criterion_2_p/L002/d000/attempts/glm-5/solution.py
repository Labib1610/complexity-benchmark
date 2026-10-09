import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    vital = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        vital[v] = True

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    parent_edge = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    pos = 0
    while pos < len(order):
        u = order[pos]; pos += 1
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge[v] = w
                depth[v] = depth[u] + 1
                order.append(v)

    LOG = max(1, (n).bit_length())
    up = [[0] * (n + 1) for _ in range(LOG)]
    up[0] = parent[:]
    for k in range(1, LOG):
        upk = up[k]
        upk_1 = up[k - 1]
        for v in range(1, n + 1):
            upk[v] = upk_1[upk_1[v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        k = 0
        while diff:
            if diff & 1:
                u = up[k][u]
            diff >>= 1
            k += 1
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    marked = [False] * (n + 1)
    vital_nodes = []
    for i in range(1, n + 1):
        if vital[i]:
            vital_nodes.append(i)
            marked[i] = True

    vital_nodes.sort(key=lambda x: depth[x])
    for i in range(len(vital_nodes) - 1):
        a = vital_nodes[i]
        b = vital_nodes[i + 1]
        l = lca(a, b)
        if not marked[l]:
            marked[l] = True
            vital_nodes.append(l)
            vital_nodes.sort(key=lambda x: depth[x])

    total = 0
    for v in vital_nodes:
        if v != 1 and marked[parent[v]]:
            total += parent_edge[v]

    print(total)

solve()