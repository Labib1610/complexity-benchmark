from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm approach
    # But we'll use a simpler approach with DFS-based augmenting paths
    
    # match_u[u] stores the matched platform for controller u (0 if unmatched)
    # match_v[v] stores the matched controller for platform v (0 if unmatched)
    match_u = [0] * (q + 1)
    match_v = [0] * (q + 1)
    
    def dfs(u, visited):
        for v in graph[u]:
            if visited[v - q]:  # v is platform, so adjust index
                continue
            visited[v - q] = True
            
            # If v is unmatched or we can find augmenting path from match_v[v]
            if match_v[v - q] == 0 or dfs(match_v[v - q], visited):
                match_u[u] = v
                match_v[v - q] = u
                return True
        return False
    
    matching = 0
    for u in range(1, q + 1):
        visited = [False] * (q + 1)
        if dfs(u, visited):
            matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_u[u])
    else:
        print("NO")

solve()