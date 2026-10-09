import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    # bipartition via BFS coloring
    color = [-1] * n  # 0 left, 1 right
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    # build adjacency from left to right for matching
    left_ids = [i for i in range(n) if color[i] == 0]
    right_ids = [i for i in range(n) if color[i] == 1]
    L = len(left_ids)
    R = len(right_ids)
    # map original index to left/right position
    lid = [-1] * n
    rid = [-1] * n
    for idx, v in enumerate(left_ids):
        lid[v] = idx
    for idx, v in enumerate(right_ids):
        rid[v] = idx

    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[lid[u]].append(rid[v])
        else:
            g[lid[v]].append(rid[u])

    # Hopcroft–Karp
    INF = 10 ** 9
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
                for v in g[u]:
                    if pairV[v] == -1:
                        d = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return d != INF

    def dfs(u):
        for v in g[u]:
            pu = pairV[v]
            if pairV[v] == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    while bfs():
        for u in range(L):
            if pairU[u] == -1:
                dfs(u)

    # Minimum vertex cover from alternating BFS
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
                if not visited_right[v] and pairU[idx] != v:  # non-matching edge
                    visited_right[v] = True
                    q.append(('R', v))
        else:  # right
            pu = pairV[idx]
            if pu != -1 and not visited_left[pu]:
                visited_left[pu] = True
                q.append(('L', pu))

    # Independent set = (left visited) U (right not visited)
    independent = []
    for i, orig in enumerate(left_ids):
        if visited_left[i]:
            independent.append(orig + 1)
    for i, orig in enumerate(right_ids):
        if not visited_right[i]:
            independent.append(orig + 1)

    if len(independent) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()