import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    targets = [int(next(it)) - 1 for _ in range(t)]
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    if t <= 1:
        print(0)
        return

    target_mark = [0] * n
    for x in targets:
        target_mark[x] = 1

    parent = [-1] * n
    pw = [0] * n          # weight to parent
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                pw[v] = w
                stack.append(v)

    cnt = [0] * n
    for u in reversed(order):
        cnt[u] += target_mark[u]
        if u != 0:
            cnt[parent[u]] += cnt[u]

    total = 0
    for v in range(1, n):
        c = cnt[v]
        if 0 < c < t:
            total += pw[v]
    print(total)

if __name__ == "__main__":
    solve()