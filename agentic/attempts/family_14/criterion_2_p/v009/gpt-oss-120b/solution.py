import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it)
    m = next(it)          # equals n-1
    t = next(it)

    required = [False] * (n + 1)
    for _ in range(t):
        v = next(it)
        required[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    # iterative DFS to get parent, edge weight and order
    parent = [0] * (n + 1)
    w_parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1          # root marker

    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            w_parent[to] = w
            stack.append(to)

    cnt = [0] * (n + 1)
    ans = 0

    for v in reversed(order):
        cur = 1 if required[v] else 0
        for to, _ in adj[v]:
            if parent[to] == v:          # to is a child
                cur += cnt[to]
        cnt[v] = cur
        if v != 1:                       # skip root
            if cnt[v] > 0 and t - cnt[v] > 0:
                ans += w_parent[v]

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()