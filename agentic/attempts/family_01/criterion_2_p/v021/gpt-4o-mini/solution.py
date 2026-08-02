def dual_frequency_channel_allocation():
    import sys
    from collections import deque
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n + 1)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [0] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with channel 1

        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # Unvisited
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict
                    return False
        return True
    
    for i in range(1, n + 1):
        if colors[i] == 0:  # Not colored yet
            if not bfs(i):
                print("NO")
                return
    
    # Prepare output, ignore index 0
    print("YES")
    print(' '.join(map(str, colors[1:])))

dual_frequency_channel_allocation()