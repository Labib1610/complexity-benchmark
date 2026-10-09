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
        # Map platform from [q+1, 2q] to [1, q]
        b_mapped = b - q
        graph[a].append(b_mapped)
        edges.append((a, b_mapped))
    
    # Implement Hopcroft-Karp algorithm for maximum bipartite matching
    def bfs():
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
        if u != 0:
            for v in graph[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    # Initialize
    pair_u = [0] * (q + 1)  # pair_u[u] = v means u is matched to v
    pair_v = [0] * (q + 1)  # pair_v[v] = u means v is matched to u
    dist = [float('inf')] * (q + 1)
    
    # Find maximum matching
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            # Convert back to original platform ID
            print(u, pair_u[u] + q)
    else:
        print("NO")

solve()