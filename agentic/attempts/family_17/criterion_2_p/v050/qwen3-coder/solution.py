from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Left side: command units 1 to q
    # Right side: response units q+1 to 2q
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm approach
    # But we'll use a simpler approach with DFS-based maximum matching
    
    match_command = [0] * (q + 1)  # match_command[i] = matched response unit for command i
    match_response = [0] * (q + 1)  # match_response[j] = matched command unit for response j
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v - q]:  # Adjust index for response units
                continue
            visited[v - q] = True
            
            # If v is unmatched or we can find augmenting path
            if match_response[v - q] == 0 or dfs(match_response[v - q], visited):
                match_command[u] = v
                match_response[v - q] = u
                return True
        return False
    
    matching = 0
    for i in range(1, q + 1):
        visited = [False] * (q + 1)
        if dfs(i, visited):
            matching += 1
    
    if matching < q:
        print("NO")
        return
    
    print("YES")
    for i in range(1, q + 1):
        print(i, match_command[i])

solve()