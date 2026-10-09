import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    essential = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        essential[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0 and v != parent[1]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)

    cnt = [1 if essential[i] else 0 for i in range(n + 1)]

    for u in reversed(order):
        p = parent[u]
        if p != -1:
            cnt[p] += cnt[u]

    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_weight[u]

    sys.stdout.write(str(total))

solve()