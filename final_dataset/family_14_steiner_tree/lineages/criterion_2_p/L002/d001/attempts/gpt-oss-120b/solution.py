import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    terminals = [0] * (n + 1)
    for _ in range(t):
        terminals[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
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
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            pw[v] = w
            stack.append(v)

    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        cnt[i] = terminals[i]

    total = 0
    for u in reversed(order):
        if parent[u] == -1:
            continue
        if cnt[u] > 0 and cnt[u] < t:
            total += pw[u]
        cnt[parent[u]] += cnt[u]

    print(total)

if __name__ == "__main__":
    solve()