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

    side = [-1] * (n + 1)          # temporary bipartition side 0/1
    color = [0] * (n + 1)          # final grades 1/2
    q = deque()

    for start in range(1, n + 1):
        if side[start] != -1:
            continue
        # start new component
        comp = []
        side[start] = 0
        q.append(start)
        bip = True
        while q:
            v = q.popleft()
            comp.append(v)
            for to in adj[v]:
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    # not bipartite
                    print("NO")
                    return
        # choose orientation to make smallest index vertex colour 1
        min_idx = min(comp)
        s = side[min_idx]          # side (0 or 1) of that vertex
        # mapping: side == s -> 1, else -> 2
        for v in comp:
            color[v] = 1 if side[v] == s else 2

    # all components processed, graph bipartite
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()