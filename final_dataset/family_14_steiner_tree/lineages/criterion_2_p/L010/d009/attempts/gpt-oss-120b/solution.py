import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    targets = [int(next(it)) - 1 for _ in range(t)]
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w, len(edges)))
        adj[v].append((u, w, len(edges)))
        edges.append((u, v, w))

    if t <= 1:
        print(0)
        return

    is_target = [0] * n
    for v in targets:
        is_target[v] = 1

    parent = [-1] * n
    parent_edge = [-1] * n
    order = []
    stack = [0]
    parent[0] = -2  # visited marker
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
        cnt = is_target[u]
        for v, w, idx in adj[u]:
            if parent[v] == u:  # child
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt

    total = 0
    for v in range(1, n):
        cnt = sub_cnt[v]
        if 0 < cnt < t:
            # edge between v and parent[v] is needed
            total += edges[parent_edge[v]][2]

    print(total)

if __name__ == "__main__":
    solve()