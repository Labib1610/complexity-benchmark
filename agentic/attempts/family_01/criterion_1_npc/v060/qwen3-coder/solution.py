def solve():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color array: -1 unvisited, 0, 1, 2 are colors (halls 1, 2, 3)
    color = [-1] * n
    
    # Check if graph is 3-colorable using BFS
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign first color
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        # Assign next color (0->1, 1->2, 2->0)
                        color[neighbor] = (current_color + 1) % 3
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: same color neighbors
                        print("NO")
                        return
    
    # If we reach here, a valid 3-coloring exists
    print("YES")
    # Convert 0,1,2 to 1,2,3 for output
    result = [str(c + 1) for c in color]
    print(" ".join(result))

solve()