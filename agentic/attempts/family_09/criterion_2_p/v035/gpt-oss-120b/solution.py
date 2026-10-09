import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # 1. colour graph -> bipartition
    colour = [-1] * (n + 1)
    left = []
    right = []
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
        # continue, colours set
    for v in range(1, n + 1):
        if colour[v] == 0:
            left.append(v)
        else:
            right.append(v)

    # map vertex id to index in left/right arrays for fast arrays
    left_id = {v: i+1 for i, v in enumerate(left)}   # 1‑based for HK
    right_id = {v: i+1 for i, v in enumerate(right)}

    L = len(left)
    R = len(right)

    # adjacency for HK using indices
    hk_adj = [[] for _ in range(L + 1)]
    for u in left:
        uid = left_id[u]
        for v in adj[u]:
            hk_adj[uid].append(right_id[v])

    # Hopcroft‑Karp
    pairU = [0] * (L + 1)
    pairV = [0] * (R + 1)
    dist = [0] * (L + 1)

    INF = 10 ** 9

    def bfs():
        q = deque()
        for u in range(1, L + 1):
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in hk_adj[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    def dfs(u):
        if u == 0:
            return True
        for v in hk_adj[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    while bfs():
        for u in range(1, L + 1):
            if pairU[u] == 0:
                dfs(u)

    # 2. minimum vertex cover
    # start from free left vertices
    Lvis = [False] * (L + 1)
    Rvis = [False] * (R + 1)
    q = deque()
    for u in range(1, L + 1):
        if pairU[u] == 0:
            q.append(u)
            Lvis[u] = True
    while q:
        u = q.popleft()
        # from left, follow non‑matching edges
        for v in hk_adj[u]:
            if pairU[u] != v and not Rvis[v]:
                Rvis[v] = True
                # from right, follow matching edge back
                pu = pairV[v]
                if pu and not Lvis[pu]:
                    Lvis[pu] = True
                    q.append(pu)

    # vertices in minimum vertex cover
    in_cover = [False] * (n + 1)
    for v in left:
        idx = left_id[v]
        if not Lvis[idx]:
            in_cover[v] = True
    for v in right:
        idx = right_id[v]
        if Rvis[idx]:
            in_cover[v] = True

    independent = [i for i in range(1, n + 1) if not in_cover[i]]

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()