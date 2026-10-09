import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))

    g = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    color = [-1] * (n + 1)
    left = []
    right = []
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        dq = deque([start])
        color[start] = 0
        while dq:
            u = dq.popleft()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    dq.append(v)
        # continue, all vertices will be coloured

    for v in range(1, n + 1):
        if color[v] == 0:
            left.append(v)
        else:
            right.append(v)

    # map vertex id -> index in left/right arrays (1‑based for HK)
    lid = {v: i + 1 for i, v in enumerate(left)}
    rid = {v: i + 1 for i, v in enumerate(right)}
    L = len(left)
    R = len(right)

    adj = [[] for _ in range(L + 1)]
    for u, v in edges:
        if color[u] == 0:
            adj[lid[u]].append(rid[v])
        else:
            adj[lid[v]].append(rid[u])

    # 2. Hopcroft‑Karp
    pairU = [0] * (L + 1)
    pairV = [0] * (R + 1)
    dist = [0] * (L + 1)

    INF = 10 ** 9

    def bfs() -> bool:
        dq = deque()
        for u in range(1, L + 1):
            if pairU[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if pairV[v] == 0:
                    reachable = True
                elif dist[pairV[v]] == INF:
                    dist[pairV[v]] = dist[u] + 1
                    dq.append(pairV[v])
        return reachable

    def dfs(u: int) -> bool:
        for v in adj[u]:
            if pairV[v] == 0 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, L + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. build Z (alternating reachable set)
    visL = [False] * (L + 1)
    visR = [False] * (R + 1)
    dq = deque()
    for u in range(1, L + 1):
        if pairU[u] == 0:
            dq.append(('L', u))
            visL[u] = True
    while dq:
        side, x = dq.popleft()
        if side == 'L':
            for v in adj[x]:
                if not visR[v] and pairU[x] != v:   # non‑matched edge
                    visR[v] = True
                    dq.append(('R', v))
        else:  # side == 'R'
            pu = pairV[x]
            if pu and not visL[pu]:
                visL[pu] = True
                dq.append(('L', pu))

    # 4. independent set = (L visited) ∪ (R not visited)
    indep = []
    for v in left:
        if visL[lid[v]]:
            indep.append(v)
    for v in right:
        if not visR[rid[v]]:
            indep.append(v)

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()