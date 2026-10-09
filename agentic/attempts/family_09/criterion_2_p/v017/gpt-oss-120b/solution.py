import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # bipartition (left/right)
    color = [-1] * n
    left = []
    right = []
    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            while q:
                v = q.popleft()
                (left if color[v] == 0 else right).append(v)
                for nb in adj[v]:
                    if color[nb] == -1:
                        color[nb] = color[v] ^ 1
                        q.append(nb)
    # build adjacency from left to right for matching
    L = len(left)
    R = len(right)
    idxL = {v: i for i, v in enumerate(left)}
    idxR = {v: i for i, v in enumerate(right)}
    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[idxL[u]].append(idxR[v])
        else:
            g[idxL[v]].append(idxR[u])

    # Hopcroft–Karp
    INF = 10**9
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
        reachable = False
        while q:
            u = q.popleft()
            for v in g[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                if pu == -1:
                    reachable = True
        return reachable

    def dfs(u: int) -> bool:
        for v in g[u]:
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

    # find minimum vertex cover
    # BFS from free left vertices in the alternating graph
    visitedL = [False] * L
    visitedR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            q.append(u)
            visitedL[u] = True
    while q:
        u = q.popleft()
        for v in g[u]:
            if not visitedR[v]:
                visitedR[v] = True
                pu = pairV[v]
                if pu != -1 and not visitedL[pu]:
                    visitedL[pu] = True
                    q.append(pu)

    # min vertex cover = (L \ visitedL) ∪ (R ∩ visitedR)
    in_cover = [False] * n
    for i, v in enumerate(left):
        if not visitedL[i]:
            in_cover[v] = True
    for i, v in enumerate(right):
        if visitedR[i]:
            in_cover[v] = True

    independent = [i+1 for i in range(n) if not in_cover[i]]
    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()