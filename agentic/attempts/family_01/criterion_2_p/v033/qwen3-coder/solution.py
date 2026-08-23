import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = shift 1, 2 = shift 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            # Start BFS coloring
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Conflict found - not bipartite
                        print("NO")
                        return
    
    # If we reach here, graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")  # Isolated vertex can be assigned to any shift, choose 1
        else:
            result.append(str(color[i]))
    
    print(" ".join(result))

solve()