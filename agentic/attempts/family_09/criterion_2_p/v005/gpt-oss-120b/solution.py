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

    # bipartition by BFS coloring
    color = [-1] * (n + 1)
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

    left_nodes = [i for i in range(1, n + 1) if color[i] == 0]
    right_nodes = [i for i in range(1, n + 1) if color[i] == 1]

    # adjacency from left to right only
    G = [[] for _ in range(n + 1)]
    for u, v in edges:
        if color[u] == 0:
            G[u].append(v)
        else:
            G[v].append(u)

    INF = 10 ** 9
    pairU = [0] * (n + 1)   # left -> right
    pairV = [0] * (n + 1)   # right -> left
    dist = [0] * (n + 1)

    def bfs() -> bool:
        q = deque()
        for u in left_nodes:
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

    # Hopcroft‑Karp
    while bfs():
        for u in left_nodes:
            if pairU[u] == 0:
                dfs(u)

    # find minimum vertex cover from maximum matching
    visL = [False] * (n + 1)
    visR = [False] * (n + 1)
    q = deque()
    for u in left_nodes:
        if pairU[u] == 0:
            q.append(u)
            visL[u] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visR[v] and pairU[u] != v:   # edge not in matching
                visR[v] = True
                if pairV[v] and not visL[pairV[v]]:
                    visL[pairV[v]] = True
                    q.append(pairV[v])

    # minimum vertex cover
    cover = set()
    for u in left_nodes:
        if not visL[u]:
            cover.add(u)
    for v in right_nodes:
        if visR[v]:
            cover.add(v)

    independent = [i for i in range(1, n + 1) if i not in cover]

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()