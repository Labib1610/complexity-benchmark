import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    terminals = set(int(next(it)) - 1 for _ in range(t))
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    # iterative DFS to get parent order
    parent = [-1] * n
    pw = [0] * n          # weight to parent
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                pw[v] = w
                stack.append(v)

    # count terminals in subtrees
    cnt = [0] * n
    for v in terminals:
        cnt[v] = 1

    total = 0
    for u in reversed(order):
        if u == 0:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if 0 < cnt[u] < t:
            total += pw[u]

    print(total)

if __name__ == "__main__":
    solve()