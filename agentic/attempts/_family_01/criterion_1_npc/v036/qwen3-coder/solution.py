import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list for conflicts
    conflicts = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        conflicts[u].add(v)
        conflicts[v].add(u)
    
    # Try to color the graph with 3 colors
    colors = [-1] * n  # -1 means uncolored
    
    def is_safe(node, color):
        for neighbor in conflicts[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def graph_coloring(node):
        if node == n:
            return True
            
        for color in range(3):  # 0, 1, 2 representing rotations 1, 2, 3
            if is_safe(node, color):
                colors[node] = color
                if graph_coloring(node + 1):
                    return True
                colors[node] = -1
        
        return False
    
    # Start coloring from node 0
    if graph_coloring(0):
        print("YES")
        print(' '.join(str(colors[i] + 1) for i in range(n)))
    else:
        print("NO")

solve()