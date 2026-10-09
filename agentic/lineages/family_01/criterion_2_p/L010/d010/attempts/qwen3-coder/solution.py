import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, all 1s is lexicographically smallest
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color the graph with BFS/DFS - each component must be bipartite
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    for start in range(n):
        if color[start] == -1:
            # BFS to check if component is bipartite
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Not bipartite - impossible to satisfy constraints
                        print("NO")
                        return
    
    # Bipartite - construct solution
    # For lexicographically smallest, we want s[i] = 1 if color[i] = 0
    # But we need to verify this satisfies all edges
    result = []
    for i in range(n):
        if color[i] == -1:  # Isolated vertex, assign 1 (lexicographically smallest)
            result.append("1")
        elif color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    # Verify solution
    for u, v in edges:
        if (result[u] == "1" and result[v] == "1") or (result[u] == "2" and result[v] == "2"):
            print("NO")
            return
    
    print("YES")
    print(" ".join(result))

solve()