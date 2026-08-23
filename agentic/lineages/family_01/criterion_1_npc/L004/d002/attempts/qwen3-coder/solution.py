def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph using backtracking with lexicographically smallest order
    color = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the three buses
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in range(1, 4):  # Try colors 1, 2, 3 in order for lexicographically smallest
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
        
        return False
    
    # Check if graph is 3-colorable
    if not backtrack(1):
        print("NO")
    else:
        print("YES")
        print(*color[1:])  # Print colors of nodes 1 to n

solve()