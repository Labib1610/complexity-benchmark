import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # m = n-1, tree
    t = int(next(it))
    anchors = set(int(next(it)) - 1 for _ in range(t))  # zero‑based
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    deg = [len(adj[i]) for i in range(n)]
    removed = [False] * n
    q = deque([i for i in range(n) if deg[i] == 1 and i not in anchors])

    while q:
        v = q.popleft()
        if removed[v]:
            continue
        removed[v] = True
        for nb, _ in adj[v]:
            if removed[nb]:
                continue
            deg[nb] -= 1
            if deg[nb] == 1 and nb not in anchors:
                q.append(nb)

    ans = 0
    for u, v, w in edges:
        if not removed[u] and not removed[v]:
            ans += w
    print(ans)

if __name__ == "__main__":
    solve()