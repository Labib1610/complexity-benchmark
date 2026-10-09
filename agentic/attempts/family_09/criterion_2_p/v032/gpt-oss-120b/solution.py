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

    # bipartition (graph is guaranteed bipartite)
    color = [-1] * n
    left_ids = []
    right_ids = []
    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                # else: guaranteed consistent
    for i, c in enumerate(color):
        if c == 0:
            left_ids.append(i)
        else:
            right_ids.append(i)

    # map original vertex -> left/right index
    left_index = {v: i for i, v in enumerate(left_ids)}
    right_index = {v: i for i, v in enumerate(right_ids)}
    L = len(left_ids)
    R = len(right_ids)

    # build adjacency for Hopcroft‑Karp (left -> list of right indices)
    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[left_index[u]].append(right_index[v])
        else:
            g[left_index[v]].append(right_index[u])

    # Hopcroft‑Karp
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
        for v in g[u]:
            if not visR[v]:
                visR[v] = True
                pu = pairV[v]
                if pu != -1 and not visL[pu]:
                    visL[pu] = True
                    q.append(pu)

    # vertex cover = (L not visited) U (R visited)
    in_cover = [False] * n
    for i, v in enumerate(left_ids):
        if not visL[i]:
            in_cover[v] = True
    for i, v in enumerate(right_ids):
        if visR[i]:
            in_cover[v] = True

    independent = [i+1 for i in range(n) if not in_cover[i]]
    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()