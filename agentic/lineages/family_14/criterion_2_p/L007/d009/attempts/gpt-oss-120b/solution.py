import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # equals n-1, not needed separately
    t = int(next(it))

    targets = [0] * (n + 1)
    for _ in range(t):
        idx = int(next(it))
        targets[idx] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    # iterative DFS to avoid recursion limit
    parent = [0] * (n + 1)
    w_to_parent = [0] * (n + 1)
    order = []

    stack = [1]
    parent[1] = -1          # root marker
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            w_to_parent[v] = w
            stack.append(v)

    subtree_cnt = [0] * (n + 1)
    total = 0
    for u in reversed(order):
        cnt = targets[u]
        for v, _ in adj[u]:
            if parent[v] == u:          # v is a child of u
                cnt += subtree_cnt[v]
        subtree_cnt[u] = cnt
        if parent[u] != -1:             # not the root
            if 0 < cnt < t:
                total += w_to_parent[u]

    print(total)


if __name__ == "__main__":
    solve()