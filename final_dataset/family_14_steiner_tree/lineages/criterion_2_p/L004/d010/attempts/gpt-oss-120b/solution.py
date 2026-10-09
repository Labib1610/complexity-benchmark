import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    specials = set(int(next(it)) for _ in range(t))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        node = stack.pop()
        order.append(node)
        for nb, w in adj[node]:
            if nb == parent[node]:
                continue
            parent[nb] = node
            pw[nb] = w
            stack.append(nb)

    cnt = [0] * (n + 1)
    total = 0
    for node in reversed(order):
        cnt[node] = 1 if node in specials else 0
        for nb, w in adj[node]:
            if parent[nb] == node:          # nb is child
                cnt[node] += cnt[nb]
                if 0 < cnt[nb] < t:
                    total += w
    print(total)

if __name__ == "__main__":
    solve()