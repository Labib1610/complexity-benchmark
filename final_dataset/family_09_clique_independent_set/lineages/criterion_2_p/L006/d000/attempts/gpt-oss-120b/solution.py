import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj_all = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_all[u].append(v)
        adj_all[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    color = [-1] * n
    L = []
    R = []
    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        while q:
            v = q.popleft()
            for to in adj_all[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
        # component coloured
    for v in range(n):
        if color[v] == 0:
            L.append(v)
        else:
            R.append(v)

    # map left vertices to 0..len(L)-1 for HK
    left_id = {v: i for i, v in enumerate(L)}
    right_id = {v: i for i, v in enumerate(R)}
    nl = len(L)
    nr = len(R)
    adj = [[] for _ in range(nl)]
    for u, v in edges:
        if color[u] == 0:
            adj[left_id[u]].append(right_id[v])
        else:
            adj[left_id[v]].append(right_id[u])

    # 2. Hopcroft‑Karp
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
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                if pu == -1:
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
        for u in range(nl):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    # 3. minimum vertex cover via alternating BFS
    visL = [False] * nl
    visR = [False] * nr
    q = deque()
    for u in range(nl):
        if pairU[u] == -1:
            q.append(('L', u))
            visL[u] = True
    while q:
        side, idx = q.popleft()
        if side == 'L':
            for v in adj[idx]:
                if not visR[v] and pairU[idx] != v:   # edge not in matching
                    visR[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            pu = pairV[idx]
            if pu != -1 and not visL[pu]:
                visL[pu] = True
                q.append(('L', pu))

    # independent set = (L ∩ visL) ∪ (R \ visR)
    indep = []
    for i, v in enumerate(L):
        if visL[i]:
            indep.append(v + 1)
    for i, v in enumerate(R):
        if not visR[i]:
            indep.append(v + 1)

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()