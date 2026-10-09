import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    rented = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        rented[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    pos = 0
    while pos < len(order):
        u = order[pos]; pos += 1
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    cnt = [0] * (n + 1)
    for u in order:
        cnt[u] = 1 if rented[u] else 0

    for i in range(len(order) - 1, 0, -1):
        u = order[i]
        cnt[parent[u]] += cnt[u]

    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0:
            total += parent_weight[u]

    print(total)

solve()