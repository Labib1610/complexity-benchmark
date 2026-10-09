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
    
    # Color array: 0 means unvisited, 1, 2, 3 are colors
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
            
            # Try to assign colors to neighbors
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    # Assign the next available color (1, 2, or 3) different from current
                    # We'll use a greedy approach: try colors 1, 2, 3 in order
                    used_colors = set()
                    for nn in adj[neighbor]:
                        if color[nn] != 0:
                            used_colors.add(color[nn])
                    
                    # Find a color from {1,2,3} that's not used by neighbors
                    found_color = False
                    for c in range(1, 4):
                        if c not in used_colors:
                            color[neighbor] = c
                            found_color = True
                            queue.append(neighbor)
                            break
                    
                    if not found_color:
                        print("NO")
                        return
                else:
                    # Check if there's a conflict
                    if color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we get here, we have a valid 3-coloring
    print("YES")
    print(*color[1:])

solve()