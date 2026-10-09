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

    adj_all = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj_all[u].append(v)
        adj_all[v].append(u)
        edges.append((u, v))

    # 1. colour the graph (bipartition)
    colour = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj_all[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)

    # 2. build left/right lists and mapping to indices
    left_vertices = []
    right_vertices = []
    left_id = [-1] * (n + 1)
    right_id = [-1] * (n + 1)

    for v in range(1, n + 1):
        if colour[v] == 0:
            left_id[v] = len(left_vertices)
            left_vertices.append(v)
        else:
            right_id[v] = len(right_vertices)
            right_vertices.append(v)

    L = len(left_vertices)
    R = len(right_vertices)

    # adjacency from left to right (by indices)
    adj = [[] for _ in range(L)]
    for u, v in edges:
        if colour[u] == 0:
            lu = left_id[u]
            rv = right_id[v]
        else:
            lu = left_id[v]
            rv = right_id[u]
        adj[lu].append(rv)

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
        reachable_free = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    reachable_free = True
        return reachable_free

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(L):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    # 4. Build Z (vertices reachable from free left vertices via alternating paths)
    visitedL = [False] * L
    visitedR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            visitedL[u] = True
            q.append(('L', u))

    while q:
        typ, idx = q.popleft()
        if typ == 'L':
            u = idx
            for v in adj[u]:
                if pairU[u] == v:          # matched edge, skip
                    continue
                if not visitedR[v]:
                    visitedR[v] = True
                    q.append(('R', v))
        else:  # 'R'
            v = idx
            pu = pairV[v]
            if pu != -1 and not visitedL[pu]:
                visitedL[pu] = True
                q.append(('L', pu))

    # 5. Independent set = (Left ∩ Z) ∪ (Right \ Z)
    independent = []
    for i, v in enumerate(left_vertices):
        if visitedL[i]:
            independent.append(v)
    for i, v in enumerate(right_vertices):
        if not visitedR[i]:
            independent.append(v)

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()