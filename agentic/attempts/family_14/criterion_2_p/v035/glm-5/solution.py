import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    required = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        required[v] = True

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
    for v in order:
        for to, w in adj[v]:
            if to != parent[v]:
                parent[to] = v
                parent_weight[to] = w
                order.append(to)

    cnt = [1 if required[i] else 0 for i in range(n + 1)]
    total = 0
    for v in reversed(order):
        p = parent[v]
        if p != 0 and cnt[v] != 0 and cnt[v] != t:
            total += parent_weight[v]
            cnt[p] += cnt[v]

    print(total)

solve()