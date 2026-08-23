def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    for i in range(m):
        u = int(data[2 + 2*i]) - 1  # Convert to 0-indexed
        v = int(data[3 + 2*i]) - 1
        edges.append((u, v))
    
    # Try all 3^n assignments, but we can do better with backtracking
    # We want lexicographically smallest assignment
    
    # This is essentially a graph coloring problem with 3 colors
    # We need to check if the graph is 3-colorable
    
    # Use backtracking to find the lexicographically smallest valid coloring
    coloring = [-1] * n  # -1 means unassigned
    
    def is_safe(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for u, v in edges:
            if u == node and coloring[v] == color:
                return False
            if v == node and coloring[u] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for color in range(1, 4):  # Colors 1, 2, 3
            if is_safe(node, color):
                coloring[node] = color
                if backtrack(node + 1):
                    return True
                coloring[node] = -1  # Backtrack
                
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, coloring)))
    else:
        print("NO")

solve()