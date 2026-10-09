import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

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

    # 1. bipartition by BFS
    colour = [-1] * n
    left = []
    right = []
    for start in range(n):
        if colour[start] != -1:
            continue
        dq = deque([start])
        colour[start] = 0
        while dq:
            v = dq.popleft()
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    dq.append(to)
    for v in range(n):
        if colour[v] == 0:
            left.append(v)
        else:
            right.append(v)

    # build adjacency from left to right
    L = len(left)
    R = len(right)
    idL = [-1] * n
    idR = [-1] * n
    for i, v in enumerate(left):
        idL[v] = i
    for i, v in enumerate(right):
        idR[v] = i

    g = [[] for _ in range(L)]
    for u, v in edges:
        if colour[u] == 0:
            g[idL[u]].append(idR[v])
        else:
            g[idL[v]].append(idR[u])

    # 2. Hopcroft‑Karp
    INF = 10 ** 9
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

    # 3. minimum vertex cover from the matching
    # start from unmatched left vertices
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
            if not visR[v]:
                visR[v] = True
                pu = pairV[v]
                if pu != -1 and not visL[pu]:
                    visL[pu] = True
                    dq.append(pu)

    # cover = (L \ visited) ∪ (R ∩ visited)
    independent = []
    for i, v in enumerate(left):
        if not visL[i]:
            independent.append(v + 1)
    for i, v in enumerate(right):
        if visR[i]:
            independent.append(v + 1)

    if k > len(independent):
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()