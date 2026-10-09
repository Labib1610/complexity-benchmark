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

    # 1) bipartition
    color = [-1] * (n + 1)          # 0 = left, 1 = right
    left_nodes = []
    right_nodes = []
    for start in range(1, n + 1):
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
        # after BFS component coloured
    for v in range(1, n + 1):
        if color[v] == 0:
            left_nodes.append(v)
        else:
            right_nodes.append(v)

    # 2) Hopcroft‑Karp
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
        d_augment = INF
        while q:
            u = q.popleft()
            if dist[u] >= d_augment:
                continue
            for v in adj[u]:
                if pairV[v] == 0:
                    d_augment = dist[u] + 1
                elif dist[pairV[v]] == INF:
                    dist[pairV[v]] = dist[u] + 1
                    q.append(pairV[v])
        return d_augment != INF

    def dfs(u: int) -> bool:
        for v in adj[u]:
            if pairV[v] == 0 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
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

    # 3) minimum vertex cover from the matching
    visL = [False] * (n + 1)
    visR = [False] * (n + 1)
    q = deque()
    for u in left_nodes:
        if pairU[u] == 0:
            q.append(u)
            visL[u] = True
    while q:
        u = q.popleft()          # u is left
        for v in adj[u]:
            if not visR[v] and pairU[u] != v:   # edge not in matching
                visR[v] = True
                pu = pairV[v]
                if pu != 0 and not visL[pu]:
                    visL[pu] = True
                    q.append(pu)

    cover = set()
    for u in left_nodes:
        if not visL[u]:
            cover.add(u)
    for v in right_nodes:
        if visR[v]:
            cover.add(v)

    min_cover_size = len(cover)
    # 4) feasibility test
    if k > n - min_cover_size:
        print("NO")
        return

    target = n - k                     # desired cover size
    # enlarge cover arbitrarily
    if len(cover) < target:
        for v in range(1, n + 1):
            if v not in cover:
                cover.add(v)
                if len(cover) == target:
                    break

    independent = [str(v) for v in range(1, n + 1) if v not in cover]
    # independent size must be exactly k
    independent = independent[:k]

    print("YES")
    print(" ".join(independent))

if __name__ == "__main__":
    solve()