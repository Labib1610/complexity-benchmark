import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1, not used separately
    t = int(next(it))

    targets = [int(next(it)) for _ in range(t)]
    if t == 1:
        # no required differences
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    # iterative DFS to get parent, weight to parent and order
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight of edge (parent -> node)
    order = []
    stack = [(1, 0, 0)]         # node, weight from parent, parent
    while stack:
        v, w, p = stack.pop()
        parent[v] = p
        pw[v] = w
        order.append(v)
        for to, wt in adj[v]:
            if to == p:
                continue
            stack.append((to, wt, v))

    cnt = [0] * (n + 1)
    for v in targets:
        cnt[v] = 1

    total = t
    ans = 0
    for v in reversed(order):
        p = parent[v]
        if p != 0:
            if 0 < cnt[v] < total:
                ans += pw[v]
            cnt[p] += cnt[v]

    print(ans)


if __name__ == "__main__":
    solve()