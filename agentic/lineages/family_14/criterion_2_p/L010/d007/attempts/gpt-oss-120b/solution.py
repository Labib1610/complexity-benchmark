import sys
sys.setrecursionlimit(300000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    specials = set()
    for _ in range(t):
        specials.add(int(next(it)) - 1)   # zero‑based
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
    for i in range(n):
        if i in specials:
            cnt[i] = 1

    ans = 0
    for u in reversed(order):
        if u == 0:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if 0 < cnt[u] < t:
            ans += pw[u]

    print(ans)

if __name__ == "__main__":
    solve()