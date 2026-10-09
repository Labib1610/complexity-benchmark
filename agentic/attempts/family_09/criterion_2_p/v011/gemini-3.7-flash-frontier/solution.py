import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # 2-color the graph to partition into Left (L) and Right (R)
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)

    # Hopcroft-Karp Algorithm for Maximum Bipartite Matching
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    def bfs():
        q = deque()
        for u in range(1, n + 1):
            if color[u] == 0:
                if pair_u[u] == 0:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if color[u] == 0 and pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    # Find Minimum Vertex Cover using Konig's Theorem
    # Reachability in alternating paths starting from unmatched vertices in L
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = deque()
    for u in range(1, n + 1):
        if color[u] == 0 and pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited_R[v] and pair_u[u] != v:
                visited_R[v] = True
                match_u = pair_v[v]
                if match_u != 0 and not visited_L[match_u]:
                    visited_L[match_u] = True
                    q.append(match_u)

    # Maximum Independent Set consists of:
    # - Vertices in L that are visited
    # - Vertices in R that are NOT visited
    mis = []
    for u in range(1, n + 1):
        if color[u] == 0:
            if visited_L[u]:
                mis.append(u)
        else:
            if not visited_R[u]:
                mis.append(u)

    if len(mis) < k:
        print("NO")
    else:
        print("YES")
        print(*(mis[:k]))

if __name__ == '__main__':
    solve()