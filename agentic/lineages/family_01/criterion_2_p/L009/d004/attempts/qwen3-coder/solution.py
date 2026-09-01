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
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge, check if p_u^2 + p_v^2 = 5
    # Possible values: 1^2 + 2^2 = 1 + 4 = 5 ✓
    #                   2^2 + 1^2 = 4 + 1 = 5 ✓
    # So each edge must connect a 1-node with a 2-node
    
    # This is a bipartite graph problem where each component must be bipartite
    # Color each component with 2 colors (1 and 2)
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    visited = [False] * n
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False  # Not bipartite
        return True
    
    # Check if all components are bipartite
    for i in range(n):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                return
    
    # Verify the solution satisfies all constraints
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Convert colors to frequency multipliers (0 -> 1, 1 -> 2)
    result = []
    for c in color:
        result.append(str(c + 1))
    
    print("YES")
    print(" ".join(result))

solve()