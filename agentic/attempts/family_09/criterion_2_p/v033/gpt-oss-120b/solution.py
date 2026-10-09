import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # bipartition via BFS
    color = [-1] * n
    left = []
    right = []
    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]

    # build adjacency from left to right indices
    L = len(left)
    R = len(right)
    lid = {v: i for i, v in enumerate(left)}
    rid = {v: i for i, v in enumerate(right)}
    g = [[] for _ in range(L)]
    for u in left:
        for v in adj[u]:
            g[lid[u]].append(rid[v])

    # Hopcroft-Karp
    INF = 10**9
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L

    def bfs():
        dq = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        d = INF
        while dq:
            u = dq.popleft()
            if dist[u] < d:
                for v in g[u]:
                    if pairV[v] == -1:
                        d = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        dq.append(pairV[v])
        return d != INF

    def dfs(u):
        for v in g[u]:
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
    # start from free left vertices, follow alternating paths
    visL = [False] * L
    visR = [False] * R
    dq = deque()
    for u in range(L):
        if pairU[u] == -1:
            dq.append(u)
            visL[u] = True
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if not visR[v] and pairU[u] != v:  # edge not in matching
                visR[v] = True
                pu = pairV[v]
                if pu != -1 and not visL[pu]:
                    visL[pu] = True
                    dq.append(pu)

    # independent set = (L ∩ Z) ∪ (R \ Z)
    indep = []
    for idx, u in enumerate(left):
        if visL[idx]:
            indep.append(u + 1)
    for idx, v in enumerate(right):
        if not visR[idx]:
            indep.append(v + 1)

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()