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

    # bipartition via BFS
    color = [-1] * n
    left_nodes = []
    right_nodes = []
    for i in range(n):
        if color[i] == -1:
            dq = deque([i])
            color[i] = 0
            while dq:
                u = dq.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        dq.append(v)
    for i in range(n):
        if color[i] == 0:
            left_nodes.append(i)
        else:
            right_nodes.append(i)

    L = len(left_nodes)
    R = len(right_nodes)
    # map original index to left/right index
    left_id = {v: idx for idx, v in enumerate(left_nodes)}
    right_id = {v: idx for idx, v in enumerate(right_nodes)}

    # build adjacency for Hopcroft-Karp (left -> list of right indices)
    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[left_id[u]].append(right_id[v])
        else:
            g[left_id[v]].append(right_id[u])

    # Hopcroft-Karp
    INF = 10**9
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L

    def bfs() -> bool:
        dq = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in g[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
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

    # Minimum vertex cover from BFS on alternating paths
    visL = [False] * L
    visR = [False] * R
    dq = deque()
    for u in range(L):
        if pairU[u] == -1:
            dq.append(u)
            visL[u] = True
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if not visR[v] and pairU[u] != v:  # edge not in matching
                visR[v] = True
                pu = pairV[v]
                if pu != -1 and not visL[pu]:
                    visL[pu] = True
                    dq.append(pu)

    # Independent set = (left visited) U (right not visited)
    indep = []
    for idx, u in enumerate(left_nodes):
        if visL[idx]:
            indep.append(u + 1)
    for idx, v in enumerate(right_nodes):
        if not visR[idx]:
            indep.append(v + 1)

    if len(indep) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, indep[:k])))

if __name__ == "__main__":
    solve()