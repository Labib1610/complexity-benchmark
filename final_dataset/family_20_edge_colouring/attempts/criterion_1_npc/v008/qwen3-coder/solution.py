import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(len(edges) - 1)
        adj[v].append(len(edges) - 1)
    return n, m, edges, adj

def solve(n, m, edges, adj):
    # Try to 3-color the edges such that edges around each vertex have different colors
    # This is equivalent to edge coloring of a cubic graph with 3 colors
    
    color = [0] * m  # 0 means uncolored, 1,2,3 are the colors
    
    # We'll use a greedy approach with backtracking if needed
    # But for cubic graphs, if 3-edge-coloring exists, it can be found efficiently
    
    def get_used_colors_at_vertex(v):
        used = set()
        for e_idx in adj[v]:
            if color[e_idx] != 0:
                used.add(color[e_idx])
        return used
    
    def dfs(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Find available colors (not used at u and not used at v)
        used_at_u = get_used_colors_at_vertex(u)
        used_at_v = get_used_colors_at_vertex(v)
        used_colors = used_at_u | used_at_v
        
        for c in [1, 2, 3]:
            if c not in used_colors:
                color[edge_idx] = c
                # Check if we can continue
                if dfs(edge_idx + 1):
                    return True
                # Backtrack handled by setting color back to 0 when function returns
        color[edge_idx] = 0
        return False
    
    # For some inputs, simple DFS might be too slow
    # Let's try a more structured approach
    
    # Since this is a 3-regular graph and we're trying to 3-edge-color it,
    # we can model this as finding a proper edge coloring
    
    # More efficient approach: try to build the coloring incrementally
    # But let's stick with DFS for now with a better pruning strategy
    
    # Actually, let's implement a smarter backtracking algorithm
    def is_colorable():
        # Use a greedy + backtracking approach
        order = list(range(m))
        
        def backtrack(i):
            if i == m:
                return True
                
            u, v = edges[order[i]]
            
            # Determine forbidden colors at u and v
            forbidden = set()
            for e_idx in adj[u]:
                if color[e_idx] != 0 and e_idx != order[i]:
                    forbidden.add(color[e_idx])
            for e_idx in adj[v]:
                if color[e_idx] != 0 and e_idx != order[i]:
                    forbidden.add(color[e_idx])
                    
            for c in [1, 2, 3]:
                if c not in forbidden:
                    color[order[i]] = c
                    if backtrack(i + 1):
                        return True
                    color[order[i]] = 0
            return False
            
        return backtrack(0)
    
    # Sort edges to try to make the search faster
    # Put edges with more colored neighbors first
    def sort_edges():
        # Simple heuristic: process edges in some fixed order
        pass
    
    if is_colorable():
        return True, color
    else:
        return False, []

    # Let's try a completely different approach based on the structure theory
    # Every 3-regular graph that can be 3-edge-colored corresponds to a very specific structure
    
    # Actually, let's just do a clean backtracking implementation
    
def main():
    n, m, edges, adj = read_input()
    
    # Edge coloring problem: assign colors 1,2,3 to edges such that 
    # no two edges incident to the same vertex have the same color
    
    color = [0] * m
    
    def is_valid_assignment():
        # Check if current partial assignment is valid
        for v in adj:
            colors_used = []
            for e_idx in adj[v]:
                if color[e_idx] != 0:
                    colors_used.append(color[e_idx])
            if len(colors_used) != len(set(colors_used)):
                return False
        return True
    
    def solve_coloring(edge_idx):
        if edge_idx == m:
            return True
            
        # Pruning: check if current state is invalid
        u, v = edges[edge_idx]
        used_colors = set()
        for e_idx in adj[u]:
            if color[e_idx] != 0:
                if color[e_idx] in used_colors:
                    return False
                used_colors.add(color[e_idx])
        used_colors.clear()
        for e_idx in adj[v]:
            if color[e_idx] != 0:
                if color[e_idx] in used_colors:
                    return False
                used_colors.add(color[e_idx])
        
        # Try assigning each color
        used_at_u = {color[e_idx] for e_idx in adj[u] if color[e_idx] != 0}
        used_at_v = {color[e_idx] for e_idx in adj[v] if color[e_idx] != 0}
        forbidden = used_at_u | used_at_v
        
        for c in [1, 2, 3]:
            if c not in forbidden:
                color[edge_idx] = c
                if solve_coloring(edge_idx + 1):
                    return True
                color[edge_idx] = 0
                
        return False
    
    # Special case handling for small graphs
    if m <= 20 or n <= 10:
        # Use brute force
        if solve_coloring(0):
            print("YES")
            print(' '.join(map(str, color)))
        else:
            print("NO")
        return
    
    # For larger graphs, still use backtracking but with better ordering
    # Order edges by how constrained they are (more neighbors already colored)
    def edge_constraint(e_idx):
        u, v = edges[e_idx]
        count = 0
        for nei in adj[u] + adj[v]:
            if color[nei] != 0:
                count += 1
        return -count  # Negative for descending sort
    
    # Try a few times with different orderings
    success = False
    original_color = [0] * m
    
    if solve_coloring(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()