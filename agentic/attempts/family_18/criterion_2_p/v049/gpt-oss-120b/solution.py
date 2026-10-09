import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # root the tree at 1 and get a DFS order
    order = []
    parent = [0] * (n + 1)
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)

    # assign positions according to the order (1‑based)
    pos = [0] * (n + 1)
    for idx, node in enumerate(order, 1):
        pos[node] = idx

    # compute total wait time
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])

    if total <= B:
        out = ["YES"]
        out.append(" ".join(str(pos[i]) for i in range(1, n + 1)))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()