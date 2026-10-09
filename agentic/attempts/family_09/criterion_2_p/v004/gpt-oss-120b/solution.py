import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    col = [-1] * (n + 1)
    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        col[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if col[v] == -1:
                    col[v] = col[u] ^ 1
                    q.append(v)

    left = [i for i in range(1, n + 1) if col[i] == 0]
    right = [i for i in range(1, n + 1) if col[i] == 1]

    # adjacency from left to right
    adjL = [[] for _ in range(n + 1)]
    for u, v in edges:
        if col[u] == 0:
            adjL[u].append(v)
        else:
            adjL[v].append(u)

    # 2. Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (n + 1)   # left -> right
    pairV = [0] * (n + 1)   # right -> left
    dist = [0] * (n + 1)

    def bfs() -> bool:
        q = deque()
        for u in left:
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adjL[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adjL[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in left:
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. Build Z (alternating reachable set)
    visitedL = [False] * (n + 1)
    visitedR = [False] * (n + 1)
    q = deque()
    for u in left:
        if pairU[u] == 0:
            visitedL[u] = True
            q.append(('L', u))
    while q:
        side, x = q.popleft()
        if side == 'L':
            for v in adjL[x]:
                if not visitedR[v] and pairU[x] != v:   # non‑matching edge
                    visitedR[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            pu = pairV[x]
            if pu and not visitedL[pu]:
                visitedL[pu] = True
                q.append(('L', pu))

    # 4. independent set = (L∩Z) ∪ (R\Z)
    indep = []
    for u in left:
        if visitedL[u]:
            indep.append(u)
    for v in right:
        if not visitedR[v]:
            indep.append(v)

    if len(indep) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, indep[:k])))

if __name__ == "__main__":
    solve()