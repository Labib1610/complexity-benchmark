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
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm
    # But we'll use a simpler approach with DFS for this case
    
    # match_u[u] stores the matched platform for controller u
    # match_v[v] stores the matched controller for platform v
    match_u = [0] * (q + 1)  # 1-indexed
    match_v = [0] * (q + 1)  # 1-indexed, for platforms q+1 to 2*q, we map to 1 to q
    
    def dfs(u, visited):
        for v in graph[u]:
            # Convert platform id to 1-based index: v - q
            v_idx = v - q
            if visited[v_idx]:
                continue
            visited[v_idx] = True
            
            # If platform v is unmatched or we can find augmenting path
            if match_v[v_idx] == 0 or dfs(match_v[v_idx], visited):
                match_u[u] = v
                match_v[v_idx] = u
                return True
        return False
    
    # Try to find maximum matching
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