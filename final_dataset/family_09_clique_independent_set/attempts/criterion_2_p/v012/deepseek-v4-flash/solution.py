import sys
from collections import deque

input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    # Bipartite coloring
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    # Hopcroft–Karp maximum matching
    INF = 10**9
    pairU = [-1] * n
    pairV = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        for u in range(n):
            if color[u] == 0 and pairU[u] == -1:
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

    def dfs(u):
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
        for u in range(n):
            if color[u] == 0 and pairU[u] == -1 and dfs(u):
                matching += 1

    # Minimum vertex cover via König's theorem
    # Mark vertices reachable from unmatched left vertices
    visited = [False] * n
    q = deque()
    for u in range(n):
        if color[u] == 0 and pairU[u] == -1:
            q.append(u)
            visited[u] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                pu = pairV[v]
                if pu != -1 and not visited[pu]:
                    visited[pu] = True
                    q.append(pu)

    # Minimum vertex cover: left not visited + right visited
    in_cover = [False] * n
    for u in range(n):
        if color[u] == 0 and not visited[u]:
            in_cover[u] = True
        if color[u] == 1 and visited[u]:
            in_cover[u] = True

    # Independent set = all vertices not in cover
    independent = [i for i in range(n) if not in_cover[i]]

    if len(independent) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x + 1) for x in independent[:k]))

if __name__ == "__main__":
    main()