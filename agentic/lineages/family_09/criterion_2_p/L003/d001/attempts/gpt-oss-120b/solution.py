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
    colour = [-1] * (n + 1)
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    q.append(v)

    # left side = colour 0
    left_nodes = [i for i in range(1, n + 1) if colour[i] == 0]
    is_left = [c == 0 for c in colour]

    # build adjacency from left to right only
    G = [[] for _ in range(n + 1)]
    for u, v in edges:
        if is_left[u]:
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

    sys.setrecursionlimit(1 << 25)
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
        for u in left_nodes:
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. build Z (alternating reachable)
    visitedL = [False] * (n + 1)
    visitedR = [False] * (n + 1)
    q = deque()
    for u in left_nodes:
        if pairU[u] == 0:
            visitedL[u] = True
            q.append(u)          # left side nodes in queue, we store as positive id
    while q:
        u = q.popleft()
        # u is a left vertex
        for v in G[u]:
            if not visitedR[v] and pairU[u] != v:   # edge not in matching
                visitedR[v] = True
                # from right we can go only via matched edge
                pu = pairV[v]
                if pu and not visitedL[pu]:
                    visitedL[pu] = True
                    q.append(pu)

    # 4. minimum vertex cover
    in_cover = [False] * (n + 1)
    for u in left_nodes:
        if not visitedL[u]:
            in_cover[u] = True
    for v in range(1, n + 1):
        if not is_left[v] and visitedR[v]:
            in_cover[v] = True

    independent = [i for i in range(1, n + 1) if not in_cover[i]]

    if len(independent) < k:
        print("NO")
        return

    print("YES")
    print(" ".join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()