def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list for conflicts
    conflicts = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        conflicts[u].add(v)
        conflicts[v].add(u)
    
    # Try to color the graph with 3 colors (blocks)
    # Color 1, 2, 3 represent blocks 1, 2, 3
    colors = [0] * (n + 1)  # colors[i] represents the block for technician i
    
    def is_safe(node, color):
        # Check if assigning color to node violates any constraints
        for neighbor in conflicts[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in range(1, 4):  # Try colors 1, 2, 3
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0  # Backtrack
        
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()