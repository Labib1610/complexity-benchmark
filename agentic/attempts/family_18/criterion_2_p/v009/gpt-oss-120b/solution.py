import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # BFS order starting from node 1
    order = []
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    while q:
        v = q.popleft()
        order.append(v)
        for nb in adj[v]:
            if not visited[nb]:
                visited[nb] = True
                q.append(nb)

    # positions are 1‑based
    pos = [0] * (n + 1)
    for idx, node in enumerate(order):
        pos[node] = idx + 1

    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])

    out = []
    if total <= B:
        out.append("YES")
        out.append(" ".join(str(pos[i]) for i in range(1, n + 1)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()