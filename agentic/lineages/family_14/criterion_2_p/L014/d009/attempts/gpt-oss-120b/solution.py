import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1, not used separately
    t = int(next(it))

    specials = [int(next(it)) for _ in range(t)]

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    is_special = [0] * (n + 1)
    for s in specials:
        is_special[s] = 1

    parent = [0] * (n + 1)          # 0 means no parent (root)
    w_to_parent = [0] * (n + 1)     # weight of edge to parent
    order = []                      # preorder

    stack = [1]
    parent[1] = -1                  # mark root
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            w_to_parent[to] = w
            stack.append(to)

    cnt = is_special[:]             # subtree special counts
    for v in reversed(order):
        p = parent[v]
        if p > 0:                   # not the root
            cnt[p] += cnt[v]

    total = 0
    for v in range(2, n + 1):       # all non‑root vertices
        if cnt[v] > 0 and t - cnt[v] > 0:
            total += w_to_parent[v]

    print(total)


if __name__ == "__main__":
    solve()