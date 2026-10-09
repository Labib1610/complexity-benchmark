import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)          # = n-1, not used separately
    t = next(it)

    critical = [0] * (n + 1)
    for _ in range(t):
        v = next(it)
        critical[v] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
    order = []

    # iterative DFS to get parent array and traversal order
    stack = [1]
    parent[1] = -1               # mark root
    while stack:
        v = stack.pop()
        order.append(v)
        for nb, w in adj[v]:
            if nb != parent[v]:
                parent[nb] = v
                pw[nb] = w
                stack.append(nb)

    cnt = [0] * (n + 1)
    ans = 0
    # process vertices in reverse order (post‑order)
    for v in reversed(order):
        total = critical[v]
        for nb, _ in adj[v]:
            if parent[nb] == v:          # nb is a child
                total += cnt[nb]
        cnt[v] = total
        if parent[v] > 0:                # not the root
            if 0 < cnt[v] < t:
                ans += pw[v]

    print(ans)


if __name__ == "__main__":
    solve()