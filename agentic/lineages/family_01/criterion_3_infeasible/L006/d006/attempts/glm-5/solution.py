import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # Threshold for switching to O(M*sqrt(M)) algorithm
    # Based on problem constraints n <= 2000, m <= 2*10^5
    # If m is small, O(n^3) is too slow. If m is large, O(n^3) is too slow.
    # We use the threshold logic common for triangle finding in graphs.
    threshold = int((2 * m) ** 0.5)
    
    best_a, best_b, best_c = n + 1, n + 1, n + 1
    
    # Iterate through all edges to find triangles
    # Since we need the lexicographically smallest triangle, we can iterate edges
    # and check for common neighbors.
    # To ensure we find the smallest, we iterate edges (u, v) with u < v.
    # For each common neighbor w, we check the triangle (u, v, w).
    # Since we iterate u from 1 to n, and v from u+1 to n, the first valid triangle found
    # might not be the absolute smallest if we don't check w carefully.
    # However, for a fixed u, the smallest triangle involving u is found by smallest v and smallest w.
    
    # We can iterate u from 1 to n.
    # For each u, iterate v > u such that edge (u, v) exists.
    # Then iterate w > v such that edges (u, w) and (v, w) exist.
    # This guarantees we find the lexicographically first triangle.
    
    # Optimization: 
    # If deg[u] <= threshold, iterate neighbors v of u where v > u.
    #   Then iterate neighbors w of u where w > v.
    #   Check if edge (v, w) exists.
    # If deg[u] > threshold, u is a "heavy" node.
    #   We can iterate all pairs of heavy nodes (v, w) where v < w.
    #   If (v, w) is an edge, check if u forms a triangle with them.
    #   This part is efficient because the number of heavy nodes is small.
    
    # However, a simpler approach that fits the constraints and logic:
    # Iterate u from 1 to n.
    # If deg[u] is small, use the neighbor iteration method.
    # If deg[u] is large, we might skip or use a different method, 
    # but actually, if deg[u] is large, iterating neighbors is slow.
    # But we can just iterate all edges (u, v) and check common neighbors w.
    # To handle the heavy node case efficiently, we can iterate edges and check common neighbors.
    # If both u and v are heavy, iterating common neighbors might be slow if we just list them.
    # But we can iterate the node with smaller degree.
    
    # Let's stick to the degree-based strategy.
    
    for u in range(1, n + 1):
        if deg[u] == 0:
            continue
            
        if deg[u] <= threshold:
            # u is light, iterate pairs of neighbors
            neighbors = [v for v in range(1, n + 1) if adj[u][v]]
            # We want v < w for correct ordering, but we need u < v < w for the triangle.
            # Since we iterate u from 1 to n, any triangle (u, v, w) with u < v < w will be found here.
            # We just need to ensure we find the smallest one.
            for i in range(len(neighbors)):
                v = neighbors[i]
                if v <= u:
                    continue
                for j in range(i + 1, len(neighbors)):
                    w = neighbors[j]
                    if w <= v:
                        continue
                    if adj[v][w]:
                        # Found a triangle u, v, w
                        if u < best_a or (u == best_a and v < best_b) or (u == best_a and v == best_b and w < best_c):
                            best_a, best_b, best_c = u, v, w
                            # Since we want the lexicographically smallest, and we iterate u then v then w in order,
                            # the first one we find is the answer.
                            # We can break out early.
                            print(best_a, best_b, best_c)
                            return
    
    # If no triangle found in the light nodes pass, it must involve heavy nodes.
    # Or we can just iterate all edges (u, v) and check common neighbors w.
    # For heavy nodes, we iterate all edges.
    # Since we already checked cases where u is light, we now check where u is heavy.
    # But iterating all neighbors of a heavy node is slow.
    # Instead, we iterate all edges (v, w) and check if u connects to both.
    # Since u is heavy, v and w must be heavy too (if they weren't, the triangle would have been found when iterating the light node).
    # Actually, if u is heavy, and v is light, the triangle would be found when iterating v (the light node).
    # So we only need to check triangles formed by three heavy nodes.
    
    # Identify heavy nodes
    heavy_nodes = [i for i in range(1, n + 1) if deg[i] > threshold]
    
    # Iterate all pairs of heavy nodes
    for i in range(len(heavy_nodes)):
        u = heavy_nodes[i]
        for j in range(i + 1, len(heavy_nodes)):
            v = heavy_nodes[j]
            if not adj[u][v]:
                continue
            for k in range(j + 1, len(heavy_nodes)):
                w = heavy_nodes[k]
                if adj[u][w] and adj[v][w]:
                    # Found triangle u, v, w
                    # Sort them to a < b < c
                    nodes = sorted([u, v, w])
                    a, b, c = nodes[0], nodes[1], nodes[2]
                    if a < best_a or (a == best_a and b < best_b) or (a == best_a and b == best_b and c < best_c):
                        best_a, best_b, best_c = a, b, c
    
    print(best_a, best_b, best_c)

if __name__ == '__main__':
    solve()