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
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. colour the graph
    colour = [-1] * (n + 1)          # 0 = left, 1 = right
    left_vertices = []
    right_vertices = []
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    q.append(v)

    for v in range(1, n + 1):
        if colour[v] == 0:
            left_vertices.append(v)
        else:
            right_vertices.append(v)

    # 2. build adjacency from left to right
    left_adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        if colour[u] == 0:
            left_adj[u].append(v)
        else:
            left_adj[v].append(u)

    # 3. Hopcroft‑Karp
    INF = 10 ** 9
    matchL = [0] * (n + 1)   # left -> right
    matchR = [0] * (n + 1)   # right -> left
    dist = [0] * (n + 1)

    def bfs() -> bool:
        q = deque()
        for u in left_vertices:
            if matchL[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in left_adj[u]:
                if matchR[v] == 0:
                    found = True
                else:
                    nxt = matchR[v]
                    if dist[nxt] == INF:
                        dist[nxt] = dist[u] + 1
                        q.append(nxt)
        return found

    def dfs(u: int) -> bool:
        for v in left_adj[u]:
            if matchR[v] == 0 or (dist[matchR[v]] == dist[u] + 1 and dfs(matchR[v])):
                matchL[u] = v
                matchR[v] = u
                return True
        dist[u] = INF
        return False

    while bfs():
        for u in left_vertices:
            if matchL[u] == 0:
                dfs(u)

    # 4. build Z (vertices reachable by alternating paths)
    visitedL = [False] * (n + 1)
    visitedR = [False] * (n + 1)
    q = deque()
    for u in left_vertices:
        if matchL[u] == 0:
            visitedL[u] = True
            q.append(('L', u))

    while q:
        side, node = q.popleft()
        if side == 'L':
            u = node
            for v in left_adj[u]:
                if not visitedR[v] and matchL[u] != v:   # non‑matched edge
                    visitedR[v] = True
                    q.append(('R', v))
        else:   # side == 'R'
            v = node
            if matchR[v] != 0:
                u = matchR[v]
                if not visitedL[u]:
                    visitedL[u] = True
                    q.append(('L', u))

    # 5. maximum independent set
    independent = []
    for u in left_vertices:
        if visitedL[u]:
            independent.append(u)
    for v in right_vertices:
        if not visitedR[v]:
            independent.append(v)

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()