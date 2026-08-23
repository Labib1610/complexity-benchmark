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
    
    # Color the graph with BFS/DFS - each node can be 1 or 2
    # If we can 2-color the graph, then it's bipartite and we can stabilize
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS coloring
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
    
    # If we reach here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:  # Isolated node
            result.append("1")
        else:
            result.append(str(color[i]))
    
    print(" ".join(result))

solve()