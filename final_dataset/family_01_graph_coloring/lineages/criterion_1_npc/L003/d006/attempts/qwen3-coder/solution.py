def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Colors: 1, 2, 3
    # We need to ensure that for every edge (u,v): |color[u] - color[v]| != 0
    # That means color[u] != color[v]
    # This is a graph coloring problem with 3 colors where adjacent nodes must have different colors
    # But we also have the constraint from the matrix determinant:
    # Determinant of [[x,y],[y,x]] is x^2 - y^2 = (x-y)(x+y)
    # For full rank, det != 0, so x^2 != y^2, which means |x| != |y|
    # Since x,y are in {1,2,3}, this just means x != y.
    
    # So we need a proper 3-coloring of the graph.
    
    color = [0] * n  # 0 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        if color[node] != 0:
            return backtrack(node + 1)
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    # Try to find a valid coloring
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()