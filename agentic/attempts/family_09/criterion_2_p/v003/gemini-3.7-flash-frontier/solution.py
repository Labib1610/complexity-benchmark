import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # 2-color the graph into L (color 0) and R (color 1)
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                c = color[u] ^ 1
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = c
                        q.append(v)

    # Build directed/bipartite graph from L to R
    # L vertices have color 0, R vertices have color 1
    # Hopcroft-Karp algorithm
    pair_u = [0] * (n + 1)  # match for L
    pair_v = [0] * (n + 1)  # match for R
    dist = [0] * (n + 1)

    # Pre-filter adjacency list so L only points to R
    adj_L = [[] for _ in range(n + 1)]
    L_nodes = []
    R_nodes = []
    for u in range(1, n + 1):
        if color[u] == 0:
            L_nodes.append(u)
            adj_L[u] = adj[u]
        else:
            R_nodes.append(u)

    INF = 10**9

    def bfs():
        q = deque()
        for u in L_nodes:
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF

        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj_L[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj_L[u]:
                pu = pair_v[v]
                if dist[pu] == dist[u] + 1:
                    if dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in L_nodes:
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    max_independent_set_size = n - matching
    if max_independent_set_size < k:
        print("NO")
        return

    # Find Min Vertex Cover via reachability in alternating graph
    # Start BFS from unmatched vertices in L
    # Traverse: L -> R along non-matched edges, R -> L along matched edges
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)

    q = deque()
    for u in L_nodes:
        if pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)

    while q:
        u = q.popleft()
        for v in adj_L[u]:
            if v != pair_u[u] and not visited_R[v]:
                visited_R[v] = True
                pu = pair_v[v]
                if pu != 0 and not visited_L[pu]:
                    visited_L[pu] = True
                    q.append(pu)

    # In bipartite graph:
    # Min Vertex Cover = (L \ visited_L) U (R \cap visited_R)
    # Max Independent Set = (L \cap visited_L) U (R \ visited_R)
    independent_set = []
    for u in L_nodes:
        if visited_L[u]:
            independent_set.append(u)
    for v in R_nodes:
        if not visited_R[v]:
            independent_set.append(v)

    ans = independent_set[:k]
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()