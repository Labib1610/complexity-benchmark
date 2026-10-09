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
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm approach
    # But we'll use a simpler approach with DFS for this case
    
    # For each controller, try to match it with some platform
    match_controller = [0] * (q + 1)  # match_controller[i] = platform matched to controller i
    match_platform = [0] * (2 * q + 1)  # match_platform[j] = controller matched to platform j
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            # If platform v is unmatched or we can find augmenting path
            if match_platform[v] == 0 or dfs(match_platform[v], visited):
                match_controller[u] = v
                match_platform[v] = u
                return True
        return False
    
    matching = 0
    for i in range(1, q + 1):
        visited = [False] * (2 * q + 1)
        if dfs(i, visited):
            matching += 1
    
    if matching == q:
        print("YES")
        for i in range(1, q + 1):
            print(i, match_controller[i])
    else:
        print("NO")

solve()