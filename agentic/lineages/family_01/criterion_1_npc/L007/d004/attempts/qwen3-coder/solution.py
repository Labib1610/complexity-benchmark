def solve():
    import sys
    from collections import defaultdict, deque
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color the graph with 3 colors using BFS
    # 0: uncolored, 1, 2, 3: colors
    color = [0] * (n + 1)
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        # BFS to color this component
        queue = deque([start])
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            # Try to assign a different color to each neighbor
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    # Assign the next available color (1, 2, 3 in cycle)
                    next_color = (current_color % 3) + 1
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    # Conflict: adjacent nodes have the same color
                    print("NO")
                    return
    
    # If we get here, a valid 3-coloring exists
    print("YES")
    print(*color[1:])

solve()