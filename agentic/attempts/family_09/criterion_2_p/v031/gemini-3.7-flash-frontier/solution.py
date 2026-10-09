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
        
    # 2-color the graph to find bipartition L and R
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)

    # Hopcroft-Karp Algorithm
    pair_u = [0] * (n + 1)  # matching for L vertices
    pair_v = [0] * (n + 1)  # matching for R vertices
    dist = [0] * (n + 1)
    INF = 10**9

    def bfs():
        queue = deque()
        for u in range(1, n + 1):
            if color[u] == 1:
                if pair_u[u] == 0:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = INF
        dist[0] = INF
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
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

    # Run Hopcroft-Karp
    while bfs():
        for u in range(1, n + 1):
            if color[u] == 1 and pair_u[u] == 0:
                dfs(u)

    # Find Minimum Vertex Cover via reachability from unmatched L-vertices
    visited = [False] * (n + 1)
    queue = deque()
    for u in range(1, n + 1):
        if color[u] == 1 and pair_u[u] == 0:
            visited[u] = True
            queue.append(u)
            
    while queue:
        curr = queue.popleft()
        if color[curr] == 1:
            for v in adj[curr]:
                if v != pair_u[curr] and not visited[v]:
                    visited[v] = True
                    queue.append(v)
        else:
            v = pair_v[curr]
            if v != 0 and not visited[v]:
                visited[v] = True
                queue.append(v)

    # Maximum Independent Set is:
    # (L \cap Visited) \cup (R \setminus Visited)
    mis = []
    for i in range(1, n + 1):
        if color[i] == 1:
            if visited[i]:
                mis.append(i)
        else:
            if not visited[i]:
                mis.append(i)

    if len(mis) < k:
        print("NO")
    else:
        print("YES")
        print(*(mis[:k]))

if __name__ == '__main__':
    solve()