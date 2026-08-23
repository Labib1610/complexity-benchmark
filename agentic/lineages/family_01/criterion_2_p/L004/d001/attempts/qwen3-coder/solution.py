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
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color graph with 2 colors (0 and 1)
    # Each node must have opposite color to its neighbors
    color = {}
    
    for start_node in adj:
        if start_node not in color:
            # BFS to color component
            queue = deque([start_node])
            color[start_node] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Verify all edges satisfy constraint
    for u, v in edges:
        if u not in color or v not in color:
            continue
        # Power values: 0-color -> 1, 1-color -> 2
        power_u = 1 if color[u] == 0 else 2
        power_v = 1 if color[v] == 0 else 2
        if power_u + power_v != 3:
            print("NO")
            return
    
    # Generate lexicographically smallest assignment
    result = []
    for i in range(1, n + 1):
        if i not in color:
            # Isolated node - assign 1 (lexicographically smallest)
            result.append("1")
        elif color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()