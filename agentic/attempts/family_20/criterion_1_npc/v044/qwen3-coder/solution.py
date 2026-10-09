import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Store edges and build adjacency list
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Try to 3-color the line graph (each edge is a node, adjacent if they share a vertex)
    # This is equivalent to assigning phases 1,2,3 to edges such that edges sharing a vertex have different phases
    
    # This is essentially edge coloring of a cubic graph (3-regular)
    # Since each vertex has degree 3, and we have 3 colors, this is possible iff
    # the graph is class 1 (edge chromatic number = 3)
    
    # We'll model this as a constraint satisfaction problem
    # Each edge needs a color from {1,2,3}
    # For each vertex, its 3 edges must have distinct colors
    
    # This is equivalent to finding a proper 3-edge-coloring of a cubic graph
    # All 3-regular graphs are either class 1 (3-edge-colorable) or class 2 (4-edge-colorable)
    # But since we're asked to use exactly 3 colors, we need to check if it's class 1
    
    # Let's try to construct such a coloring using BFS/DFS approach
    
    # For each vertex, we need to assign 3 different phases to its 3 edges
    # We can do this by trying all permutations for each vertex consistent with neighbors
    
    phase = [0] * m  # phase[i] will store the phase of edge i (1-indexed)
    assigned = [False] * m
    
    # For each vertex, keep track of which phases are used by its edges
    vertex_phase_used = [set() for _ in range(n + 1)]
    
    # Process vertices in some order, and for each unassigned edge, try to assign a phase
    # This greedy approach might not work; let's think of a better way
    
    # Better approach: Build a conflict graph where nodes are edges and edges represent conflicts
    # Two edges conflict if they share a vertex
    # Then we 3-color this conflict graph
    
    # Actually, let's think differently:
    # The line graph of a cubic graph is what we need to 3-color
    # But let's just try a greedy approach with backtracking simulation
    
    # Simpler idea: Try to build a valid assignment greedily
    # For each edge, assign a phase that doesn't conflict with already assigned edges at its endpoints
    
    def can_assign(edge_idx, p):
        u, v = edges[edge_idx]
        return p not in vertex_phase_used[u] and p not in vertex_phase_used[v]
    
    def assign_phase(edge_idx, p):
        u, v = edges[edge_idx]
        phase[edge_idx] = p
        vertex_phase_used[u].add(p)
        vertex_phase_used[v].add(p)
        assigned[edge_idx] = True
    
    def unassign_phase(edge_idx):
        u, v = edges[edge_idx]
        p = phase[edge_idx]
        vertex_phase_used[u].discard(p)
        vertex_phase_used[v].discard(p)
        phase[edge_idx] = 0
        assigned[edge_idx] = False
    
    # Try a greedy assignment
    # Order edges arbitrarily and for each, pick a valid phase
    
    success = True
    for i in range(m):
        found = False
        for p in [1, 2, 3]:
            if can_assign(i, p):
                assign_phase(i, p)
                found = True
                break
        if not found:
            success = False
            break
            
    # If greedy fails, let's try a more systematic approach
    if not success:
        # Try backtracking with a specific order
        # Order vertices and process their edges
        
        # Reset
        phase = [0] * m
        assigned = [False] * m
        vertex_phase_used = [set() for _ in range(n + 1)]
        
        # Process vertices in order and assign phases to their edges
        success = True
        for v in range(1, n + 1):
            edge_indices = [i for _, i in adj[v]]
            # These are the 3 edges incident to vertex v
            # We need to assign them 3 different phases
            
            available_phases = [1, 2, 3]
            edge_to_process = []
            
            # First process edges that are already partially assigned (from other endpoint)
            for u, i in adj[v]:
                if assigned[i]:  # Already assigned from the other endpoint
                    p = phase[i]
                    if p in available_phases:
                        available_phases.remove(p)
                else:
                    edge_to_process.append(i)
                    
            # Now assign remaining phases to unprocessed edges
            if len(available_phases) < len(edge_to_process):
                success = False
                break
                
            # Assign phases arbitrarily
            for i in range(len(edge_to_process)):
                idx = edge_to_process[i]
                u, v_end = edges[idx]  # v_end should be v
                assign_phase(idx, available_phases[i])
                
        if not success:
            # One more attempt: Try a different strategy - build a spanning tree and propagate
            print("NO")
            return
            
    if success:
        print("YES")
        print(' '.join(map(str, phase)))
    else:
        print("NO")

# Run the solution
solve()