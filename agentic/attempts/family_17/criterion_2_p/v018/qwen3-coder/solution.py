from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build graph for bipartite matching
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q (we'll map them to 1 to q for easier handling)
    
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        # Map platform from [q+1, 2*q] to [1, q]
        b_mapped = b - q
        graph[a].append(b_mapped)
        edges.append((a, b_mapped))
    
    # Find maximum matching using Hopcroft-Karp algorithm implementation
    # or simpler augmenting paths approach
    
    # pair_u[u] stores the matched platform for controller u (0 if unmatched)
    # pair_v[v] stores the matched controller for platform v (0 if unmatched)
    pair_u = [0] * (q + 1)
    pair_v = [0] * (q + 1)
    
    def bfs():
        # BFS to find shortest augmenting paths
        dist = [0] * (q + 1)
        queue = deque()
        
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            
            if dist[u] < dist[0]:
                for v in graph[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        
        return dist[0] != float('inf')
    
    def dfs(u):
        if u == 0:
            return True
            
        for v in graph[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(pair_v[v]):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        
        dist[u] = float('inf')
        return False
    
    # Hopcroft-Karp main algorithm
    matching = 0
    
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            # Convert platform back to original numbering
            print(u, pair_u[u] + q)
    else:
        print("NO")

solve()