import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(10000)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Since m = 3n/2 and each player plays exactly 3 matches,
    # the total degree is 2m = 3n, so average degree is 3.
    # Every vertex has degree exactly 3 => cubic graph
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # We need to color the edges with 3 colors such that
    # at each vertex, all 3 edges have different colors.
    # This is equivalent to properly edge-coloring a cubic graph with 3 colors.
    
    # This is possible if and only if the graph is bipartite.
    # But actually, not all cubic graphs are 3-edge-colorable.
    # However, a cubic graph is 3-edge-colorable if and only if
    # it's class 1. All bipartite cubic graphs are class 1.
    
    # Let's try to 3-edge-color the graph.
    # For each vertex, we need to assign its 3 edges to 3 different colors.
    
    # We'll use a greedy approach with backtracking if needed.
    # Actually, since this is a cubic graph, we can try a specific algorithm.
    
    # A classical result: a cubic graph has a 3-edge-coloring if and only if
    # it has a perfect matching. Moreover, we can find such a coloring by:
    # 1. Find a perfect matching M
    # 2. Remove M to get a 2-regular graph (union of cycles)
    # 3. Color the cycles with 2 colors
    # 4. Color the matching edges with the 3rd color
    
    # Let's implement this approach.
    
    # First, find a perfect matching using a simple greedy method or blossom algorithm.
    # For simplicity, let's try a greedy approach first.
    
    def find_perfect_matching():
        matched = [False] * (n + 1)
        matching = [-1] * m
        edge_indices = list(range(m))
        
        # Try greedy matching
        for idx, (u, v) in enumerate(edges):
            if not matched[u] and not matched[v]:
                matching[idx] = True
                matched[u] = matched[v] = True
        
        # Check if we got a perfect matching
        if sum(matched[1:]) == n:
            return matching
            
        # If greedy fails, we might need a more sophisticated approach.
        # But for now, let's assume the input allows a solution.
        # Let's try a different strategy: since the problem guarantees a solution exists
        # when possible, we can attempt to construct one.
        
        return None
    
    # Alternative approach: Try to 3-color directly by DFS
    color = [-1] * m  # -1 means uncolored
    
    def is_valid_color(e_idx, c, adj_list, colors):
        u, v = edges[e_idx]
        for neighbor, nei_idx in adj_list[u]:
            if colors[nei_idx] == c:
                return False
        for neighbor, nei_idx in adj_list[v]:
            if colors[nei_idx] == c:
                return False
        return True
    
    def solve_edge_coloring(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        for c in range(3):
            if is_valid_color(edge_idx, c, adj, color):
                color[edge_idx] = c
                if solve_edge_coloring(edge_idx + 1):
                    return True
                color[edge_idx] = -1
        return False
    
    # Optimization: process vertices in order and color their edges
    def solve_by_vertex():
        color = [-1] * m
        colored = [False] * m
        
        # Process each vertex and assign colors to its 3 edges
        for v in range(1, n+1):
            edge_list = []  # list of (neighbor, edge_index)
            for neighbor, edge_idx in adj[v]:
                edge_list.append((neighbor, edge_idx))
            
            if len(edge_list) != 3:
                return None  # Not a cubic graph
                
            # Get available colors for each edge
            available_colors = []
            used_colors = set()
            
            # Determine which colors are already used by colored neighbors
            for neighbor, edge_idx in edge_list:
                if colored[edge_idx]:
                    used_colors.add(color[edge_idx])
                    
            if len(used_colors) > 3:
                return None
                
            # For uncolored edges, determine conflicts
            uncolored_edges = [(nbr, idx) for nbr, idx in edge_list if not colored[idx]]
            
            # Try to assign colors to uncolored edges
            # This is a small case (only 3 edges), so we can brute-force
            from itertools import permutations
            
            # Get colors not yet used at this vertex
            all_colors = {0, 1, 2}
            # But we also need to make sure we don't conflict with neighbors
            
            # Simple greedy approach
            for nbr, idx in edge_list:
                if not colored[idx]:
                    # Find a color not used by adjacent colored edges
                    forbidden = set()
                    other_u, other_v = edges[idx]
                    for neighbor, nei_idx in adj[other_u]:
                        if colored[nei_idx]:
                            forbidden.add(color[nei_idx])
                    for neighbor, nei_idx in adj[other_v]:
                        if colored[nei_idx]:
                            forbidden.add(color[nei_idx])
                    
                    for c in range(3):
                        if c not in forbidden:
                            color[idx] = c
                            colored[idx] = True
                            break
                    else:
                        # No valid color found
                        return None
        
        return color
    
    # Even simpler: just try backtracking on the whole thing
    def backtrack(index):
        if index == m:
            return True
        u, v = edges[index]
        # Find forbidden colors
        forbidden = set()
        for x, idx in adj[u]:
            if color[idx] != -1:
                forbidden.add(color[idx])
        for x, idx in adj[v]:
            if color[idx] != -1:
                forbidden.add(color[idx])
                
        for c in range(3):
            if c not in forbidden:
                color[index] = c
                if backtrack(index + 1):
                    return True
                color[index] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    main()