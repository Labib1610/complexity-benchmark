import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Read edges
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Try to 3-color the edges such that edges sharing a vertex have different colors
    # This is equivalent to edge-coloring the graph with 3 colors
    
    # Since each vertex has degree 3, and we have exactly 3*n/2 edges,
    # this is a cubic graph with exactly 3*n/2 edges
    
    color = [0] * m  # 0 means uncolored, 1, 2, 3 are the three windows
    
    # We'll use a greedy approach with backtracking if needed
    # But first, let's try a systematic approach
    
    # For cubic graphs, if it's 3-edge-colorable, we can find a coloring
    # We'll model this as a constraint satisfaction problem
    
    # Let's try a backtracking approach
    def is_safe(edge_idx, c):
        u, v = edges[edge_idx]
        # Check all edges incident to u
        for e_idx in adj[u]:
            if color[e_idx] == c:
                return False
        # Check all edges incident to v
        for e_idx in adj[v]:
            if color[e_idx] == c:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        for c in range(1, 4):
            if is_safe(edge_idx, c):
                color[edge_idx] = c
                if backtrack(edge_idx + 1):
                    return True
                color[edge_idx] = 0
        
        return False
    
    # For performance, let's try to order edges smartly
    # Start with vertices of highest degree (but in cubic graph, all degrees are 3)
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()