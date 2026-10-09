import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    specials = [False] * (n + 1)
    for _ in range(t):
        specials[int(next(it))] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    edge_w = [0] * (n + 1)
    order = []

    stack = [(1, 0, 0)]          # node, parent, weight to parent
    while stack:
        v, p, w = stack.pop()
        parent[v] = p
        edge_w[v] = w
        order.append(v)
        for to, wt in adj[v]:
            if to == p:
                continue
            stack.append((to, v, wt))

    sub_special = [0] * (n + 1)
    ans = 0
    for v in reversed(order):
        cnt = 1 if specials[v] else 0
        for to, _ in adj[v]:
            if to == parent[v]:
                continue
            cnt += sub_special[to]
        sub_special[v] = cnt
        if parent[v] != 0 and 0 < cnt < t:
            ans += edge_w[v]

    print(ans)


if __name__ == "__main__":
    solve()