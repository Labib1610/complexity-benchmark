import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    # bipartition via BFS coloring
    color = [-1] * n
    left_nodes = []
    right_nodes = []
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
    left_nodes = [i for i in range(n) if color[i] == 0]
    right_nodes = [i for i in range(n) if color[i] == 1]

    # map original indices to left/right ids
    lid = {v: i for i, v in enumerate(left_nodes)}
    rid = {v: i for i, v in enumerate(right_nodes)}
    L = len(left_nodes)
    R = len(right_nodes)

    # build adjacency for Hopcroft-Karp (left -> right ids)
    g = [[] for _ in range(L)]
    for u in left_nodes:
        for v in adj[u]:
            if color[v] == 1:
                g[lid[u]].append(rid[v])

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

    # Minimum vertex cover from matching
    # start from free left vertices, follow alternating paths
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
            if not visR[v] and pairU[u] != v:  # edge not in matching
                visR[v] = True
                pu = pairV[v]
                if pu != -1 and not visL[pu]:
                    visL[pu] = True
                    q.append(pu)

    # vertex cover = (Left \ visL) ∪ (Right ∩ visR)
    in_cover = [False] * n
    for i, u in enumerate(left_nodes):
        if not visL[i]:
            in_cover[u] = True
    for i, v in enumerate(right_nodes):
        if visR[i]:
            in_cover[v] = True

    independent = [i+1 for i in range(n) if not in_cover[i]]
    if len(independent) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()