import sys
import collections

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    # ----- build undirected graph for colouring -----
    g = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)
        edges.append((u, v))

    # ----- bipartition by BFS -----
    color = [-1] * n          # 0 = left, 1 = right
    for start in range(n):
        if color[start] != -1:
            continue
        dq = collections.deque([start])
        color[start] = 0
        while dq:
            v = dq.popleft()
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    dq.append(to)

    # ----- create left/right index maps -----
    left_idx = [-1] * n
    right_idx = [-1] * n
    left_nodes = []
    right_nodes = []
    for v in range(n):
        if color[v] == 0:
            left_idx[v] = len(left_nodes)
            left_nodes.append(v)
        else:
            right_idx[v] = len(right_nodes)
            right_nodes.append(v)

    L = len(left_nodes)
    R = len(right_nodes)

    # ----- adjacency from left to right -----
    adj = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            lu = left_idx[u]
            rv = right_idx[v]
        else:
            lu = left_idx[v]
            rv = right_idx[u]
        adj[lu].append(rv)

    # ----- Hopcroft‑Karp -----
    INF = 10 ** 9
    pairU = [-1] * L
    pairV = [-1] * R
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
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    sys.setrecursionlimit(1 << 25)

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

    # ----- minimum vertex cover via alternating paths -----
    visitedL = [False] * L
    visitedR = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            visitedL[u] = True
            q.append(('L', u))

    while q:
        side, x = q.popleft()
        if side == 'L':
            for v in adj[x]:
                if pairU[x] != v and not visitedR[v]:
                    visitedR[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            pu = pairV[x]
            if pu != -1 and not visitedL[pu]:
                visitedL[pu] = True
                q.append(('L', pu))

    # independent set = (left visited) ∪ (right NOT visited)
    independent = []
    for idx, v in enumerate(left_nodes):
        if visitedL[idx]:
            independent.append(v + 1)          # back to 1‑based
    for idx, v in enumerate(right_nodes):
        if not visitedR[idx]:
            independent.append(v + 1)

    if len(independent) < k:
        sys.stdout.write("NO")
        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()