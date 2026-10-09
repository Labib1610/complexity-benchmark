import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    terminals = set(int(next(it)) for _ in range(t))

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    # iterative DFS to get order and parent info
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_w[v] = w
            stack.append(v)

    cnt = [0] * (n + 1)
    ans = 0
    for u in reversed(order):
        cnt[u] = 1 if u in terminals else 0
        for v, w in adj[u]:
            if parent[v] == u:          # v is child
                cnt[u] += cnt[v]
        if u != 1:
            # edge to parent
            if 0 < cnt[u] < t:
                ans += parent_w[u]

    print(ans)

if __name__ == "__main__":
    solve()