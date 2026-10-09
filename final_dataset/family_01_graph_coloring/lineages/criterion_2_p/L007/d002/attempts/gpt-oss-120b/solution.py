import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    colour = [0] * n          # 0 / 1 inside a component
    ans = [0] * n

    for start in range(n):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        visited[start] = True
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if not visited[to]:
                    visited[to] = True
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == colour[v]:
                    # not bipartite
                    print("NO")
                    return
        # choose orientation: smallest index gets value 1
        min_v = min(comp)
        if colour[min_v] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            ans[v] = map0 if colour[v] == 0 else map1

    # all components processed
    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()