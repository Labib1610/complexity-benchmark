import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color nodes with BFS (2-coloring for bipartite check)
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    
    # Process each connected component
    for start_node in range(1, n + 1):
        if color[start_node] == -1:  # Unvisited node
            queue = deque([start_node])
            color[start_node] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        # Convert 0->1 and 1->2 for output
        result.append(str(color[i] + 1))
    print(" ".join(result))

solve()