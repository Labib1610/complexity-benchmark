import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each connected component
    for start in range(1, n + 1):
        if color[start] == 0:
            # Start BFS coloring
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Conflict found - not bipartite
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    # We already have a valid coloring, but we need the lexicographically smallest
    # Since we always start with color 1 for unvisited components, this is already optimal
    print("YES")
    print(*color[1:n+1])

solve()