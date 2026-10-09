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
    T = set()
    for _ in range(t):
        T.add(int(next(it)) - 1)  # zero‑based
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
    for v in T:
        cnt[v] = 1

    ans = 0
    # process in reverse order (post‑order)
    for u in reversed(order):
        if u == 0:
            continue
        p = parent[u]
        if cnt[u] > 0 and t - cnt[u] > 0:
            ans += pw[u]
        cnt[p] += cnt[u]

    print(ans)

if __name__ == "__main__":
    solve()