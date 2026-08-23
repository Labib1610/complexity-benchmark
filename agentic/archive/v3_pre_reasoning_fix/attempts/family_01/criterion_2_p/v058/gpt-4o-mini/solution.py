def dual_frequency_channel_allocation():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    
    graph = defaultdict(list)
    
    for line in data[1:m + 1]:
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [0] * (n + 1)  # Color 0 means uncolored, 1 and 2 are the two colors.
    
    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with 1
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # If uncolored, color it with next_color
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict detected
                    return False
        return True
    
    for unit in range(1, n + 1):
        if colors[unit] == 0:  # Unvisited
            if not bfs(unit):
                print("NO")
                return
    
    print("YES")
    print(" ".join(map(str, colors[1:])))
    
dual_frequency_channel_allocation()