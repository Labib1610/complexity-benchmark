import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # x is locked to y, so we can group by x
    # For each x, we have a list of possible z values
    x_to_z = [[] for _ in range(k + 1)]
    x_to_y = [0] * (k + 1)
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        x_to_z[x].append(z)
        x_to_y[x] = y
    
    # We need to select exactly one z for each x such that all z are distinct
    # This is a bipartite matching problem: left side x, right side z
    # Since x is locked to y, and y is distinct for each x, we just need to match x to z
    
    # Build adjacency list
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        adj[x] = x_to_z[x][:]
    
    # Hopcroft-Karp algorithm for bipartite matching
    pair_u = [0] * (k + 1)  # pair_u[x] = matched z
    pair_v = [0] * (k + 1)  # pair_v[z] = matched x
    dist = [0] * (k + 1)
    
    INF = float('inf')
    
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
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        for x in range(1, k + 1):
            z = pair_u[x]
            y = x_to_y[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()