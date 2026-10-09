import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    # Controllers: 1 to q (left side)
    # Platforms: q+1 to 2q (right side)
    # Renumber platforms to 0 to q-1 for adjacency list
    
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b - q - 1)  # platform index 0 to q-1
    
    # Hopcroft-Karp algorithm
    pair_u = [-1] * (q + 1)  # pair_u[u] = v matched with u
    pair_v = [-1] * q        # pair_v[v] = u matched with v
    dist = [0] * (q + 1)
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if pair_v[v] == -1:
                        dist[NIL] = dist[u] + 1
                    elif dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[NIL] != float('inf')
    
    def dfs(u):
        for v in adj[u]:
            if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == -1:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            v = pair_u[u]
            print(u, v + q + 1)
    else:
        print("NO")

solve()