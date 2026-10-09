import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj, U, V):
    # U, V are lists of vertex ids on each side
    # adj maps U vertex -> list of V vertices
    INF = 10**9
    pairU = {u: None for u in U}
    pairV = {v: None for v in V}
    dist = {}

    def bfs():
        q = deque()
        for u in U:
            if pairU[u] is None:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu is not None and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu is None:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu is None or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in U:
            if pairU[u] is None and dfs(u):
                matching += 1
    return matching, pairU, pairV

def main():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # Bipartition via BFS
    color = [-1] * (n+1)
    for i in range(1, n+1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    U = [i for i in range(1, n+1) if color[i] == 0]
    V = [i for i in range(1, n+1) if color[i] == 1]

    # Build adjacency for Hopcroft-Karp: only from U to V
    adjU = {u: [] for u in U}
    for u, v in edges:
        if color[u] == 0:
            adjU[u].append(v)
        else:
            adjU[v].append(u)

    matching, pairU, pairV = hopcroft_karp(n, m, adjU, U, V)

    # Minimum vertex cover via alternating paths
    # Mark all U not matched, then follow alternating paths
    visitedU = {u: False for u in U}
    visitedV = {v: False for v in V}

    q = deque()
    for u in U:
        if pairU[u] is None:
            visitedU[u] = True
            q.append(u)

    while q:
        u = q.popleft()
        for v in adjU[u]:
            if not visitedV[v]:
                visitedV[v] = True
                if pairV[v] is not None and not visitedU[pairV[v]]:
                    visitedU[pairV[v]] = True
                    q.append(pairV[v])

    # Vertex cover: U not visited + V visited
    vertex_cover = set()
    for u in U:
        if not visitedU[u]:
            vertex_cover.add(u)
    for v in V:
        if visitedV[v]:
            vertex_cover.add(v)

    independent_set = [i for i in range(1, n+1) if i not in vertex_cover]

    if len(independent_set) >= k:
        print("YES")
        print(" ".join(map(str, independent_set[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()