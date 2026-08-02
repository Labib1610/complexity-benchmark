def relay_channel_allocation(n, m, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)  # 0 means uncolored, 1 and 2 are our colors
    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with color 1
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # If uncolored, color it
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict found
                    return False
        return True

    for i in range(1, n + 1):
        if colors[i] == 0:  # If the node is not colored yet
            if not bfs(i):
                print("NO")
                return

    print("YES")
    print(" ".join(str(colors[i]) for i in range(1, n + 1)))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m+1]]
relay_channel_allocation(n, m, edges)