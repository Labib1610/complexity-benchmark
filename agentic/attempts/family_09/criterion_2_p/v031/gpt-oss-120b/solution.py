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

    # 1. bipartition
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)

    # map to left/right indices
    left_id = [-1] * n
    right_id = [-1] * n
    L = R = 0
    for v in range(n):
        if color[v] == 0:
            left_id[v] = L
            L += 1
        else:
            right_id[v] = R
            R += 1

    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[left_id[u]].append(right_id[v])
        else:
            g[left_id[v]].append(right_id[u])

    # 2. Hopcroft‑Karp
    INF = 10 ** 9
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
        found = False
        while q:
            u = q.popleft()
            for v in g[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                if pu == -1:
                    found = True
        return found

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

    # 3. minimum vertex cover via alternating bfs
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

    # 4. independent set = (L visited) ∪ (R not visited)
    independent = []
    for v in range(n):
        if color[v] == 0:
            if visL[left_id[v]]:
                independent.append(v + 1)
        else:
            if not visR[right_id[v]]:
                independent.append(v + 1)

    if len(independent) < k:
        print("NO")
        return
    print("YES")
    print(" ".join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()