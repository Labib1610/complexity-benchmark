import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the graph
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = branch 1, 2 = branch 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for i in range(1, n + 1):
        if color[i] == 0:
            queue = deque([i])
            color[i] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - current_color  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()