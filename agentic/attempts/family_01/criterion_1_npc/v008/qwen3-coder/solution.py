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
    
    # Color array: 0 = unvisited, 1, 2, 3 = colors
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
                    # Assign the next available color (1, 2, or 3) different from current
                    # We'll use a greedy approach: try colors 1, 2, 3 in order
                    found_color = False
                    for c in range(1, 4):
                        # Check if any neighbor already has this color
                        conflict = False
                        for n_neighbor in adj[neighbor]:
                            if color[n_neighbor] == c:
                                conflict = True
                                break
                        if not conflict:
                            color[neighbor] = c
                            queue.append(neighbor)
                            found_color = True
                            break
                    
                    if not found_color:
                        print("NO")
                        return
                else:
                    # Check for conflict with already colored neighbor
                    if color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we get here, we have a valid 3-coloring
    print("YES")
    print(*color[1:])

solve()