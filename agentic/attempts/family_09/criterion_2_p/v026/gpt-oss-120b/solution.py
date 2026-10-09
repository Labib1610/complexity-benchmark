import sys
import collections

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj_all = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj_all[u].append(v)
        adj_all[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    colour = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = collections.deque([start])
        while q:
            u = q.popleft()
            for v in adj_all[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    q.append(v)

    # Build adjacency from left to right
    left_nodes = [i for i in range(1, n + 1) if colour[i] == 0]
    right_nodes = [i for i in range(1, n + 1) if colour[i] == 1]

    # map original ids to 0‑based indices inside each part
    left_id = {v: idx for idx, v in enumerate(left_nodes)}
    right_id = {v: idx for idx, v in enumerate(right_nodes)}

    L = len(left_nodes)
    R = len(right_nodes)
    adj = [[] for _ in range(L)]
    for u, v in edges:
        if colour[u] == 0:
            adj[left_id[u]].append(right_id[v])
        else:
            adj[left_id[v]].append(right_id[u])

    # 2. Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [ -1 ] * L
    pairV = [ -1 ] * R
    dist = [0] * L

    from collections import deque

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
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    reachable = True
        return reachable

    def dfs(u: int) -> bool:
        for v in adj[u]:
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

    # 3. Build alternating reachability from free left vertices
    visL = [False] * L
    visR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            visL[u] = True
            q.append(('L', u))

    while q:
        side, idx = q.popleft()
        if side == 'L':
            u = idx
            for v in adj[u]:
                if not visR[v] and pairU[u] != v:   # edge not in matching
                    visR[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            v = idx
            pu = pairV[v]
            if pu != -1 and not visL[pu]:
                visL[pu] = True
                q.append(('L', pu))

    # 4. Independent set = (L∩visL) ∪ (R\visR)
    independent = []
    for i, u in enumerate(left_nodes):
        if visL[i]:
            independent.append(u)
    for i, v in enumerate(right_nodes):
        if not visR[i]:
            independent.append(v)

    if matching <= n - k:
        # we have enough vertices
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()