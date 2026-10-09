import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj_full = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj_full[u].append(v)
        adj_full[v].append(u)
        edges.append((u, v))

    # 0/1 coloring (bipartition)
    color = [-1] * (n + 1)
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0
        dq = deque([start])
        while dq:
            u = dq.popleft()
            for v in adj_full[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    dq.append(v)

    # Build adjacency from left (color 0) to right (color 1)
    left_nodes = [i for i in range(1, n + 1) if color[i] == 0]
    right_nodes = [i for i in range(1, n + 1) if color[i] == 1]
    adj = {u: [] for u in left_nodes}
    for u, v in edges:
        if color[u] == 0:
            adj[u].append(v)
        else:
            adj[v].append(u)

    # Hopcroft–Karp
    INF = 10 ** 9
    matchL = {u: -1 for u in left_nodes}
    matchR = {v: -1 for v in right_nodes}
    dist = {}

    def bfs() -> bool:
        q = deque()
        for u in left_nodes:
            if matchL[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reachable = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                mu = matchR[v]
                if mu != -1 and dist[mu] == INF:
                    dist[mu] = dist[u] + 1
                    q.append(mu)
                if mu == -1:
                    reachable = True
        return reachable

    def dfs(u: int) -> bool:
        for v in adj[u]:
            mu = matchR[v]
            if mu == -1 or (dist[mu] == dist[u] + 1 and dfs(mu)):
                matchL[u] = v
                matchR[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in left_nodes:
            if matchL[u] == -1 and dfs(u):
                matching += 1

    # Minimum vertex cover from matching
    # start from unmatched left vertices, traverse alternating paths
    L_vis = set()
    R_vis = set()
    q = deque([u for u in left_nodes if matchL[u] == -1])
    for u in q:
        L_vis.add(u)
    while q:
        u = q.popleft()
        if u in L_vis:  # left side
            for v in adj[u]:
                if v not in R_vis and matchL[u] != v:  # non-matching edge
                    R_vis.add(v)
                    if matchR[v] != -1 and matchR[v] not in L_vis:
                        L_vis.add(matchR[v])
                        q.append(matchR[v])
        else:  # right side (should not happen in this loop)
            pass

    # Minimum vertex cover
    min_vc = set()
    for u in left_nodes:
        if u not in L_vis:
            min_vc.add(u)
    for v in right_nodes:
        if v in R_vis:
            min_vc.add(v)

    # Maximum independent set = complement
    indep = [i for i in range(1, n + 1) if i not in min_vc]

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()