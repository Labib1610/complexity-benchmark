import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    required = [0] * (n + 1)
    for _ in range(t):
        required[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    edges_w = [0] * (n - 1)
    for idx in range(n - 1):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
        edges_w[idx] = w

    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, eid in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_edge[v] = eid
            stack.append(v)

    cnt = [0] * (n + 1)
    for u in reversed(order):
        cnt[u] += required[u]
        p = parent[u]
        if p != -1:
            cnt[p] += cnt[u]

    total = 0
    for v in range(2, n + 1):
        c = cnt[v]
        if c > 0 and t - c > 0:
            total += edges_w[parent_edge[v]]
    print(total)

if __name__ == "__main__":
    solve()