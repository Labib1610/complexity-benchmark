import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

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
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    # 2-color the graph
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

    # Hopcroft-Karp algorithm
    # Partition vertices into L (color 0) and R (color 1)
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    
    INF = 10**9
    
    # Pre-filter adjacency for L -> R
    adj_L = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        if color[u] == 0:
            adj_L[u] = adj[u]
            
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
                for v in adj_L[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj_L[u]:
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

    max_is_size = n - matching
    if max_is_size < k:
        print("NO")
        return

    # Find Min Vertex Cover / Max Independent Set
    # Reachability from unmatched vertices in L via alternating paths
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = deque()
    for u in range(1, n + 1):
        if color[u] == 0 and pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    while q:
        u = q.popleft()
        for v in adj_L[u]:
            if v != pair_u[u] and not visited_R[v]:
                visited_R[v] = True
                matched_u = pair_v[v]
                if matched_u != 0 and not visited_L[matched_u]:
                    visited_L[matched_u] = True
                    q.append(matched_u)

    # Max Independent Set:
    # vertices in L that are visited, and vertices in R that are NOT visited
    independent_set = []
    for u in range(1, n + 1):
        if color[u] == 0:
            if visited_L[u]:
                independent_set.append(u)
        else:
            if not visited_R[u]:
                independent_set.append(u)
                
    print("YES")
    print(*(independent_set[:k]))

if __name__ == '__main__':
    solve()