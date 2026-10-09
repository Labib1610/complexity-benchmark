import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color assignment: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each connected component
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - current_color  # Flip between 1 and 2
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")
        else:
            result.append(str(color[i]))
    
    print(" ".join(result))

solve()