import sys
from collections import deque

def solve() -> None:
    sys.setrecursionlimit(1 << 25)
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

    # bipartition
    color = [-1] * n
    left_nodes = []
    right_nodes = []
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
    for i in range(n):
        if color[i] == 0:
            left_nodes.append(i)
        else:
            right_nodes.append(i)

    # build adjacency from left to right (indices in original graph)
    L = len(left_nodes)
    R = len(right_nodes)
    left_id = {v: idx for idx, v in enumerate(left_nodes)}
    right_id = {v: idx for idx, v in enumerate(right_nodes)}
    g = [[] for _ in range(L)]
    for u in left_nodes:
        uid = left_id[u]
        for v in adj[u]:
            if color[v] == 1:
                g[uid].append(right_id[v])

    # Hopcroft-Karp
    INF = 10**9
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L

    def bfs():
        q = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v in g[u]:
                    if pairV[v] == -1:
                        d = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return d != INF

    def dfs(u):
        for v in g[u]:
            if pairV[v] == -1 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
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
                if pairV[v] != -1 and not visL[pairV[v]]:
                    visL[pairV[v]] = True
                    q.append(pairV[v])

    # vertex cover = (L not visited) U (R visited)
    in_cover = [False] * n
    for idx, u in enumerate(left_nodes):
        if not visL[idx]:
            in_cover[u] = True
    for idx, v in enumerate(right_nodes):
        if visR[idx]:
            in_cover[v] = True

    independent = [i+1 for i in range(n) if not in_cover[i]]
    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()