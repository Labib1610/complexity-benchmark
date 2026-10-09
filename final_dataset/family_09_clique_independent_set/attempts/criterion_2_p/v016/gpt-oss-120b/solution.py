import sys
from collections import deque

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

    # bipartition via BFS coloring
    color = [-1] * (n + 1)   # 0 = left, 1 = right
    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    left_nodes = [i for i in range(1, n + 1) if color[i] == 0]
    right_nodes = [i for i in range(1, n + 1) if color[i] == 1]

    # build adjacency from left to right
    G = {u: [] for u in left_nodes}
    for u, v in edges:
        if color[u] == 0:
            G[u].append(v)
        else:
            G[v].append(u)

    # Hopcroft–Karp
    INF = 10 ** 9
    pairU = {u: -1 for u in left_nodes}
    pairV = {v: -1 for v in right_nodes}
    dist = {}

    def bfs() -> bool:
        dq = deque()
        for u in left_nodes:
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                if pu == -1:
                    found = True
        return found

    def dfs(u: int) -> bool:
        for v in G[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in left_nodes:
            if pairU[u] == -1 and dfs(u):
                matching += 1

    max_independent_size = n - matching
    if k > max_independent_size:
        print("NO")
        return

    # find minimum vertex cover
    # start from unmatched left vertices, follow alternating paths
    visited_left = set()
    visited_right = set()
    dq = deque()
    for u in left_nodes:
        if pairU[u] == -1:
            dq.append(('L', u))
            visited_left.add(u)
    while dq:
        side, v = dq.popleft()
        if side == 'L':
            for to in G[v]:
                if to not in visited_right and pairU[v] != to:  # non-matching edge
                    visited_right.add(to)
                    dq.append(('R', to))
        else:  # right side
            pu = pairV[v]
            if pu != -1 and pu not in visited_left:
                visited_left.add(pu)
                dq.append(('L', pu))

    # min vertex cover = (Left \ visited_left) ∪ (Right ∩ visited_right)
    # independent set = complement
    independent = []
    for u in left_nodes:
        if u in visited_left:
            independent.append(u)
    for v in right_nodes:
        if v not in visited_right:
            independent.append(v)

    # take any k vertices
    ans = independent[:k]
    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()