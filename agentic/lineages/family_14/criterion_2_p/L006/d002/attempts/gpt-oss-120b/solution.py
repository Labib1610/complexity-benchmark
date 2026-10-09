import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)          # = n-1
    t = next(it)

    specials = [0] * (n + 1)
    for _ in range(t):
        v = next(it)
        specials[v] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight of edge to parent
    order = []                  # traversal order
    stack = [1]
    parent[1] = -1              # mark root

    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if parent[to] == 0:
                parent[to] = v
                pw[to] = w
                stack.append(to)

    cnt = [0] * (n + 1)
    ans = 0
    total_special = t

    for v in reversed(order):
        cur = specials[v]
        # add children's counts (already accumulated)
        for to, _ in adj[v]:
            if parent[to] == v:          # to is a child
                cur += cnt[to]
        cnt[v] = cur
        if v != 1:                       # not root, consider edge to parent
            if 0 < cnt[v] < total_special:
                ans += pw[v]

    print(ans)

if __name__ == "__main__":
    solve()