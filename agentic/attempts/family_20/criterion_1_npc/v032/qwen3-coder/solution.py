import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Since m = 3*n/2 and each node has same degree, degree = 3*m/n = 3*3*n/2/n = 9/2
    # Wait, let's compute properly: sum of degrees = 2*m = 3*n, so average degree = 3
    # Since all nodes have same degree, each node has degree 3
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Each node has exactly 3 edges
    # We need to color edges with 3 colors such that edges incident to each node have different colors
    # This is edge coloring with 3 colors for a 3-regular graph
    
    # Try to construct such coloring
    # This is always possible for 3-regular graphs (by Vizing's theorem, chromatic index is 3 or 4)
    # For bridgeless 3-regular graphs, it's always 3
    
    color = [0] * m  # 1-indexed colors, 0 means uncolored
    
    # Check if the graph is 3-regular
    for u in range(1, n+1):
        if len(adj[u]) != 3:
            print("NO")
            return
    
    # Try to find a valid edge coloring
    # We'll use a greedy approach with backtracking if needed
    
    def can_color(edge_idx, c):
        u, v = edges[edge_idx]
        # Check if any adjacent edge already has color c
        for neighbor, nei_idx in adj[u]:
            if color[nei_idx] == c:
                return False
        for neighbor, nei_idx in adj[v]:
            if color[nei_idx] == c:
                return False
        return True
    
    def dfs(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        # Try colors 1, 2, 3
        for c in range(1, 4):
            if can_color(edge_idx, c):
                color[edge_idx] = c
                if dfs(edge_idx + 1):
                    return True
                color[edge_idx] = 0
        return False
    
    # For small graphs, this might work
    # But let's think of a better approach
    
    # Actually, since this is a 3-regular graph on n nodes with n even,
    # and m=3*n/2 edges, it should be 3-edge-colorable
    
    # Let's try a more systematic approach
    # Build the line graph and try to 3-color it
    
    # But for implementation simplicity, let's try the DFS with some optimizations
    
    # Actually, let's reconsider the mathematical approach
    # A 3-regular graph is 3-edge-colorable iff it's class 1
    # All 3-regular graphs with odd number of vertices are NOT 3-edge-colorable
    # But here n is even, so it might be possible
    
    # Let's just implement a smart backtracking
    
    def solve_coloring():
        # Sort edges by degree of endpoints for better pruning
        order = list(range(m))
        
        def backtrack(idx):
            if idx == m:
                return True
                
            edge_idx = order[idx]
            u, v = edges[edge_idx]
            
            # Find forbidden colors
            forbidden = set()
            for neighbor, nei_idx in adj[u]:
                if color[nei_idx] != 0:
                    forbidden.add(color[nei_idx])
            for neighbor, nei_idx in adj[v]:
                if color[nei_idx] != 0:
                    forbidden.add(color[nei_idx])
            
            # Try available colors
            for c in range(1, 4):
                if c not in forbidden:
                    color[edge_idx] = c
                    if backtrack(idx + 1):
                        return True
                    color[edge_idx] = 0
            return False
        
        return backtrack(0)
    
    if solve_coloring():
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()