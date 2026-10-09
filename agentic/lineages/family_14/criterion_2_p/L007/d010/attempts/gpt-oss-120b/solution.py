import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = set(int(next(it)) - 1 for _ in range(t))
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

    parent = [-1] * n
    parent_edge = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        node = stack.pop()
        order.append(node)
        for nb, w, idx in adj[node]:
            if parent[nb] == -1:
                parent[nb] = node
                parent_edge[nb] = idx
                stack.append(nb)

    sub_cnt = [0] * n
    for v in targets:
        sub_cnt[v] = 1

    ans = 0
    for node in reversed(order):
        if node == 0:
            continue
        cnt = sub_cnt[node]
        if 0 < cnt < t:
            ans += edges[parent_edge[node]][2]
        sub_cnt[parent[node]] += cnt

    print(ans)

if __name__ == "__main__":
    solve()