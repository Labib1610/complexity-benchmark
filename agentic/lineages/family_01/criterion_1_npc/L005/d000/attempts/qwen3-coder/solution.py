def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list representation of incompatibilities
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph
    colors = [0] * (n + 1)  # 0 means uncolored, 1,2,3 are the three colors
    
    def is_safe(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        if colors[node] != 0:
            return backtrack(node + 1)
            
        for color in range(1, 4):
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        
        return False
    
    # Run backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()