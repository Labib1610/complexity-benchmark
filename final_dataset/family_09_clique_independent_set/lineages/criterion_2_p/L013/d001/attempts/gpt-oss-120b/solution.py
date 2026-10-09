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
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    color = [-1] * (n + 1)
    left = []
    right = []
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
        # no need to check conflict, guaranteed bipartite

    for v in range(1, n + 1):
        if color[v] == 0:
            left.append(v)
        else:
            right.append(v)

    # map vertex id to index in left/right arrays
    left_id = {v: i for i, v in enumerate(left)}
    right_id = {v: i for i, v in enumerate(right)}

    L = len(left)
    R = len(right)
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

    # 3. minimum vertex cover
    # start from unmatched left vertices, follow alternating paths
    visited_left = [False] * L
    visited_right = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            q.append(('L', u))
            visited_left[u] = True
    while q:
        side, idx = q.popleft()
        if side == 'L':
            for v in g[idx]:
                if not visited_right[v] and pairU[idx] != v:  # edge not in matching
                    visited_right[v] = True
                    if pairV[v] != -1 and not visited_left[pairV[v]]:
                        visited_left[pairV[v]] = True
                        q.append(('L', pairV[v]))
        else:  # right side, we only reach right via non‑matching edges, so no further moves
            pass

    cover = set()
    # left not visited
    for i, v in enumerate(left):
        if not visited_left[i]:
            cover.add(v)
    # right visited
    for i, v in enumerate(right):
        if visited_right[i]:
            cover.add(v)

    indep = [v for v in range(1, n + 1) if v not in cover]

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()