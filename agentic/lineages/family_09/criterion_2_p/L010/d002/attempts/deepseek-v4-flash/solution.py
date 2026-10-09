import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj, U, V):
    # U, V are lists of vertices in left and right partitions
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
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu is not None and dist[pu] == float('inf'):
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
        dist[u] = float('inf')
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

    # Bipartite coloring
    color = [-1]*(n+1)
    left = []
    right = []
    for i in range(1, n+1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            left.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            left.append(v)
                        else:
                            right.append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        # Should not happen due to voltage property
                        pass

    # Build adjacency for matching: from left to right only
    adj_match = {u: [] for u in left}
    for u in left:
        for v in adj[u]:
            if color[v] == 1:
                adj_match[u].append(v)

    matching, pairU, pairV = hopcroft_karp(n, m, adj_match, left, right)

    # Minimum vertex cover via Konig's theorem
    # From unmatched left vertices, BFS alternating paths
    visited_left = set()
    visited_right = set()
    q = deque()
    for u in left:
        if pairU[u] is None:
            q.append(u)
            visited_left.add(u)
    while q:
        u = q.popleft()
        for v in adj_match[u]:
            if v not in visited_right:
                visited_right.add(v)
                pu = pairV[v]
                if pu is not None and pu not in visited_left:
                    visited_left.add(pu)
                    q.append(pu)

    # Minimum vertex cover = (left not visited) U (right visited)
    min_vertex_cover = set()
    for u in left:
        if u not in visited_left:
            min_vertex_cover.add(u)
    for v in right:
        if v in visited_right:
            min_vertex_cover.add(v)

    # Maximum independent set = complement of min vertex cover
    max_independent = [i for i in range(1, n+1) if i not in min_vertex_cover]

    if k <= len(max_independent):
        print("YES")
        print(" ".join(map(str, max_independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()