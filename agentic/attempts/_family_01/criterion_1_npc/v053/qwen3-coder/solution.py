def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for the graph
    adj = [[] for _ in range(n)]
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color the graph with 3 colors using backtracking
    color = [-1] * n  # -1 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for c in range(3):  # Try colors 0, 1, 2 (representing cycles 1, 2, 3)
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1  # Backtrack
                
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))  # Convert back to 1-based indexing
    else:
        print("NO")

solve()