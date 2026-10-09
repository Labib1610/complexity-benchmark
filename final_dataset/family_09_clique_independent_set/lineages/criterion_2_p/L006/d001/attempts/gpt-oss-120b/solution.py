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
    left = []
    right = []
    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            while q:
                v = q.popleft()
                for to in adj[v]:
                    if color[to] == -1:
                        color[to] = color[v] ^ 1
                        q.append(to)
    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]

    # build adjacency from left to right
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

    # Hopcroft-Karp
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

    # find minimum vertex cover via alternating BFS
    visitedL = [False] * L
    visitedR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            q.append(('L', u))
            visitedL[u] = True
    while q:
        side, v = q.popleft()
        if side == 'L':
            for to in g[v]:
                if not visitedR[to] and pairU[v] != to:  # edge not in matching
                    visitedR[to] = True
                    q.append(('R', to))
        else:  # side R
            pu = pairV[v]
            if pu != -1 and not visitedL[pu]:
                visitedL[pu] = True
                q.append(('L', pu))

    # independent set = (L ∩ visitedL) ∪ (R \ visitedR)
    indep = []
    for i, v in enumerate(left):
        if visitedL[i]:
            indep.append(v + 1)
    for i, v in enumerate(right):
        if not visitedR[i]:
            indep.append(v + 1)

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()