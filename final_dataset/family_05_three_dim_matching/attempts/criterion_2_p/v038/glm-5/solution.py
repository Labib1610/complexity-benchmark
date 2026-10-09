import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Build adjacency: for each sensor u (1..k), list of frequencies
    adj = [[] for _ in range(k + 1)]
    # Store the relay for each sensor
    relay_of = [0] * (k + 1)
    
    for _ in range(t):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append(w)
        relay_of[u] = v
    
    # Hopcroft-Karp: match sensors to frequencies
    # Left: sensors 1..k, Right: frequencies 1..k
    INF = float('inf')
    pair_u = [0] * (k + 1)  # pair_u[u] = frequency matched to u (0 = none)
    pair_v = [0] * (k + 1)  # pair_v[v] = sensor matched to v (0 = none)
    dist = [0] * (k + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for w in adj[u]:
                    v = pair_v[w]
                    if v == 0:
                        dist[0] = dist[u] + 1
                    elif dist[v] == INF:
                        dist[v] = dist[u] + 1
                        queue.append(v)
        return dist[0] != INF
    
    def dfs(u):
        for w in adj[u]:
            v = pair_v[w]
            if v == 0 or (dist[v] == dist[u] + 1 and dfs(v)):
                pair_u[u] = w
                pair_v[w] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        for u in range(1, k + 1):
            print(f"{u} {relay_of[u]} {pair_u[u]}")
    else:
        print("NO")

solve()