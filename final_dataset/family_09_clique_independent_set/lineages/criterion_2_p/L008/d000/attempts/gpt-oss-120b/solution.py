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

    # bipartition via BFS
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    L = len(left)
    R = len(right)
    # map original index to left/right ids
    lid = {v: idx for idx, v in enumerate(left)}
    rid = {v: idx for idx, v in enumerate(right)}

    G = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            G[lid[u]].append(rid[v])
        else:
            G[lid[v]].append(rid[u])

    # Hopcroft-Karp
    INF = 10**9
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L

    def bfs():
        q = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v in G[u]:
                    if pairV[v] == -1:
                        d = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return d != INF

    def dfs(u):
        for v in G[u]:
            pu = pairV[v]
            if pairV[v] == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
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

    # find min vertex cover
    # BFS in alternating graph from free left vertices
    visL = [False] * L
    visR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            q.append(u)
            visL[u] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visR[v]:
                visR[v] = True
                if pairV[v] != -1 and not visL[pairV[v]]:
                    visL[pairV[v]] = True
                    q.append(pairV[v])

    # min vertex cover = (L \ visL) U (visR)
    # max independent set = visL U (R \ visR)
    indep = []
    for idx, u in enumerate(left):
        if visL[idx]:
            indep.append(u + 1)
    for idx, v in enumerate(right):
        if not visR[idx]:
            indep.append(v + 1)

    if len(indep) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, indep[:k])))

if __name__ == "__main__":
    solve()