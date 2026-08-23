def tier_allocation(n, m, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [0] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        colors[start] = 1
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 1 if current_color == 3 else current_color + 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    return False
        return True
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    result = []
    for i in range(1, n + 1):
        result.append(str(colors[i]))
        
    print("YES")
    print(" ".join(result))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m+1]]
tier_allocation(n, m, edges)