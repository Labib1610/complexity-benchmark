import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Read edges and build graph
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Each node has degree 3, so we can just take the first 3 neighbors
    # We need to assign shifts 1,2,3 to the 3 edges of each vertex
    
    # For each vertex, we'll try all 6 permutations of assigning shifts to its 3 edges
    # But since this is a constraint satisfaction problem, we can model it as a graph coloring
    
    # Actually, this is equivalent to edge-coloring the graph with 3 colors
    # Since every vertex has degree exactly 3, this is always possible (by Vizing's theorem)
    # and more specifically, for cubic graphs, if it's class 1, then it's 3-edge-colorable
    
    # Let's try a greedy approach with backtracking
    
    # Assignments for each edge (indexed by edge index)
    assignment = [-1] * m
    
    # For each vertex, track which shifts are used
    used_shifts = [set() for _ in range(n + 1)]
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Try shifts 1, 2, 3
        for shift in range(1, 4):
            # Check if this shift is already used by u or v
            if shift not in used_shifts[u] and shift not in used_shifts[v]:
                # Assign this shift
                assignment[edge_idx] = shift
                used_shifts[u].add(shift)
                used_shifts[v].add(shift)
                
                # Recurse
                if backtrack(edge_idx + 1):
                    return True
                    
                # Backtrack
                used_shifts[u].remove(shift)
                used_shifts[v].remove(shift)
        
        # No valid assignment found
        assignment[edge_idx] = -1
        return False
    
    # Start backtracking
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()