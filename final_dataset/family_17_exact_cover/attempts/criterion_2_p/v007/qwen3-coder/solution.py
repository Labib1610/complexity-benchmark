from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm
    # But we'll use a simpler approach with DFS-based augmenting paths
    
    # match_u[u] stores the matched platform for controller u
    # match_v[v] stores the matched controller for platform v
    match_u = [0] * (q + 1)  # 1-indexed
    match_v = [0] * (q + 1)  # 1-indexed, for platforms q+1 to 2*q
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v - q]:  # Convert platform id to 1-based index
                continue
            visited[v - q] = True
            
            # If v is unmatched or we can find an augmenting path from v's match
            if match_v[v - q] == 0 or dfs(match_v[v - q], visited):
                match_u[u] = v
                match_v[v - q] = u
                return True
        return False
    
    matching = 0
    while True:
        visited = [False] * (q + 1)
        found_augmenting_path = False
        
        for u in range(1, q + 1):
            if match_u[u] == 0:  # If u is unmatched
                if dfs(u, visited):
                    found_augmenting_path = True
                    
        if not found_augmenting_path:
            break
            
        matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_u[u])
    else:
        print("NO")

solve()