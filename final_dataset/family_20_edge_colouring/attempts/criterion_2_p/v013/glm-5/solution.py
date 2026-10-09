import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))
    
    adjA = [[] for _ in range(nA + 1)]
    adjB = [[] for _ in range(nB + 1)]
    
    transfers = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        transfers.append((u, v))
        adjA[u].append(i)
        adjB[v].append(i)
    
    # Calculate T: max degree
    T = 0
    for i in range(1, nA + 1):
        T = max(T, len(adjA[i]))
    for i in range(1, nB + 1):
        T = max(T, len(adjB[i]))
    
    if T == 0:
        print("YES")
        print("")
        return
    
    # We use edge coloring on bipartite graph via matching
    # Colors are 1..T
    # We process colors one by one, finding a matching for each color
    
    # For each color c, we build a bipartite graph of uncolored edges
    # and find a maximum matching using Hopcroft-Karp
    
    # To optimize, we use adjacency lists that shrink as edges get colored
    # We maintain current lists of uncolored edges for each vertex
    
    # We'll use 1-based indexing for vertices
    # We need to map edges to their endpoints
    
    # Current uncolored edges for each vertex (stored as list of edge indices)
    # We'll use sets for O(1) deletion, but for HK we need adjacency lists
    
    # Actually, for each color, we need to build the graph from scratch
    # from the remaining uncolored edges
    
    # To make it efficient, we maintain:
    # - For each vertex, a list of uncolored edge indices
    # - We can filter this list when building the graph for a color
    
    # But with T up to 400,000 and m up to 400,000, we need O(T * sqrt(V) * E') total
    # which could be too slow
    
    # Alternative: Use the greedy approach with augmenting paths
    # For each edge, try to assign the smallest available color
    # If conflict, find an augmenting path to recolor
    
    # Let's implement the augmenting path approach
    
    # For each vertex, track which colors are used by its incident edges
    # colorA[u] = set of colors used by edges incident to Alpha vertex u
    # colorB[v] = set of colors used by edges incident to Beta vertex v
    
    # For each edge (u, v), find a color c not in colorA[u] and not in colorB[v]
    # If such c exists, assign it
    # Otherwise, find c1 in colorA[u] - colorB[v] and c2 in colorB[v] - colorA[u]
    # Then find an alternating path from u using c1 and c2, and swap colors
    
    # This is the standard edge coloring algorithm
    
    # We'll use arrays to track colors: -1 means uncolored
    colors = [-1] * m
    
    # For each vertex, track which color is used by which edge
    # edgeAtA[u][c] = edge index that uses color c at Alpha vertex u
    edgeAtA = [dict() for _ in range(nA + 1)]
    edgeAtB = [dict() for _ in range(nB + 1)]
    
    # For each edge, try to color it
    for edge_idx in range(m):
        u, v = transfers[edge_idx]
        
        # Find available colors
        # Available for u: colors not in edgeAtA[u]
        # Available for v: colors not in edgeAtB[v]
        
        # Find smallest color available for both
        found = -1
        for c in range(1, T + 1):
            if c not in edgeAtA[u] and c not in edgeAtB[v]:
                found = c
                break
        
        if found != -1:
            colors[edge_idx] = found
            edgeAtA[u][found] = edge_idx
            edgeAtB[v][found] = edge_idx
        else:
            # Need to find augmenting path
            # Find c1 in edgeAtA[u] but not in edgeAtB[v]
            # Find c2 in edgeAtB[v] but not in edgeAtA[u]
            
            c1 = -1
            for c in edgeAtA[u]:
                if c not in edgeAtB[v]:
                    c1 = c
                    break
            
            c2 = -1
            for c in edgeAtB[v]:
                if c not in edgeAtA[u]:
                    c2 = c
                    break
            
            # c1 and c2 must exist (by König's theorem)
            # Find alternating path starting from u, alternating between c1 and c2
            
            # BFS/DFS to find the path
            # We alternate: from Alpha vertex, follow c2; from Beta vertex, follow c1
            
            # path stores: list of (vertex_type, vertex_id, edge_idx)
            # vertex_type: 'A' or 'B'
            
            # We'll use DFS to find the path
            # Start from u (Alpha), we want to find a path that ends at a vertex
            # where we can place c1 or c2 without conflict
            
            # Actually, the augmenting path alternates between c1 and c2
            # Starting from u (Alpha), we follow edges with color c2 (from u's perspective)
            # Then from Beta vertex, follow edges with color c1
            # And so on, until we reach a vertex where we can swap
            
            # Let's trace the path
            path = []  # list of edge indices
            
            # We need to find a path from u using colors c1 and c2
            # that ends at a vertex where we can make a swap
            
            # visited vertices
            visitedA = set()
            visitedB = set()
            
            def dfs(curr_u, looking_for_c2):
                # curr_u is current Alpha vertex
                # looking_for_c2: if True, we're looking for an edge with color c2 from curr_u
                # if False, we're looking for an edge with color c1 from curr_u (but this is from Beta side)
                
                if looking_for_c2:
                    # From Alpha vertex, look for edge with color c2
                    if c2 in edgeAtA[curr_u]:
                        e2 = edgeAtA[curr_u][c2]
                        _, next_v = transfers[e2]
                        if next_v not in visitedB:
                            visitedB.add(next_v)
                            path.append(e2)
                            # Now from Beta vertex next_v, look for edge with color c1
                            if c1 not in edgeAtB[next_v]:
                                # Found the end of path
                                return True
                            else:
                                e1 = edgeAtB[next_v][c1]
                                next_u, _ = transfers[e1]
                                if next_u not in visitedA:
                                    visitedA.add(next_u)
                                    path.append(e1)
                                    if dfs(next_u, True):
                                        return True
                                    path.pop()
                                path.pop()
                    return False
                else:
                    # This case shouldn't happen in our structure
                    return False
            
            visitedA.add(u)
            if dfs(u, True):
                # Found augmenting path, now swap colors
                # path contains edges: e2, e1, e2, e1, ...
                # We need to swap: c1 <-> c2 for all edges in path
                
                for i, e in enumerate(path):
                    if i % 2 == 0:
                        # This edge had c2, now gets c1
                        old_c = c2
                        new_c = c1
                    else:
                        # This edge had c1, now gets c2
                        old_c = c1
                        new_c = c2
                    
                    eu, ev = transfers[e]
                    del edgeAtA[eu][old_c]
                    del edgeAtB[ev][old_c]
                    colors[e] = new_c
                    edgeAtA[eu][new_c] = e
                    edgeAtB[ev][new_c] = e
                
                # Now assign c2 to the current edge
                colors[edge_idx] = c2
                edgeAtA[u][c2] = edge_idx
                edgeAtB[v][c2] = edge_idx
            else:
                # This shouldn't happen if the graph is bipartite and T is max degree
                # But let's handle it by trying a different approach
                # Actually, this case means we need to find a different c1/c2 pair
                
                # Let's try all pairs
                found_swap = False
                for c1_candidate in edgeAtA[u]:
                    if found_swap:
                        break
                    if c1_candidate in edgeAtB[v]:
                        continue
                    for c2_candidate in edgeAtB[v]:
                        if c2_candidate in edgeAtA[u]:
                            continue
                        
                        # Try this pair
                        c1 = c1_candidate
                        c2 = c2_candidate
                        
                        path.clear()
                        visitedA.clear()
                        visitedB.clear()
                        visitedA.add(u)
                        
                        if dfs(u, True):
                            for i, e in enumerate(path):
                                if i % 2 == 0:
                                    old_c = c2
                                    new_c = c1
                                else:
                                    old_c = c1
                                    new_c = c2
                                
                                eu, ev = transfers[e]
                                del edgeAtA[eu][old_c]
                                del edgeAtB[ev][old_c]
                                colors[e] = new_c
                                edgeAtA[eu][new_c] = e
                                edgeAtB[ev][new_c] = e
                            
                            colors[edge_idx] = c2
                            edgeAtA[u][c2] = edge_idx
                            edgeAtB[v][c2] = edge_idx
                            found_swap = True
                            break
                
                if not found_swap:
                    # Fallback: just find any valid color (shouldn't happen)
                    for c in range(1, T + 1):
                        if c not in edgeAtA[u] and c not in edgeAtB[v]:
                            colors[edge_idx] = c
                            edgeAtA[u][c] = edge_idx
                            edgeAtB[v][c] = edge_idx
                            break
    
    print("YES")
    print(" ".join(map(str, colors)))

solve()