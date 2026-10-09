import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
    color = [-1] * n          # 0 = left, 1 = right
    from collections import deque
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

    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    L_id = {v: i for i, v in enumerate(left)}
    R_id = {v: i for i, v in enumerate(right)}
    nl = len(left)
    nr = len(right)

    # build adjacency from left to right indices
    G = [[] for _ in range(nl)]
    for u, v in edges:
        if color[u] == 0:
            G[L_id[u]].append(R_id[v])
        else:
            G[L_id[v]].append(R_id[u])

    # 2. Hopcroft‑Karp
    from collections import deque
    INF = 10 ** 9

    pairU = [-1] * nl
    pairV = [-1] * nr
    dist = [0] * nl

    def bfs() -> bool:
        q = deque()
        for u in range(nl):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reachable = False
        while q:
            u = q.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    reachable = True
        return reachable

    def dfs(u: int) -> bool:
        for v in G[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(nl):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    # 3. minimum vertex cover via alternating BFS
    Lvis = [False] * nl
    Rvis = [False] * nr
    q = deque()
    for u in range(nl):
        if pairU[u] == -1:
            q.append(('L', u))
            Lvis[u] = True
    while q:
        side, idx = q.popleft()
        if side == 'L':
            for v in G[idx]:
                if not Rvis[v] and pairU[idx] != v:   # non‑matching edge
                    Rvis[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            pu = pairV[idx]
            if pu != -1 and not Lvis[pu]:
                Lvis[pu] = True
                q.append(('L', pu))

    # 4. independent set = Lvis ∪ (Right \ Rvis)
    independent = []
    for i, v in enumerate(left):
        if Lvis[i]:
            independent.append(v + 1)
    for i, v in enumerate(right):
        if not Rvis[i]:
            independent.append(v + 1)

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()