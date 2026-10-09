import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Read edges
    edges = []
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        degree[u] += 1
        degree[v] += 1
    
    # Check if all degrees are the same
    d = degree[1]
    for i in range(1, n + 1):
        if degree[i] != d:
            print("NO")
            return
    
    # Number of windows equals degree
    windows = d
    
    # Try to color the edges with d colors
    # This is edge coloring of a regular graph
    # We can use Vizing's theorem - since it's regular, it can be colored with d colors
    
    # For a regular graph, we can try to construct a proper edge coloring
    # Using a greedy approach with Kempe chain swaps if needed
    
    color = [0] * m  # color[i] represents the window for edge i
    
    # For each vertex, maintain which colors are used on its incident edges
    used_colors = [set() for _ in range(n + 1)]
    
    # Process edges one by one
    for i in range(m):
        u, v = edges[i]
        
        # Find a color not used by either u or v
        found_color = -1
        for c in range(1, windows + 1):
            if c not in used_colors[u] and c not in used_colors[v]:
                found_color = c
                break
        
        if found_color == -1:
            print("NO")
            return
            
        color[i] = found_color
        used_colors[u].add(found_color)
        used_colors[v].add(found_color)
    
    print("YES")
    print(' '.join(map(str, color)))

solve()