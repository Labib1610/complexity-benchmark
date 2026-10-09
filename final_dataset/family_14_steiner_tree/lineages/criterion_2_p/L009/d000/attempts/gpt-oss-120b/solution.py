import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # equals n-1
    t = int(next(it))
    terminals = set()
    for _ in range(t):
        terminals.add(int(next(it)) - 1)  # zero‑based
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w, len(edges)))
        adj[v].append((u, w, len(edges)))
        edges.append((u, v, w))

    parent = [-1] * n
    parent_edge = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w, idx in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_edge[v] = idx
                stack.append(v)

    sub_cnt = [0] * n
    for u in reversed(order):
        cnt = 1 if u in terminals else 0
        for v, w, idx in adj[u]:
            if parent[v] == u:  # child
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt

    total_term = t
    ans = 0
    for v in range(1, n):
        cnt = sub_cnt[v]
        if cnt > 0 and total_term - cnt > 0:
            ans += edges[parent_edge[v]][2]

    print(ans)

if __name__ == "__main__":
    solve()