import sys
from collections import deque

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

    # bipartition (0 = left, 1 = right)
    color = [-1] * n
    left_nodes = []
    right_nodes = []
    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
    for i, c in enumerate(color):
        if c == 0:
            left_nodes.append(i)
        else:
            right_nodes.append(i)

    # map original indices to left/right ids
    left_id = {v: idx for idx, v in enumerate(left_nodes)}
    right_id = {v: idx for idx, v in enumerate(right_nodes)}
    L = len(left_nodes)
    R = len(right_nodes)

    # build adjacency from left ids to right ids
    g = [[] for _ in range(L)]
    for u, v in edges:
        if color[u] == 0:
            g[left_id[u]].append(right_id[v])
        else:
            g[left_id[v]].append(right_id[u])

    # Hopcroft–Karp
    INF = 10**9
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
        reachable = False
        while q:
            u = q.popleft()
            for v in g[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    reachable = True
        return reachable

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

    max_independent_size = n - matching
    if max_independent_size < k:
        print("NO")
        return

    # Find minimum vertex cover
    # start from unmatched left vertices, follow alternating paths
    visited_left = [False] * L
    visited_right = [False] * R
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            q.append(u)
            visited_left[u] = True
    while q:
        u = q.popleft()
        for v in g[u]:
            if not visited_right[v]:
                visited_right[v] = True
                pu = pairV[v]
                if pu != -1 and not visited_left[pu]:
                    visited_left[pu] = True
                    q.append(pu)

    # Vertex cover = (left not visited) U (right visited)
    in_cover = [False] * n
    for idx, node in enumerate(left_nodes):
        if not visited_left[idx]:
            in_cover[node] = True
    for idx, node in enumerate(right_nodes):
        if visited_right[idx]:
            in_cover[node] = True

    # Independent set = complement
    independent = [i+1 for i, inc in enumerate(in_cover) if not inc]
    result = independent[:k]

    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()