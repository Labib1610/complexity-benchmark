import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u == v:          # self‑loop impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0 / 1 bipartite colors
    ans = [0] * (n + 1)             # final concentrations
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation to make lexicographically smallest
        min_idx = min(comp)
        if color[min_idx] == 0:
            # 0 -> 1, 1 -> 2
            for v in comp:
                ans[v] = 1 if color[v] == 0 else 2
        else:
            # flip: 1 -> 1, 0 -> 2
            for v in comp:
                ans[v] = 1 if color[v] == 1 else 2

    # isolated vertices (no edges) already handled: they are single‑node components,
    # color 0, min_idx = that vertex, so assigned 1.

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()