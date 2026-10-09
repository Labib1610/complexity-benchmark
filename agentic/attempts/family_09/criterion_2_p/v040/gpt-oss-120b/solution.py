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

    # 2‑color the graph (it is bipartite by guarantee)
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                v = q.popleft()
                for to in adj[v]:
                    if color[to] == -1:
                        color[to] = color[v] ^ 1
                        q.append(to)

    # map original ids to left/right indices
    left_ids = [i for i in range(n) if color[i] == 0]
    right_ids = [i for i in range(n) if color[i] == 1]
    L = len(left_ids)
    R = len(right_ids)
    lid = [-1] * n
    rid = [-1] * n
    for idx, v in enumerate(left_ids):
        lid[v] = idx
    for idx, v in enumerate(right_ids):
        rid[v] = idx

    # build adjacency for left side using right indices
    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[lid[u]].append(rid[v])
        else:
            g[lid[v]].append(rid[u])

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
                elif pu == -1:
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

    # Minimum vertex cover from maximum matching
    # start from unmatched left vertices, follow alternating paths
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

    # Vertex cover = (L not visited) ∪ (R visited)
    cover = set()
    for idx, v in enumerate(left_ids):
        if not visL[idx]:
            cover.add(v)
    for idx, v in enumerate(right_ids):
        if visR[idx]:
            cover.add(v)

    independent = [i+1 for i in range(n) if i not in cover]
    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()