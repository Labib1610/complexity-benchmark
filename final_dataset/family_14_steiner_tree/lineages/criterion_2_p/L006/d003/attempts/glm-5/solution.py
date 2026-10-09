import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    priority = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        priority[v] = True

    if t <= 1:
        print(0)
        return

    head = list(range(n + 1))
    to = [0] * (2 * n)
    weight = [0] * (2 * n)
    nxt = [0] * (2 * n)
    edge_cnt = 0

    def add_edge(u, v, w):
        nonlocal edge_cnt
        edge_cnt += 1
        to[edge_cnt] = v
        weight[edge_cnt] = w
        nxt[edge_cnt] = head[u]
        head[u] = edge_cnt

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        add_edge(u, v, w)
        add_edge(v, u, w)

    LOG = 20
    up = [[0] * (n + 1) for _ in range(LOG)]
    up_w = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)

    stack = [(1, 0, 0, 0)]
    while stack:
        node, parent, parent_weight, state = stack.pop()
        if state == 0:
            visited[node] = True
            depth[node] = depth[parent] + 1 if parent != 0 else 0
            up[0][node] = parent
            up_w[0][node] = parent_weight
            stack.append((node, parent, parent_weight, 1))
            e = head[node]
            while e != 0:
                v = to[e]
                if not visited[v]:
                    stack.append((v, node, weight[e], 0))
                e = nxt[e]
        else:
            for j in range(1, LOG):
                mid = up[j-1][node]
                if mid != 0:
                    up[j][node] = up[j-1][mid]
                    up_w[j][node] = max(up_w[j-1][node], up_w[j-1][mid])
                else:
                    up[j][node] = 0
                    up_w[j][node] = 0

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
                res = max(res, up_w[j][u])
                u = up[j][u]
            diff >>= 1
            j += 1
        if u == v:
            return res
        for j in range(LOG - 1, -1, -1):
            if up[j][u] != up[j][v]:
                res = max(res, up_w[j][u], up_w[j][v])
                u = up[j][u]
                v = up[j][v]
        res = max(res, up_w[0][u], up_w[0][v])
        return res

    nodes = [i for i in range(1, n + 1) if priority[i]]
    nodes.sort(key=lambda x: depth[x])

    total = 0
    for i in range(1, len(nodes)):
        total += get_max_edge(nodes[i-1], nodes[i])

    print(total)

solve()