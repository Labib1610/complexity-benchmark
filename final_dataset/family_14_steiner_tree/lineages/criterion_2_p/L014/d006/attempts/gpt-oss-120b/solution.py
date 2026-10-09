import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    specials = [0] * (n + 1)
    for _ in range(t):
        specials[int(next(it))] = 1
    adj = [[] for _ in range(n + 1)]
    edges = []
    for eid in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w, eid))
        adj[v].append((u, w, eid))
        edges.append((u, v, w))
    if t <= 1:
        print(0)
        return

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

    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        cnt[i] = specials[i]

    total_special = t
    ans = 0
    for u in reversed(order):
        if parent[u] == -1:
            continue
        if 0 < cnt[u] < total_special:
            ans += pw[u]
        cnt[parent[u]] += cnt[u]

    print(ans)

if __name__ == "__main__":
    solve()