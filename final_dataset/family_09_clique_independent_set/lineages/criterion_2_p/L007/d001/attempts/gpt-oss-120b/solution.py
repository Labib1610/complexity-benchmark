import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))

    g = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)
        edges.append((u, v))

    # colour the graph (0/1)
    colour = [-1] * (n + 1)
    left_nodes = []
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        dq = deque([start])
        while dq:
            u = dq.popleft()
            for v in g[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    dq.append(v)

    # build adjacency from left (colour 0) to right (colour 1)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        if colour[u] == 0:
            adj[u].append(v)
        else:
            adj[v].append(u)

    # Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (n + 1)   # left -> right
    pairV = [0] * (n + 1)   # right -> left
    dist = [0] * (n + 1)

    left_list = [i for i in range(1, n + 1) if colour[i] == 0]

    def bfs() -> bool:
        dq = deque()
        for u in left_list:
            if pairU[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu == 0:
                    found = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
        return found

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pairV[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in left_list:
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # minimum vertex cover
    visitedU = [False] * (n + 1)
    visitedV = [False] * (n + 1)
    dq = deque()
    for u in left_list:
        if pairU[u] == 0:
            visitedU[u] = True
            dq.append(u)
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if not visitedV[v] and pairU[u] != v:   # non‑matching edge
                visitedV[v] = True
                pu = pairV[v]
                if pu and not visitedU[pu]:
                    visitedU[pu] = True
                    dq.append(pu)

    cover = set()
    for u in left_list:
        if not visitedU[u]:
            cover.add(u)
    for v in range(1, n + 1):
        if colour[v] == 1 and visitedV[v]:
            cover.add(v)

    independent = [i for i in range(1, n + 1) if i not in cover]

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()