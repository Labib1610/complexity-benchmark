import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
    color = [0] * n          # bipartite color 0/1
    res = [0] * n            # final 1/2 values

    for start in range(n):
        if visited[start]:
            continue
        # BFS to collect component
        q = deque([start])
        visited[start] = True
        comp = [start]
        while q:
            u = q.popleft()
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    color[w] = color[u] ^ 1
                    q.append(w)
                    comp.append(w)
                else:
                    if color[w] == color[u]:
                        print("NO")
                        return
        # choose orientation: smallest vertex gets 1
        mn = min(comp)
        if color[mn] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            res[v] = map0 if color[v] == 0 else map1

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()