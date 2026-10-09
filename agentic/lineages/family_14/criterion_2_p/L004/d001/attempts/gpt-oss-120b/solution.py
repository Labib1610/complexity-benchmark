import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    marked = [0] * (n + 1)
    for _ in range(t):
        marked[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    # Build parent order using stack (root at 1)
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

    # Post-order compute count of marked nodes in subtree
    cnt = [0] * (n + 1)
    for u in reversed(order):
        cnt[u] = marked[u]
        for v, w in adj[u]:
            if parent[v] == u:   # v is child
                cnt[u] += cnt[v]

    total = 0
    for v in range(2, n + 1):
        if 0 < cnt[v] < t:          # edge (parent[v], v) lies between marked nodes
            total += pw[v]

    print(total)

if __name__ == "__main__":
    solve()