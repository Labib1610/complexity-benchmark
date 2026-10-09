import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    m = int(next(it))          # = n-1
    t = int(next(it))

    critical = [False] * (n + 1)
    for _ in range(t):
        critical[int(next(it))] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    # iterative DFS to obtain parent, edge weight to parent and order
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight of edge to parent
    order = []
    stack = [1]
    parent[1] = -1              # root marker

    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                pw[v] = w
                stack.append(v)

    # bottom‑up: count critical vertices in each subtree
    cnt = [0] * (n + 1)
    for u in reversed(order):
        total = 1 if critical[u] else 0
        for v, _ in adj[u]:
            if parent[v] == u:          # v is a child of u
                total += cnt[v]
        cnt[u] = total

    total_crit = t
    ans = 0
    for v in range(2, n + 1):           # all vertices except the root
        sub = cnt[v]
        if sub > 0 and total_crit - sub > 0:
            ans += pw[v]

    print(ans)

if __name__ == "__main__":
    solve()