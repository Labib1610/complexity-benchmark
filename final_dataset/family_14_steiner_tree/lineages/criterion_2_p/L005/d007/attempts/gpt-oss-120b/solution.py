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
    focus = set()
    for _ in range(t):
        focus.add(int(next(it)))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for idx in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight of edge to parent
    pedge = [-1] * (n + 1)      # edge index to parent
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w, idx in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            pw[v] = w
            pedge[v] = idx
            stack.append(v)

    cnt = [0] * (n + 1)
    for v in range(1, n + 1):
        if v in focus:
            cnt[v] = 1

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