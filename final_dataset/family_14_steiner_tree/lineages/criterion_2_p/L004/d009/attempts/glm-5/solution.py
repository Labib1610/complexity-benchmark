import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    priority = [False] * (n + 1)
    for _ in range(t):
        p = int(data[idx]); idx += 1
        priority[p] = True

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
    order = []
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = w
                stack.append(v)

    count = [0] * (n + 1)
    for u in reversed(order):
        if priority[u]:
            count[u] += 1
        if parent[u] != 0:
            count[parent[u]] += count[u]

    total = 0
    for u in range(2, n + 1):
        if count[u] > 0:
            total += parent_edge[u]

    print(total)

solve()