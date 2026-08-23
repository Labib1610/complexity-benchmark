import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color graph with 2 colors (1 and 2)
    # This is equivalent to checking if the graph is bipartite
    color = [0] * (n + 1)  # 0 means unvisited, 1 and 2 are the two colors
    
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to color this component
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If we get here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

solve()