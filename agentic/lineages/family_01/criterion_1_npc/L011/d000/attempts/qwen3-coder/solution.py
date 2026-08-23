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
    colors = [0] * (n + 1)  # 0 means uncolored
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' is valid
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0  # backtrack
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()