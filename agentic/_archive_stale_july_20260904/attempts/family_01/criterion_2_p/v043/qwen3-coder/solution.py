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
    colors = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if colors[start] == 0:
            queue = deque([start])
            colors[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = colors[node]
                neighbor_color = 3 - current_color  # flips 1->2, 2->1
                
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif colors[neighbor] != neighbor_color:
                        print("NO")
                        return
    
    # If we get here, it's bipartite
    print("YES")
    # For lexicographically smallest, we prefer 1 over 2 when there's choice
    # But our algorithm already ensures this by starting with color 1
    result = []
    for i in range(1, n + 1):
        if colors[i] == 0:  # Isolated node, default to 1
            result.append(1)
        else:
            result.append(colors[i])
    
    print(' '.join(map(str, result)))

solve()