import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. bipartition by BFS colouring
    colour = [-1] * n          # 0 = left, 1 = right
    left_ids = []              # original vertex numbers (1‑based) of left side
    right_ids = []             # same for right side
    left_index = [-1] * n
    right_index = [-1] * n

    for start in range(n):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        while q:
            v = q.popleft()
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)

    # build lists of vertices per side
    for v in range(n):
        if colour[v] == 0:
            left_index[v] = len(left_ids)
            left_ids.append(v + 1)
        else:
            right_index[v] = len(right_ids)
            right_ids.append(v + 1)

    L = len(left_ids)
    R = len(right_ids)

    # 2. adjacency from left to right (indices)
    g = [[] for _ in range(L)]
    for u, v in edges:
        if colour[u] == 0:          # u in left, v in right
            g[left_index[u]].append(right_index[v])
        else:                       # v in left, u in right
            g[left_index[v]].append(right_index[u])

    # 3. Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L

    def bfs() -> bool:
        q = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in g[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    sys.setrecursionlimit(1_000_000)

    def dfs(u: int) -> bool:
        for v in g[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    while bfs():
        for u in range(L):
            if pairU[u] == -1:
                dfs(u)

    # 4. minimum vertex cover via König's construction
    visitedL = [False] * L
    visitedR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            visitedL[u] = True
            q.append(('L', u))

    while q:
        side, x = q.popleft()
        if side == 'L':
            for v in g[x]:
                if not visitedR[v] and pairU[x] != v:   # non‑matched edge
                    visitedR[v] = True
                    q.append(('R', v))
        else:   # side == 'R'
            u = pairV[x]
            if u != -1 and not visitedL[u]:
                visitedL[u] = True
                q.append(('L', u))

    # 5. maximum independent set = visitedL ∪ (R \ visitedR)
    independent = []
    for i, ok in enumerate(visitedL):
        if ok:
            independent.append(left_ids[i])
    for i, ok in enumerate(visitedR):
        if not ok:
            independent.append(right_ids[i])

    if len(independent) >= k:
        print("YES")
        print(" ".join(map(str, independent[:k])))
    else:
        print("NO")


if __name__ == "__main__":
    solve()