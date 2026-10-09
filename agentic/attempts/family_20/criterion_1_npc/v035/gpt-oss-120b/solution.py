import sys
from collections import deque

def solve() -> None:
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # check bipartite
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        while q:
            v = q.popleft()
            for to, _ in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return

    # Build bipartite graph for matching (left = color 0)
    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    L = len(left)
    R = len(right)
    # map vertex to index in left/right arrays
    lid = {v: i for i, v in enumerate(left)}
    rid = {v: i for i, v in enumerate(right)}
    G = [[] for _ in range(L)]
    edge_id_map = {}
    for idx, (u, v) in enumerate(edges):
        if color[u] == 0:
            a, b = u, v
        else:
            a, b = v, u
        ui = lid[a]
        vi = rid[b]
        G[ui].append((vi, idx))
        edge_id_map[(ui, vi)] = idx  # not needed later

    # Hopcroft–Karp
    INF = 10**9
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L

    def bfs():
        q = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v, _ in G[u]:
                    if pairV[v] == -1:
                        d = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return d != INF

    def dfs(u):
        for v, _ in G[u]:
            pu = pairV[v]
            if pairV[v] == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
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

    if matching * 2 != n:  # perfect matching needed
        print("NO")
        return

    # assign colors
    ans = [0] * m
    # edges in matching -> color 1
    for u in range(L):
        v = pairU[u]
        # find edge index between left vertex left[u] and right vertex right[v]
        # scan adjacency of left[u]
        lu = left[u]
        rv = right[v]
        for to, eid in adj[lu]:
            if to == rv:
                ans[eid] = 1
                break

    # build remaining adjacency (each vertex degree 2 now)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if ans[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m

    for start in range(n):
        while rem_adj[start]:
            # start a new cycle
            cur = start
            col = 2
            while True:
                # pick an unused edge from cur
                while rem_adj[cur] and visited_edge[rem_adj[cur][-1][1]]:
                    rem_adj[cur].pop()
                if not rem_adj[cur]:
                    break
                nxt, eid = rem_adj[cur].pop()
                if visited_edge[eid]:
                    continue
                visited_edge[eid] = True
                ans[eid] = col
                col = 5 - col  # toggle between 2 and3
                cur = nxt
                if cur == start:
                    # cycle closed, but may still have edges at start; continue outer while
                    break

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()