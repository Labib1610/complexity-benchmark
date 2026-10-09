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
    
    # Color assignment: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each connected component
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1  # Start with color 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # 1->2, 2->1
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If we reach here, a valid configuration exists
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    print(" ".join(result))

solve()