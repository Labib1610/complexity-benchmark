import sys
from collections import deque

input = sys.stdin.readline

def solve():
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
    left = []
    right = []
    for i in range(n):
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

    # Build matching graph from left to right
    left_set = set(left)
    right_set = set(right)
    match_right = [-1] * n
    match_left = [-1] * n

    # Hopcroft-Karp
    INF = 10**9
    dist = [0] * n

    def bfs():
        q = deque()
        for u in left:
            if match_left[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                mu = match_right[v]
                if mu != -1 and dist[mu] == INF:
                    dist[mu] = dist[u] + 1
                    q.append(mu)
                elif mu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            mu = match_right[v]
            if mu == -1 or (dist[mu] == dist[u] + 1 and dfs(mu)):
                match_left[u] = v
                match_right[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in left:
            if match_left[u] == -1 and dfs(u):
                matching += 1

    # Minimum vertex cover via Konig's theorem
    # From unmatched left nodes, BFS alternating paths
    visited_left = [False] * n
    visited_right = [False] * n
    q = deque()
    for u in left:
        if match_left[u] == -1:
            visited_left[u] = True
            q.append(u)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited_right[v]:
                visited_right[v] = True
                mu = match_right[v]
                if mu != -1 and not visited_left[mu]:
                    visited_left[mu] = True
                    q.append(mu)

    # Vertex cover: right visited + left not visited
    cover = set()
    for u in left:
        if not visited_left[u]:
            cover.add(u)
    for v in right:
        if visited_right[v]:
            cover.add(v)

    # Independent set = complement of cover
    independent = [i for i in range(n) if i not in cover]

    if len(independent) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in independent[:k]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()