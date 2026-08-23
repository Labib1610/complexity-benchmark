import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No restrictions, all 1s is lexicographically smallest
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # The key insight: XOR of two values (1 or 2) equals 3 only when one is 1 and other is 2
    # This creates a bipartite graph constraint where adjacent nodes must have different values
    # Value 1 and 2 form a bipartition since 1 XOR 2 = 3
    
    # Color the graph with 2 colors (BFS)
    color = [-1] * (n + 1)  # -1 unvisited, 0 means color 1, 1 means color 2
    
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0  # Start with color 0 (value 1)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, a valid coloring exists
    # To get lexicographically smallest, we prefer assigning 1 to nodes with color 0
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()