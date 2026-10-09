import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, adj, U):
    pair_u = [-1] * n
    pair_v = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        for u in U:
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == float('inf'):
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in U:
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u, pair_v

def main():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # Bipartite coloring
    color = [-1] * n
    U = []
    V = []
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            U.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            U.append(v)
                        else:
                            V.append(v)
                        q.append(v)

    # Build adjacency for matching from U to V
    adj_match = [[] for _ in range(n)]
    for u, v in edges:
        if color[u] == 0:
            adj_match[u].append(v)
        else:
            adj_match[v].append(u)

    matching_size, pair_u, pair_v = hopcroft_karp(n, adj_match, U)

    max_independent = n - matching_size
    if k > max_independent:
        print("NO")
        return

    # Find minimum vertex cover
    # From unmatched U vertices, BFS alternating
    visited_U = [False] * n
    visited_V = [False] * n
    q = deque()
    for u in U:
        if pair_u[u] == -1:
            visited_U[u] = True
            q.append(u)

    while q:
        u = q.popleft()
        for v in adj_match[u]:
            if not visited_V[v]:
                visited_V[v] = True
                pu = pair_v[v]
                if pu != -1 and not visited_U[pu]:
                    visited_U[pu] = True
                    q.append(pu)

    # Minimum vertex cover: U not visited + V visited
    cover = set()
    for u in U:
        if not visited_U[u]:
            cover.add(u)
    for v in V:
        if visited_V[v]:
            cover.add(v)

    # Independent set = all vertices not in cover
    independent = [i for i in range(n) if i not in cover]

    # If too many, remove extras
    if len(independent) > k:
        independent = independent[:k]

    print("YES")
    print(" ".join(str(x + 1) for x in independent))

if __name__ == "__main__":
    main()