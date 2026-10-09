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
    specials = [0] * (n + 1)
    total_special = t
    for _ in range(t):
        specials[int(next(it))] = 1
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

    sub_special = [0] * (n + 1)
    ans = 0
    for u in reversed(order):
        cnt = specials[u]
        for v, _, _ in adj[u]:
            if parent[v] == u:
                cnt += sub_special[v]
        sub_special[u] = cnt
        if parent[u] != -1:
            # edge (parent[u], u) is needed if both sides have specials
            if 0 < cnt < total_special:
                ans += pw[u]
    print(ans)

if __name__ == "__main__":
    solve()