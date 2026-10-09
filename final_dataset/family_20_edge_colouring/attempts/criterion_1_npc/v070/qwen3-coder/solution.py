import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list and edge list
    adj = defaultdict(list)
    edges = []
    
    for i in range(m):
        u, v = map(int, input().split())
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v))
    
    # Since each node has degree 3, we can try to 3-color the edges
    # This is equivalent to finding a proper edge coloring of a 3-regular graph
    # We'll use a greedy approach with backtracking if needed
    
    # For each node, we need to assign 3 different states to its 3 edges
    # This is essentially edge coloring with 3 colors for a 3-regular graph
    
    # Check if n is even (required for 3-regular graph to have perfect matching)
    if n % 2 != 0:
        print("NO")
        return
    
    # Try to construct a valid assignment
    # We'll use the fact that a 3-regular graph can be decomposed into edge-disjoint matchings
    
    # Assign states to edges
    state = [0] * m  # 0 means unassigned
    
    # For each vertex, keep track of which states are used
    used_states = defaultdict(set)
    
    # Try a greedy assignment
    def can_assign(edge_idx, s):
        u, v = edges[edge_idx]
        return s not in used_states[u] and s not in used_states[v]
    
    def assign_state(edge_idx, s):
        u, v = edges[edge_idx]
        state[edge_idx] = s
        used_states[u].add(s)
        used_states[v].add(s)
    
    def unassign_state(edge_idx):
        u, v = edges[edge_idx]
        s = state[edge_idx]
        state[edge_idx] = 0
        used_states[u].discard(s)
        used_states[v].discard(s)
    
    # Try to assign states using backtracking
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        for s in [1, 2, 3]:
            if s not in used_states[u] and s not in used_states[v]:
                assign_state(edge_idx, s)
                if backtrack(edge_idx + 1):
                    return True
                unassign_state(edge_idx)
        
        return False
    
    # This might be too slow for large inputs, let's try a more systematic approach
    
    # Since this is a 3-regular graph, we can try to find a proper edge coloring
    # A theorem states that every 3-regular graph can be edge-colored with 3 colors if and only if
    # it has a perfect matching. Since n is even, this should be possible.
    
    # Let's try a different approach: build the coloring systematically
    
    # Create a graph representation
    graph = [[] for _ in range(n + 1)]
    edge_indices = {}
    
    for i in range(m):
        u, v = edges[i]
        graph[u].append((v, i))
        graph[v].append((u, i))
        edge_indices[(u, v)] = i
        edge_indices[(v, u)] = i
    
    # Try to 3-color the edges
    color = [0] * m
    
    # For each vertex, track which colors are used on its edges
    vertex_colors = [set() for _ in range(n + 1)]
    
    # Process edges one by one
    def dfs(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Try each color
        for c in [1, 2, 3]:
            # Check if this color is available for both vertices
            if c not in vertex_colors[u] and c not in vertex_colors[v]:
                # Assign color
                color[edge_idx] = c
                vertex_colors[u].add(c)
                vertex_colors[v].add(c)
                
                # Recurse
                if dfs(edge_idx + 1):
                    return True
                    
                # Backtrack
                vertex_colors[u].remove(c)
                vertex_colors[v].remove(c)
        
        return False
    
    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()