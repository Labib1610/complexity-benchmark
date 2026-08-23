import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color nodes with BFS to check bipartiteness and find minimum cost assignment
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
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
                    # Not bipartite - impossible to assign modes
                    print("NO")
                    return
    
    # Bipartite graph - now find assignment that minimizes cost
    # Cost formula: C_i = 2*C_{i-1} + s_i - 1
    # To minimize this, we want earlier positions to have smaller s_i values
    # Since s_i can only be 1 or 2, we prefer s_i=1 for earlier positions
    
    # For each connected component, we can choose which color gets mode 1
    # We want to maximize the number of 1s in early positions
    
    # Actually, let's think differently:
    # The cost is C_n = sum over i of (s_i-1) * 2^(n-i)
    # So position i has weight 2^(n-i)
    # We want to minimize sum of (s_i-1) * 2^(n-i) = sum of (s_i-1) * 2^(n-i)
    # Since s_i is 1 or 2, (s_i-1) is 0 or 1
    # So we want to put 1s (meaning s_i-1=0) in positions with higher weights
    
    # But we're constrained by the graph coloring!
    # In each component, we have two choices for which color gets mode 1
    
    # Let's do BFS again but track components and their color assignments
    
    assignment = [0] * (n + 1)  # 0 means unset
    
    for start in range(1, n + 1):
        if assignment[start] != 0:
            continue
            
        # Find all nodes in this component
        component_nodes = []
        queue = deque([start])
        assignment[start] = 1 if color[start] == 0 else 2
        component_nodes.append(start)
        
        while queue:
            node = queue.popleft()
            node_mode = assignment[node]
            
            for neighbor in adj[node]:
                if assignment[neighbor] == 0:
                    # Assign opposite mode
                    assignment[neighbor] = 3 - node_mode  # 1->2, 2->1
                    queue.append(neighbor)
                    component_nodes.append(neighbor)
                # No need to check for conflicts since we already verified bipartiteness
    
    # Handle isolated nodes (no edges) - assign mode 1 to minimize cost
    for i in range(1, n + 1):
        if assignment[i] == 0:
            assignment[i] = 1
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

solve()