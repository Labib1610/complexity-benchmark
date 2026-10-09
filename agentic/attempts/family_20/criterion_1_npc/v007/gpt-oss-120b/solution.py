import sys
from collections import deque

def bfs_bipartite(n, adj):
    color = [ -1 ] * (n + 1)
    for start in range(1, n + 1):
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
                elif color[to] == color[v]:
                    return None          # not bipartite
    return color

# Hopcroft–Karp for bipartite graph (left side = 1..nL)
def hopcroft_karp(nL, nR, g):
    INF = 10 ** 9
    pairU = [0] * (nL + 1)
    pairV = [0] * (nR + 1)
    dist = [0] * (nL + 1)

    def bfs():
        q = deque()
        for u in range(1, nL + 1):
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in g[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    def dfs(u):
        if u == 0:
            return True
        for v in g[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, nL + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1
    return pairU, matching

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    part = bfs_bipartite(n, adj)
    if part is None:
        print("NO")
        return

    # split vertices to left/right according to part (0/1)
    left_ids = {}
    right_ids = {}
    lcnt = rcnt = 0
    for v in range(1, n + 1):
        if part[v] == 0:
            lcnt += 1
            left_ids[v] = lcnt
        else:
            rcnt += 1
            right_ids[v] = rcnt

    # adjacency for current graph (will be modified)
    cur_adj = [list() for _ in range(lcnt + 1)]   # only left side needed
    edge_pos = {}   # (l,r) -> list of original indices (there is at most one)
    for idx, (u, v) in enumerate(edges):
        if part[u] == 0:
            l = left_ids[u]; r = right_ids[v]
        else:
            l = left_ids[v]; r = right_ids[u]
        cur_adj[l].append(r)
        edge_pos[(l, r)] = idx

    colour = [0] * m
    for col in range(1, 4):
        pairU, size = hopcroft_karp(lcnt, rcnt, cur_adj)
        # size must be n/2
        for u in range(1, lcnt + 1):
            v = pairU[u]
            if v == 0:
                continue
            idx = edge_pos.pop((u, v))
            colour[idx] = col
        # rebuild adjacency without used edges
        new_adj = [list() for _ in range(lcnt + 1)]
        for (u, v), idx in edge_pos.items():
            new_adj[u].append(v)
        cur_adj = new_adj

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    solve()