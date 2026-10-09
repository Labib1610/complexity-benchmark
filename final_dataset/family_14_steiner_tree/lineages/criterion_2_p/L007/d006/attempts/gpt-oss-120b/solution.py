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
    terminals = set(int(next(it)) for _ in range(t))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for idx in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))
        edges.append((u, v, w))
    if t <= 1:
        print(0)
        return

    total_term = t
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w, _ in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            pw[v] = w
            stack.append(v)

    sub_cnt = [0] * (n + 1)
    for u in reversed(order):
        cnt = 1 if u in terminals else 0
        for v, _, _ in adj[u]:
            if parent[v] == u:
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt

    ans = 0
    for v in range(2, n + 1):
        cnt = sub_cnt[v]
        if 0 < cnt < total_term:
            ans += pw[v]
    print(ans)

if __name__ == "__main__":
    solve()