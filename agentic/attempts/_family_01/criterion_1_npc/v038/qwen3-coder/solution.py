def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Read incompatibility conditions
    incompatibilities = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        v = int(data[idx+1]) - 1
        incompatibilities.append((u, v))
        idx += 2
    
    # Valid schedule codes: positive integers s such that s^2 <= 9
    # This means s can be 1, 2, or 3
    valid_codes = [1, 2, 3]
    
    # Generate all possible assignments (3^n possibilities)
    # But since n can be up to 40, this is infeasible
    # However, we can use a greedy approach or backtracking with pruning
    
    # Since n <= 40 and each variable can take 3 values, 
    # and we have constraints, let's model this as a graph coloring problem
    # where each worker is a node and each incompatibility is an edge
    # We need to color the graph with 3 colors
    
    # Let's build the adjacency list
    adj = [[] for _ in range(n)]
    for u, v in incompatibilities:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to color the graph with 3 colors using backtracking
    color = [-1] * n  # -1 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for c in valid_codes:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1  # Backtrack
                
        return False
    
    # Start backtracking from node 0
    if not backtrack(0):
        print("NO")
    else:
        print("YES")
        print(*color)

solve()