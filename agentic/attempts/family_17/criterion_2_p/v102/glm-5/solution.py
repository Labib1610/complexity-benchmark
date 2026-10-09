import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(q + 1)]
    edges = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        edges.append((a, b))
    
    # Bipartite matching using Hopcroft-Karp
    # Left side: initiators 1..q
    # Right side: responders q+1..2q, remapped to 1..q
    
    pair_u = [0] * (q + 1)
    pair_v = [0] * (q + 1)
    dist = [0] * (q + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        dist[0] = -1
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                pu = pair_v[v - q]
                if pu != 0 and dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    queue.append(pu)
                elif pu == 0:
                    found = True
        return found
    
    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v - q]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v - q] = u
                return True
        dist[u] = -1
        return False
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u])
    else:
        print("NO")

if __name__ == "__main__":
    solve()