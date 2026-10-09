import sys
from collections import deque

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
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # 1) 2‑colouring
    color = [-1] * (n + 1)          # 0 = left, 1 = right
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

    # map original ids to left/right indices
    left_ids = []
    right_ids = []
    left_index = [0] * (n + 1)
    right_index = [0] * (n + 1)
    for v in range(1, n + 1):
        if color[v] == 0:
            left_index[v] = len(left_ids) + 1   # 1‑based for HK
            left_ids.append(v)
        else:
            right_index[v] = len(right_ids) + 1
            right_ids.append(v)

    L = len(left_ids)
    R = len(right_ids)

    # adjacency for left side using right indices
    G = [[] for _ in range(L + 1)]
    for u in range(1, n + 1):
        if color[u] != 0:
            continue
        lu = left_index[u]
        for v in adj[u]:
            rv = right_index[v]
            if rv:
                G[lu].append(rv)

    # 2) Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (L + 1)
    pairV = [0] * (R + 1)
    dist = [0] * (L + 1)

    def bfs() -> bool:
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

    matching = 0
    while bfs():
        for u in range(1, L + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3) minimum vertex cover
    visL = [False] * (L + 1)
    visR = [False] * (R + 1)
    q = deque()
    for u in range(1, L + 1):
        if pairU[u] == 0:
            q.append(u)
            visL[u] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visR[v] and pairU[u] != v:   # edge not in matching
                visR[v] = True
                pu = pairV[v]
                if pu and not visL[pu]:
                    visL[pu] = True
                    q.append(pu)

    # vertices of minimum vertex cover
    in_cover = [False] * (n + 1)
    for idx, orig in enumerate(left_ids, start=1):
        if not visL[idx]:
            in_cover[orig] = True
    for idx, orig in enumerate(right_ids, start=1):
        if visR[idx]:
            in_cover[orig] = True

    # 4) independent set = complement
    independent = [v for v in range(1, n + 1) if not in_cover[v]]

    if len(independent) < k:
        print("NO")
        return

    print("YES")
    print(" ".join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()