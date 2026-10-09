def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # For the matrix to be singular, we need:
    # [a, b]
    # [1, 1]
    # Determinant = a*1 - b*1 = a - b = 0
    # So a = b
    # Therefore, for safety, any two connected nodes must have different values
    
    # This is a graph coloring problem with 3 colors
    # Check if the graph is 3-colorable
    
    color = [-1] * n
    
    def is_bipartite(start):
        stack = [start]
        color[start] = 1
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    stack.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # First check if the graph is bipartite
    # But we actually need 3-coloring
    
    def try_coloring():
        # Use backtracking for 3-coloring
        def backtrack(node):
            if node == n:
                return True
                
            for c in [1, 2, 3]:
                valid = True
                for neighbor in adj[node]:
                    if color[neighbor] == c:
                        valid = False
                        break
                if valid:
                    old_color = color[node]
                    color[node] = c
                    if backtrack(node + 1):
                        return True
                    color[node] = old_color
            return False
            
        # Try to color starting from node 0
        return backtrack(0)
    
    # A more efficient approach for 3-coloring
    # Since n <= 40, we might need a smarter approach
    
    # Let's use the constraint that we only have 3 colors
    # We can try all possible colorings for small components
    # But with n up to 40, even 3^40 is too large
    
    # Let's implement a proper backtracking with pruning
    
    def dfs(node):
        if node == n:
            return True
            
        for c in [1, 2, 3]:
            # Check if we can assign color c to node
            conflict = False
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    conflict = True
                    break
            if not conflict:
                color[node] = c
                if dfs(node + 1):
                    return True
                color[node] = -1
        return False
                
    # Initialize color array
    color = [-1] * n
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()