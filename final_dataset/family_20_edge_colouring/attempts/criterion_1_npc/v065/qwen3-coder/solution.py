import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    return n, m, edges, adj

def solve():
    n, m, edges, adj = read_input()
    
    # Each vertex has degree 3 (since m = 1.5*n and sum of degrees = 2*m = 3*n)
    # We need to color the edges with 3 colors such that each vertex has 
    # exactly one edge of each color (a proper 3-edge-coloring)
    
    # This is equivalent to finding a proper edge coloring where each vertex
    # is incident to exactly one edge of each color. Since each vertex has degree 3
    # and we have 3 colors, this means each color appears exactly once at each vertex.
    
    # Build the line graph - each edge becomes a vertex, adjacent edges are connected
    # In the line graph, we want to 3-color the vertices such that no two adjacent
    # vertices have the same color
    
    # But there's a better approach. Since each vertex has degree 3, we can think
    # of this as decomposing the graph into 3 perfect matchings.
    
    # However, let's use a constructive approach based on the structure.
    # The key insight is that a cubic graph (3-regular) that satisfies the condition
    # that every subset of k vertices has at most floor(1.5*k) internal edges
    # can be 3-edge-colored.
    
    # Let's try to build such a coloring greedily with backtracking if needed.
    # But given the constraints, a greedy approach should work.
    
    # Actually, since this is guaranteed to have a solution by the problem properties,
    # we can try a specific algorithm.
    
    # Try to find a proper 3-edge-coloring
    color = [0] * m  # 0 means uncolored, 1, 2, 3 are the colors
    
    def is_valid_color(edge_idx, c, color):
        u, v = edges[edge_idx]
        # Check if any adjacent edge already has color c
        for neighbor, nei_idx in adj[u]:
            if color[nei_idx] == c:
                return False
        for neighbor, nei_idx in adj[v]:
            if color[nei_idx] == c:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        # Count how many colors are already used at u and v
        used_at_u = set()
        used_at_v = set()
        for neighbor, nei_idx in adj[u]:
            if color[nei_idx] != 0:
                used_at_u.add(color[nei_idx])
        for neighbor, nei_idx in adj[v]:
            if color[nei_idx] != 0:
                used_at_v.add(color[nei_idx])
                
        # Available colors are those not used at both u and v
        for c in [1, 2, 3]:
            if c not in used_at_u and c not in used_at_v:
                if is_valid_color(edge_idx, c, color):
                    color[edge_idx] = c
                    if backtrack(edge_idx + 1):
                        return True
                    color[edge_idx] = 0
        return False
    
    # Try a greedy approach first
    success = True
    for edge_idx in range(m):
        u, v = edges[edge_idx]
        # Find available colors
        used_at_u = set()
        used_at_v = set()
        for neighbor, nei_idx in adj[u]:
            if color[nei_idx] != 0:
                used_at_u.add(color[nei_idx])
        for neighbor, nei_idx in adj[v]:
            if color[nei_idx] != 0:
                used_at_v.add(color[nei_idx])
        
        found_color = False
        for c in [1, 2, 3]:
            if c not in used_at_u and c not in used_at_v:
                color[edge_idx] = c
                found_color = True
                break
        
        if not found_color:
            success = False
            break
    
    if not success:
        # Fall back to backtracking
        color = [0] * m
        if not backtrack(0):
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()