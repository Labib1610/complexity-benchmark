import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to color this component
            queue = deque([start])
            color[start] = 1
            
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
    
    # If we get here, a valid assignment exists
    print("YES")
    # For lexicographically smallest, we want tier 1 wherever possible
    # Since we started with color 1, and alternated, this is already optimal
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

solve()