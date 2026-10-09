import sys
import collections

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    color = [-1] * (n + 1)
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = collections.deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)

    # left side = color 0
    L = [i for i in range(1, n + 1) if color[i] == 0]
    R = [i for i in range(1, n + 1) if color[i] == 1]

    # build adjacency from left to right
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        if color[u] == 0:
            g[u].append(v)
        else:
            g[v].append(u)

    # 2. Hopcroft‑Karp
    pairU = [0] * (n + 1)   # left -> right
    pairV = [0] * (n + 1)   # right -> left
    dist = [0] * (n + 1)

    INF = 10 ** 9

    def bfs() -> bool:
        q = collections.deque()
        for u in L:
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in g[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in g[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in L:
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. minimum vertex cover
    visL = [False] * (n + 1)
    visR = [False] * (n + 1)
    q = collections.deque()
    for u in L:
        if pairU[u] == 0:
            q.append(u)
            visL[u] = True
    while q:
        u = q.popleft()
        if color[u] == 0:          # left vertex, follow non‑matching edges
            for v in g[u]:
                if not visR[v] and pairU[u] != v:
                    visR[v] = True
                    q.append(v)
        else:                      # right vertex, follow matching edge back
            pu = pairV[u]
            if pu and not visL[pu]:
                visL[pu] = True
                q.append(pu)

    cover = set()
    for u in L:
        if not visL[u]:
            cover.add(u)
    for v in R:
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