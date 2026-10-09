def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible colorings in lexicographical order
    # Use backtracking with early termination
    coloring = [0] * (n + 1)  # 0 means uncolored
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if coloring[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True  # All nodes colored
        
        # Try colors 1, 2, 3 in order (lexicographical)
        for color in range(1, 4):
            if is_valid(node, color):
                coloring[node] = color
                if backtrack(node + 1):
                    return True
                coloring[node] = 0  # Backtrack
        
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*coloring[1:])
    else:
        print("NO")

solve()