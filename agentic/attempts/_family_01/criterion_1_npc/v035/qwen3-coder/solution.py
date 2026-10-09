def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Try to 3-color the graph
    color = [-1] * n  # -1 means uncolored, 0,1,2 are the three colors
    
    def is_bipartite(start):
        # Check if component is bipartite
        queue = [start]
        color[start] = 0
        while queue:
            node = queue.pop(0)
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # First check if the graph is 2-colorable (bipartite)
    visited = [False] * n
    for i in range(n):
        if color[i] == -1:
            if not is_bipartite(i):
                # Not bipartite, try 3-coloring
                color = [-1] * n
                break
    else:
        # Graph is bipartite, so 2-colorable
        print("YES")
        result = [str(c + 1) for c in color]
        print(" ".join(result))
        return
    
    # Try 3-coloring with backtracking
    def can_color(node):
        if node == n:
            return True
            
        for c in range(3):
            # Check if color c is valid for node
            valid = True
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    valid = False
                    break
            if valid:
                color[node] = c
                if can_color(node + 1):
                    return True
                color[node] = -1
        
        return False
    
    # Try to 3-color the entire graph
    if can_color(0):
        print("YES")
        result = [str(c + 1) for c in color]
        print(" ".join(result))
    else:
        print("NO")

solve()