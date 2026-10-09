import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Controllers: 1..q, Platforms: q+1..2q
    # Remap platforms to 1..q for bipartite matching
    adj = [[] for _ in range(q + 1)]
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b - q)  # remap platform to 1..q
    
    # Hopcroft-Karp for maximum bipartite matching
    match_u = [0] * (q + 1)  # match_u[u] = v matched to u
    match_v = [0] * (q + 1)  # match_v[v] = u matched to v
    dist = [0] * (q + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if match_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                u2 = match_v[v]
                if u2 == 0:
                    found = True
                elif dist[u2] == -1:
                    dist[u2] = dist[u] + 1
                    queue.append(u2)
        return found
    
    def dfs(u):
        for v in adj[u]:
            u2 = match_v[v]
            if u2 == 0 or (dist[u2] == dist[u] + 1 and dfs(u2)):
                match_u[u] = v
                match_v[v] = u
                return True
        dist[u] = -1
        return False
    
    matching_size = 0
    while bfs():
        for u in range(1, q + 1):
            if match_u[u] == 0 and dfs(u):
                matching_size += 1
    
    if matching_size != q:
        print("NO")
        return
    
    print("YES")
    for u in range(1, q + 1):
        print(u, match_u[u] + q)

if __name__ == "__main__":
    solve()