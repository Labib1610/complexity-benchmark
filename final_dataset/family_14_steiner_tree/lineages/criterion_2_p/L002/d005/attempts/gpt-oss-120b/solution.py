import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1
    t = int(next(it))
    targets = set(int(next(it)) - 1 for _ in range(t))  # zero‑based
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [-1] * n
    pw = [0] * n          # weight of edge to parent
    order = [0]
    parent[0] = 0
    # build traversal order (stack DFS)
    for v in order:
        for to, w in adj[v]:
            if parent[to] == -1:
                parent[to] = v
                pw[to] = w
                order.append(to)

    # post‑order processing
    cnt = [0] * n
    for v in reversed(order):
        cnt[v] = 1 if v in targets else 0
        for to, _ in adj[v]:
            if parent[to] == v:          # child
                cnt[v] += cnt[to]

    total = 0
    for v in range(1, n):
        if 0 < cnt[v] < t:               # edge to parent is needed
            total += pw[v]

    print(total)

if __name__ == "__main__":
    solve()