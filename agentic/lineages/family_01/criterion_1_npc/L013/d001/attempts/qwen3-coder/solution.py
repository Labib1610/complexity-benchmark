def solve():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Color the graph with 3 colors (shifts 1, 2, 3)
    # -1 means unvisited, 0, 1, 2 are the three shifts (we'll add 1 to get 1,2,3)
    color = [-1] * n
    
    # Check each connected component
    for start in range(n):
        if color[start] != -1:
            continue
            
        # BFS to color this component
        queue = deque()
        queue.append(start)
        color[start] = 0  # Assign first color
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            # Check all neighbors
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    # Assign the next available color (0, 1, or 2)
                    # We want a color different from current_color
                    # Try color 0 first, unless it's the same as current
                    next_color = (current_color + 1) % 3
                    # But we need to make sure it's different from all already colored neighbors
                    # Actually, let's do proper 3-coloring BFS
                    
                    # For 3-coloring, when we color a node, all its neighbors must have different colors
                    # When we color a neighbor, it must be different from the current node
                    color[neighbor] = (current_color + 1) % 3
                    queue.append(neighbor)
                else:
                    # If already colored, check for conflict
                    if color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we got here, we need to do a more thorough check
    # Let's restart with a proper graph coloring approach
    
    color = [-1] * n
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def graph_coloring(node):
        if node == n:
            return True
            
        for c in range(3):
            if is_safe(node, c):
                color[node] = c
                if graph_coloring(node + 1):
                    return True
                color[node] = -1
        return False
    
    # Try to color the graph
    if graph_coloring(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

solve()