def solve():
    import sys
    from collections import defaultdict
    
    # Read input
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to 3-color the graph
    color = [0] * (n + 1)  # color[i] represents the shift for technician i
    
    def is_valid_color(node, c):
        """Check if we can assign color c to node"""
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        """Try to color nodes from node onwards"""
        if node > n:
            return True
            
        # If already colored, move to next node
        if color[node] != 0:
            return backtrack(node + 1)
            
        # Try colors 1, 2, 3
        for c in range(1, 4):
            if is_valid_color(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(color[i]))
        print(" ".join(result))
    else:
        print("NO")

solve()