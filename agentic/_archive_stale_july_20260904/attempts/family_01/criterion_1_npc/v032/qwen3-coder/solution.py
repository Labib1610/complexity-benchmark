def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible assignments in lexicographical order
    # We'll use backtracking with constraint propagation
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' violates any constraints
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0  # backtrack
                
        return False
    
    # This approach might be too slow for larger inputs
    # Let's try a more efficient approach with constraint checking
    
    # Since we want lexicographically smallest, we try colors 1,2,3 in order
    # for each node
    
    def solve_with_backtracking():
        # Try to assign colors to nodes 1 through n
        if backtrack(1):
            return True
        return False
    
    # For better performance, let's check if the graph is 3-colorable
    # with a more efficient approach
    
    if solve_with_backtracking():
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()