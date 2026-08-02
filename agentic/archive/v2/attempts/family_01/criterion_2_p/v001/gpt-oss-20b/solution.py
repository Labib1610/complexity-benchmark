import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0 or 1 during DFS
    res = [0] * n                   # final team labels (1 or 2)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # Choose orientation: make smallest node 1
        min_node = min(comp)
        min_color = color[min_node]
        for node in comp:
            if (color[node] == 0 and min_color == 0) or (color[node] == 1 and min_color == 1):
                res[node - 1] = 1
            else:
                res[node - 1] = 2

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()