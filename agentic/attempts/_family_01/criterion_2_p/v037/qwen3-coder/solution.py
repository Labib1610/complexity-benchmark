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
    
    # Color nodes with BFS to check bipartiteness
    color = {}  # 1 or 2, None means unvisited
    result = [None] * (n + 1)  # result[i] stores the shift for worker i
    
    # Process each connected component
    for start in range(1, n + 1):
        if start not in color:  # Unvisited node
            queue = deque([start])
            color[start] = 1
            result[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 2 if current_color == 1 else 1
                
                for neighbor in adj[node]:
                    if neighbor not in color:
                        color[neighbor] = next_color
                        result[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    print("YES")
    # For unassigned workers (isolated nodes), assign shift 1
    output = []
    for i in range(1, n + 1):
        if result[i] is None:
            output.append("1")
        else:
            output.append(str(result[i]))
    print(" ".join(output))

solve()