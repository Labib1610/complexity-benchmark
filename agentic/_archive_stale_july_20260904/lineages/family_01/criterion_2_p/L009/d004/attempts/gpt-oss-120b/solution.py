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
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 unvisited, 0/1 two colours
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == cu:
                    # not bipartite
                    print("NO")
                    return
        # choose mapping: smallest index gets value 1
        min_v = min(comp)
        c_min = colour[min_v]
        for v in comp:
            ans[v] = 1 if colour[v] == c_min else 2

    # isolated vertices (no edges) are already handled: they form a component of size 1
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()