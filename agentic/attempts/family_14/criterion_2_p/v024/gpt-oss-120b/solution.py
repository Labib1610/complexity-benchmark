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
    terminals = [0] * (n + 1)
    for _ in range(t):
        terminals[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    edges = []
    for idx in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))
        edges.append((u, v, w))

    parent = [0] * (n + 1)
    parent_edge_w = [0] * (n + 1)
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
            parent_edge_w[v] = w
            stack.append(v)

    sub_cnt = [0] * (n + 1)
    ans = 0
    for u in reversed(order):
        cnt = terminals[u]
        for v, w, _ in adj[u]:
            if parent[v] == u:  # child
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt
        if u != 1:
            # edge between u and parent[u] has weight parent_edge_w[u]
            if 0 < cnt < t:
                ans += parent_edge_w[u]

    print(ans)

if __name__ == "__main__":
    solve()