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
    color = [-1] * n  # 0 left, 1 right
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
    L, R = len(left), len(right)
    # map original index to left/right ids
    lid = [-1] * n
    rid = [-1] * n
    for idx, v in enumerate(left):
        lid[v] = idx
    for idx, v in enumerate(right):
        rid[v] = idx

    # build adjacency from left to right ids
    G = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            G[lid[u]].append(rid[v])
        else:
            G[lid[v]].append(rid[u])

    # Hopcroft–Karp
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

    # minimum vertex cover from BFS on alternating graph
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

    # min vertex cover = (L visited) U (R not visited)
    # max independent set = (L not visited) U (R visited)
    indep = []
    for idx, v in enumerate(left):
        if not visL[idx]:
            indep.append(v)
    for idx, v in enumerate(right):
        if visR[idx]:
            indep.append(v)

    if len(indep) < k:
        print("NO")
        return
    print("YES")
    ans = [str(v + 1) for v in indep[:k]]
    print(" ".join(ans))

if __name__ == "__main__":
    solve()