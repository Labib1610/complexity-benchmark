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
    # We'll use a greedy approach with backtracking
    
    # For each node, we need to assign 3 different colors to its 3 edges
    # Let's try to build the coloring step by step
    
    # We'll use a different approach: since it's a 3-regular graph,
    # we can try to find a proper edge coloring
    
    color = [0] * m  # 0 means uncolored
    
    # Try to color edges one by one
    def is_valid(edge_idx, c):
        u, v = edges[edge_idx]
        # Check all edges adjacent to u
        for neighbor, idx in adj[u]:
            if color[idx] == c:
                return False
        # Check all edges adjacent to v
        for neighbor, idx in adj[v]:
            if color[idx] == c:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        for c in [1, 2, 3]:
            if is_valid(edge_idx, c):
                color[edge_idx] = c
                if backtrack(edge_idx + 1):
                    return True
                color[edge_idx] = 0
        return False
    
    # This might be too slow for large inputs
    # Let's try a more systematic approach
    
    # Since each vertex has exactly degree 3, and we have 3 colors,
    # we can try a different strategy
    
    # Try to build a valid coloring by considering the structure
    # Every 3-regular graph can be edge-colored with 3 colors if and only if
    # it doesn't contain a bridge (an edge whose removal increases connected components)
    
    # But let's just try a greedy approach with a good ordering
    
    # Sort edges by the sum of degrees of their endpoints (try constrained first)
    edge_order = []
    for i in range(m):
        u, v = edges[i]
        edge_order.append((len(adj[u]) + len(adj[v]), i))
    
    edge_order.sort(reverse=True)
    edge_indices = [x[1] for x in edge_order]
    
    def greedy_color():
        for edge_idx in edge_indices:
            u, v = edges[edge_idx]
            # Find forbidden colors
            forbidden = set()
            for neighbor, idx in adj[u]:
                if color[idx] != 0:
                    forbidden.add(color[idx])
            for neighbor, idx in adj[v]:
                if color[idx] != 0:
                    forbidden.add(color[idx])
            
            # Try to assign a valid color
            for c in [1, 2, 3]:
                if c not in forbidden:
                    color[edge_idx] = c
                    break
            else:
                # No valid color found
                return False
        return True
    
    # If greedy doesn't work, try backtracking on a smaller example
    if not greedy_color():
        # Reset colors
        color = [0] * m
        if not backtrack(0):
            print("NO")
            return
    
    # Verify the solution
    valid = True
    for u in range(1, n + 1):
        colors_at_u = set()
        for neighbor, edge_idx in adj[u]:
            if color[edge_idx] == 0:
                valid = False
                break
            colors_at_u.add(color[edge_idx])
        if not valid or len(colors_at_u) != 3:
            valid = False
            break
    
    if valid:
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()