import sys
sys.setrecursionlimit(1 << 25)

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

    # root the tree at 1 (any node)
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
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
            pw[v] = w
            stack.append(v)

    # post-order compute terminal counts
    cnt = [0] * (n + 1)
    for u in terminals:
        cnt[u] = 1

    total = 0
    for u in reversed(order):
        if parent[u] == -1:
            continue
        if 0 < cnt[u] < t:
            total += pw[u]
        cnt[parent[u]] += cnt[u]

    print(total)

if __name__ == "__main__":
    solve()