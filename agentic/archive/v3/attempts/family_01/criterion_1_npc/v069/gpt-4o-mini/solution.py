def can_assign(n, restrictions):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in restrictions:
        graph[u].append(v)
        graph[v].append(u)
    
    # Attempt to color the graph using 3 colors (1, 2, 3)
    colors = [0] * (n + 1)  # 0 means uncolored

    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with 1
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_colors = {1, 2, 3} - {current_color}
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # Not colored yet
                    # Assign the smallest available color
                    colors[neighbor] = next_colors.pop()
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    return False  # Conflict detected
        return True

    for person in range(1, n + 1):
        if colors[person] == 0:  # Not colored yet
            if not bfs(person):
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, colors[1:])))

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

can_assign(n, restrictions)