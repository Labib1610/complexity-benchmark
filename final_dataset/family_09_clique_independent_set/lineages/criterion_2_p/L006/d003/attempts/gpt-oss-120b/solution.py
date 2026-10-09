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
    color = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)

    left = [i for i in range(1, n + 1) if color[i] == 0]
    # build adjacency from left to right only
    G = [[] for _ in range(n + 1)]
    for u, v in edges:
        if color[u] == 0:
            G[u].append(v)
        else:
            G[v].append(u)

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
                for v in G[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in G[u]:
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

    # 3. build Z (vertices reachable from unmatched left via alternating paths)
    visitedL = [False] * (n + 1)
    visitedR = [False] * (n + 1)
    q = deque()
    for u in left:
        if pairU[u] == 0:
            visitedL[u] = True
            q.append(('L', u))
    while q:
        side, v = q.popleft()
        if side == 'L':
            for to in G[v]:
                if not visitedR[to] and pairU[v] != to:   # edge not in matching
                    visitedR[to] = True
                    q.append(('R', to))
        else:  # side == 'R'
            pu = pairV[v]
            if pu and not visitedL[pu]:
                visitedL[pu] = True
                q.append(('L', pu))

    # 4. minimum vertex cover
    cover = [False] * (n + 1)
    for u in left:
        if not visitedL[u]:
            cover[u] = True          # L \ Z
    for v in range(1, n + 1):
        if color[v] == 1 and visitedR[v]:
            cover[v] = True          # R ∩ Z

    # 5. independent set
    independent = [i for i in range(1, n + 1) if not cover[i]]

    if len(independent) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()