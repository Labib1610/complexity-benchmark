import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color nodes with BFS (2-coloring for bipartite check)
    color = {}  # 1 or 2
    visited = set()
    
    # Process all components
    for start_node in range(1, n + 1):
        if start_node not in visited:
            queue = deque([start_node])
            color[start_node] = 1
            visited.add(start_node)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # flips 1->2, 2->1
                
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If we get here, it's bipartite
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

solve()