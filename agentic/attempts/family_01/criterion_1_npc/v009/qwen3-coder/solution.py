def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all 3-colorings
    coloring = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the colors
    
    def is_valid_color(node, color):
        for neighbor in adj[node]:
            if coloring[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in range(1, 4):
            if is_valid_color(node, color):
                coloring[node] = color
                if backtrack(node + 1):
                    return True
                coloring[node] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*coloring[1:])
    else:
        print("NO")

solve()