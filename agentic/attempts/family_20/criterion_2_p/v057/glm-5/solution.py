import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))
    
    edges = []
    degA = [0] * (nA + 1)
    degB = [0] * (nB + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degA[u] += 1
        degB[v] += 1
    
    D = 0
    if nA > 0:
        D = max(D, max(degA))
    if nB > 0:
        D = max(D, max(degB))
    
    # Build adjacency lists for the bipartite graph
    adjA = [[] for _ in range(nA + 1)]
    for i, (u, v) in enumerate(edges):
        adjA[u].append((v, i))
    
    # Initialize availability arrays for greedy edge coloring
    # availA[u] stores available colors for alpha port u
    availA = [bytearray(D + 2) for _ in range(nA + 1)]
    # availB[v] stores available colors for beta port v
    availB = [bytearray(D + 2) for _ in range(nB + 1)]
    
    color = [0] * m
    
    # Process edges for each alpha port
    for u in range(1, nA + 1):
        for v, edge_idx in adjA[u]:
            # Find the smallest available color for both u and v
            c = 1
            while availA[u][c] or availB[v][c]:
                c += 1
            
            color[edge_idx] = c
            availA[u][c] = 1
            availB[v][c] = 1
            
            # Check if we need to do a swap (if deg > D/2)
            # We use the condition from the proof: if degA[u] + degB[v] > D
            # Since we process edges of u in order, current degA[u] is remaining edges
            # But we track used colors, so we check if there's a conflict to resolve
            # Actually, the greedy approach with swaps works as follows:
            # If we found a color c that is free on both, we are good.
            # But we might have blocked a color that was free on u but not on v (or vice versa)
            # The swap procedure ensures we can always find a valid coloring
            
            # Check if there's a color c' that is free on u but not on v, and vice versa
            # We need to find c1 in free_u \ used_v and c2 in free_v \ used_u
            # But since we just assigned c, we check if we need to rebalance
            
            # Simpler approach: after assigning c, check if there's a color c' < c that is free on u but not on v
            # If so, we can try to swap
            
            # Actually, let's implement the full swap procedure
            # Find c1: a color free on u but not on v (and c1 != c)
            c1 = -1
            for k in range(1, D + 1):
                if k != c and not availA[u][k] and availB[v][k]:
                    c1 = k
                    break
            
            if c1 != -1:
                # Find c2: a color free on v but not on u (and c2 != c)
                c2 = -1
                for k in range(1, D + 1):
                    if k != c and availA[u][k] and not availB[v][k]:
                        c2 = k
                        break
                
                if c2 != -1:
                    # We can potentially swap. But we need to check if there's an edge (u, v') with color c1
                    # and an edge (u', v) with color c2, and swap them
                    # For simplicity, we'll use a different approach: chain swapping
                    
                    # Find the edge (u, v') that has color c1
                    # Since we're processing edges of u, we need to find among already processed edges
                    # We'll use a dictionary to track colors for each port
                    
                    # Actually, let's use a simpler approach: track color assignments per port
                    pass
    
    # The above approach might not work correctly. Let's use a proper implementation.
    # We'll use the approach from the paper: for each edge, find a free color or swap
    
    # Reset and use proper algorithm
    color = [0] * m
    # For each port, track which color is assigned to which edge index
    colorA = [{} for _ in range(nA + 1)]  # colorA[u][c] = edge index
    colorB = [{} for _ in range(nB + 1)]  # colorB[v][c] = edge index
    
    for u in range(1, nA + 1):
        for v, edge_idx in adjA[u]:
            # Find free colors
            free_u = set(range(1, D + 1)) - set(colorA[u].keys())
            free_v = set(range(1, D + 1)) - set(colorB[v].keys())
            
            common = free_u & free_v
            if common:
                c = min(common)
                color[edge_idx] = c
                colorA[u][c] = edge_idx
                colorB[v][c] = edge_idx
            else:
                # Need to swap
                # Pick c1 from free_u - free_v (free on u, used on v)
                c1 = min(free_u - free_v)
                # Pick c2 from free_v - free_u (free on v, used on u)
                c2 = min(free_v - free_u)
                
                # Find the edge (u, v') that has color c2
                edge2_idx = colorA[u][c2]
                # Find the edge (u', v) that has color c1
                edge1_idx = colorB[v][c1]
                
                # Swap: edge (u, v') gets c1, edge (u', v) gets c2
                # But we need to check if this creates a cycle
                # Actually, we need to follow the chain
                
                # Simpler: use the fact that we can always find a valid color by swapping
                # We'll use a BFS/DFS approach to find the swap chain
                
                # For now, let's use a simpler greedy approach that works for most cases
                # and falls back to a more complex approach if needed
                
                # Actually, let's implement the proper swap chain
                # We'll use a BFS to find the alternating path
                
                # Start with c1 (free on u, used on v)
                # We want to find a path: u -c1-> v' -c2-> u' -c1-> v'' -c2-> ... until we find a free color
                
                # For simplicity, let's use a different approach
                # We'll use the fact that the graph is bipartite and D is the max degree
                # We can always find a valid coloring using at most D colors
                
                # Let's use a simpler approach: for each edge, try colors 1 to D
                # and if a color is blocked, try to swap
                
                # Reset and use a simpler approach
                pass
    
    # Let's use a proper implementation of the edge coloring algorithm
    # We'll use the approach from the paper: for each edge, find a free color or swap
    
    # Reset everything
    color = [0] * m
    # For each port, track which colors are used
    usedA = [set() for _ in range(nA + 1)]
    usedB = [set() for _ in range(nB + 1)]
    # For each port, track which edge has which color
    edgeAtA = [dict() for _ in range(nA + 1)]  # edgeAtA[u][c] = edge index
    edgeAtB = [dict() for _ in range(nB + 1)]  # edgeAtB[v][c] = edge index
    
    for u in range(1, nA + 1):
        for v, edge_idx in adjA[u]:
            # Find a free color for both u and v
            c = 1
            while c in usedA[u] or c in usedB[v]:
                c += 1
            
            if c <= D:
                color[edge_idx] = c
                usedA[u].add(c)
                usedB[v].add(c)
                edgeAtA[u][c] = edge_idx
                edgeAtB[v][c] = edge_idx
            else:
                # This shouldn't happen if D is correct
                # But if it does, we need to swap
                # Find c1: a color used on v but not on u
                c1 = 1
                while c1 not in usedB[v] or c1 in usedA[u]:
                    c1 += 1
                # Find c2: a color used on u but not on v
                c2 = 1
                while c2 not in usedA[u] or c2 in usedB[v]:
                    c2 += 1
                
                # Swap colors along the path
                # We'll use a BFS to find the alternating path
                # For simplicity, let's just swap the two colors
                # This might not always work, but let's try
                
                # Actually, let's implement the proper swap chain
                # We'll use a BFS to find the alternating path
                
                # Start with color c1 (used on v, not on u)
                # We want to find a path: v -c1-> u' -c2-> v' -c1-> u'' -c2-> ... until we find a free color
                
                # For now, let's use a simpler approach
                # We'll use the fact that the graph is bipartite and D is the max degree
                # We can always find a valid coloring using at most D colors
                
                # Let's use a different approach: for each edge, try colors 1 to D
                # and if a color is blocked, try to swap
                
                # For simplicity, let's use a greedy approach with backtracking
                pass
    
    # Let's use a proper implementation of the edge coloring algorithm
    # We'll use the approach from the paper: for each edge, find a free color or swap
    
    # Reset everything
    color = [0] * m
    # For each port, track which colors are used
    usedA = [set() for _ in range(nA + 1)]
    usedB = [set() for _ in range(nB + 1)]
    # For each port, track which edge has which color
    edgeAtA = [dict() for _ in range(nA + 1)]  # edgeAtA[u][c] = edge index
    edgeAtB = [dict() for _ in range(nB + 1)]  # edgeAtB[v][c] = edge index
    
    for u in range(1, nA + 1):
        for v, edge_idx in adjA[u]:
            # Find a free color for both u and v
            c = 1
            while c <= D and (c in usedA[u] or c in usedB[v]):
                c += 1
            
            if c <= D:
                color[edge_idx] = c
                usedA[u].add(c)
                usedB[v].add(c)
                edgeAtA[u][c] = edge_idx
                edgeAtB[v][c] = edge_idx
            else:
                # Need to swap
                # Find c1: a color used on v but not on u
                c1 = -1
                for k in range(1, D + 1):
                    if k in usedB[v] and k not in usedA[u]:
                        c1 = k
                        break
                
                # Find c2: a color used on u but not on v
                c2 = -1
                for k in range(1, D + 1):
                    if k in usedA[u] and k not in usedB[v]:
                        c2 = k
                        break
                
                if c1 == -1 or c2 == -1:
                    # This shouldn't happen
                    continue
                
                # Swap colors along the path
                # We'll use a BFS to find the alternating path
                # Start from v, follow color c1 to some u', then color c2 to some v', etc.
                # Until we find a free color
                
                # For simplicity, let's just swap the two colors
                # This might not always work, but let's try
                
                # Find the edge (u', v) that has color c1
                edge1_idx = edgeAtB[v][c1]
                # Find the edge (u, v') that has color c2
                edge2_idx = edgeAtA[u][c2]
                
                # Swap: edge (u', v) gets c2, edge (u, v') gets c1
                # But we need to check if this creates a conflict
                
                # Actually, let's implement the proper swap chain
                # We'll use a BFS to find the alternating path
                
                # Build the path
                path = []
                current_v = v
                current_c1 = c1
                current_c2 = c2
                
                while True:
                    # Find the edge (u', current_v) that has color current_c1
                    if current_c1 not in edgeAtB[current_v]:
                        break
                    edge1_idx = edgeAtB[current_v][current_c1]
                    u_prime = edges[edge1_idx][0]
                    
                    path.append((edge1_idx, current_c1, current_c2))
                    
                    # Check if current_c2 is free on u_prime
                    if current_c2 not in usedA[u_prime]:
                        # We can stop here
                        break
                    
                    # Find the edge (u_prime, v') that has color current_c2
                    edge2_idx = edgeAtA[u_prime][current_c2]
                    v_prime = edges[edge2_idx][1]
                    
                    current_v = v_prime
                    # Swap c1 and c2
                    current_c1, current_c2 = current_c2, current_c1
                
                # Now apply the swaps
                for i in range(len(path) - 1, -1, -1):
                    edge_i, col1, col2 = path[i]
                    u_i, v_i = edges[edge_i]
                    
                    # Remove old colors
                    usedA[u_i].discard(col1)
                    usedB[v_i].discard(col1)
                    del edgeAtA[u_i][col1]
                    del edgeAtB[v_i][col1]
                    
                    # Add new colors
                    usedA[u_i].add(col2)
                    usedB[v_i].add(col2)
                    edgeAtA[u_i][col2] = edge_i
                    edgeAtB[v_i][col2] = edge_i
                    
                    color[edge_i] = col2
                
                # Now assign the current edge
                color[edge_idx] = c1
                usedA[u].add(c1)
                usedB[v].add(c1)
                edgeAtA[u][c1] = edge_idx
                edgeAtB[v][c1] = edge_idx
    
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()