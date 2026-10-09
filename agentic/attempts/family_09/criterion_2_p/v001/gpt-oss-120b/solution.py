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

    # bipartition via BFS coloring
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
    lid = {v: i for i, v in enumerate(left)}
    rid = {v: i for i, v in enumerate(right)}

    # build adjacency for HK (left -> right ids)
    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[lid[u]].append(rid[v])
        else:
            g[lid[v]].append(rid[u])

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
    # start from free left vertices, follow alternating paths
    visL = [False] * L
    visR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            q.append(u)
            visL[u] = True
    while q:
        u = q.popleft()
        for v in g[u]:
            if not visR[v] and pairU[u] != v:  # edge not in matching
                visR[v] = True
                pu = pairV[v]
                if pu != -1 and not visL[pu]:
                    visL[pu] = True
                    q.append(pu)

    # independent set = (L visited) ∪ (R not visited)
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