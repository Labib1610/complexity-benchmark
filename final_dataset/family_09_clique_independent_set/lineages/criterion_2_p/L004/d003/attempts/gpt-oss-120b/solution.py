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

    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # ------------------------------------------------------------
    # 1) bipartite colouring
    colour = [-1] * n
    left_vertices = []   # colour 0
    right_vertices = []  # colour 1
    for start in range(n):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = collections.deque([start])
        while q:
            v = q.popleft()
            for (a, b) in []:  # placeholder, will use edges later
                pass
        # we will colour using adjacency built later (more efficient)
    # Instead of scanning edges repeatedly, build adjacency first (undirected)
    adj_und = [[] for _ in range(n)]
    for u, v in edges:
        adj_und[u].append(v)
        adj_und[v].append(u)

    for start in range(n):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = collections.deque([start])
        while q:
            v = q.popleft()
            for nb in adj_und[v]:
                if colour[nb] == -1:
                    colour[nb] = colour[v] ^ 1
                    q.append(nb)

    for v in range(n):
        if colour[v] == 0:
            left_vertices.append(v)
        else:
            right_vertices.append(v)

    L = len(left_vertices)
    R = len(right_vertices)

    left_id = [-1] * n
    right_id = [-1] * n
    for idx, v in enumerate(left_vertices):
        left_id[v] = idx
    for idx, v in enumerate(right_vertices):
        right_id[v] = idx

    # ------------------------------------------------------------
    # 2) adjacency from left to right (indices)
    adj = [[] for _ in range(L)]
    for u, v in edges:
        if colour[u] == 0:
            adj[left_id[u]].append(right_id[v])
        else:
            adj[left_id[v]].append(right_id[u])

    # ------------------------------------------------------------
    # 3) Hopcroft‑Karp
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

    while bfs():
        for u in range(L):
            if pairU[u] == -1:
                dfs(u)

    # ------------------------------------------------------------
    # 4) minimum vertex cover via alternating BFS
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
                if pairU[u] != v and not visR[v]:
                    visR[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            v = idx
            pu = pairV[v]
            if pu != -1 and not visL[pu]:
                visL[pu] = True
                q.append(('L', pu))

    # ------------------------------------------------------------
    # 5) maximum independent set = (L visited) ∪ (R not visited)
    independent = []
    for i, v in enumerate(left_vertices):
        if visL[i]:
            independent.append(v + 1)          # back to 1‑based
    for i, v in enumerate(right_vertices):
        if not visR[i]:
            independent.append(v + 1)

    if len(independent) >= k:
        out = ['YES', ' '.join(map(str, independent[:k]))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')


if __name__ == "__main__":
    solve()