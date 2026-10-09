import sys
from collections import deque

# -------------------------------------------------------------

def solve() -> None:
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    # original adjacency (only needed for colouring)
    adj_orig = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_orig[u].append(v)
        adj_orig[v].append(u)
        edges.append((u, v))

    # 1) colour the graph -> bipartition
    colour = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj_orig[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)

    # build lists of vertices per side and mapping to indices
    left_nodes = []
    right_nodes = []
    left_id = [-1] * (n + 1)
    right_id = [-1] * (n + 1)
    for v in range(1, n + 1):
        if colour[v] == 0:
            left_id[v] = len(left_nodes)
            left_nodes.append(v)
        else:
            right_id[v] = len(right_nodes)
            right_nodes.append(v)

    L = len(left_nodes)
    R = len(right_nodes)

    # adjacency from left side to right side (indices)
    adj = [[] for _ in range(L)]
    for u, v in edges:
        if colour[u] == 0:          # u is left, v right
            adj[left_id[u]].append(right_id[v])
        else:                       # v is left, u right
            adj[left_id[v]].append(right_id[u])

    # ---------------------------------------------------------
    # Hopcroft‑Karp
    pairU = [-1] * L
    pairV = [-1] * R
    dist = [0] * L
    INF = 10 ** 9

    def bfs() -> bool:
        q = deque()
        for u in range(L):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu == -1:
                    found = True          # free vertex on right reachable
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return found

    sys.setrecursionlimit(1 << 25)

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(L):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    # ---------------------------------------------------------
    # Build the alternating reachable set Z
    visitedL = [False] * L
    visitedR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            visitedL[u] = True
            q.append(u)

    while q:
        u = q.popleft()          # left vertex
        for v in adj[u]:
            if pairU[u] == v:    # matched edge – skip
                continue
            if not visitedR[v]:
                visitedR[v] = True
                pu = pairV[v]    # matched partner on left, if any
                if pu != -1 and not visitedL[pu]:
                    visitedL[pu] = True
                    q.append(pu)

    # independent set = (L ∩ Z) ∪ (R \ Z)
    independent = []
    for idx, orig in enumerate(left_nodes):
        if visitedL[idx]:
            independent.append(orig)
    for idx, orig in enumerate(right_nodes):
        if not visitedR[idx]:
            independent.append(orig)

    if len(independent) >= k:
        out = ['YES']
        out.append(' '.join(map(str, independent[:k])))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')


# -------------------------------------------------------------
if __name__ == '__main__':
    solve()