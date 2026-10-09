import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    return n, m, edges, adj

def solve():
    n, m, edges, adj = read_input()
    
    # For each node, we have exactly 3 edges
    # We need to assign periods 1,2,3 to these edges such that no two edges 
    # at the same node have the same period
    
    # This is equivalent to edge coloring with 3 colors for a cubic graph
    # Since every vertex has degree 3, and we have exactly 3 periods,
    # we need a proper edge coloring with 3 colors
    
    # Let's try to find such a coloring
    # We can use a greedy approach or backtracking
    
    # Since m = 3n/2 and every vertex has degree 3, this is a cubic graph
    # Not all cubic graphs are 3-edge-colorable, but we'll try to find one
    
    # We'll model this as a constraint satisfaction problem
    # Each edge gets a color from {1,2,3}
    # For each vertex, its 3 edges must have different colors
    
    # Let's use backtracking
    color = [0] * m  # color[i] is the color of edge i (1-indexed in output)
    
    def is_valid(edge_idx, c):
        u, v = edges[edge_idx]
        # Check if any adjacent edge to u or v already has color c
        for e_idx in adj[u]:
            if color[e_idx] == c:
                return False
        for e_idx in adj[v]:
            if color[e_idx] == c:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        for c in range(1, 4):
            if is_valid(edge_idx, c):
                color[edge_idx] = c
                if backtrack(edge_idx + 1):
                    return True
                color[edge_idx] = 0
        return False
    
    # Optimization: Start with nodes that have highest degree in the constraint graph
    # But since it's a cubic graph, all nodes have degree 3
    
    # Let's try a different approach - since this is a specific structure
    # Try to find a valid coloring directly
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()