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
    
    # Color array: 0 = unvisited, 1 and 2 are colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If we get here, it's bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:  # Isolated node, default to 1
            result.append("1")
        else:
            result.append(str(color[i]))
    print(" ".join(result))

solve()