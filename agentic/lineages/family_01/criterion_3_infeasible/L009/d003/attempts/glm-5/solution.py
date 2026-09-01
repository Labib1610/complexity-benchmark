import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # Check for triangle (K3)
    for i in range(1, n + 1):
        # Collect neighbors of i
        neighbors_i = [j for j in range(1, n + 1) if adj[i][j]]
        k = len(neighbors_i)
        for p in range(k):
            u = neighbors_i[p]
            for q in range(p + 1, k):
                v = neighbors_i[q]
                if adj[u][v]:
                    # Found triangle i, u, v
                    res = sorted([i, u, v])
                    print(res[0], res[1], res[2])
                    return
    
    # Check for complement triangle (K3 in complement graph)
    # Since no triangle in G, we look for 3 vertices with no edges between them in G.
    # We use the property: if no vertex has degree >= n-2, then such a triple exists.
    # Proof: If all deg[v] <= n-3, then complement degree >= 2.
    # Complement graph has min degree >= 2, so it contains a cycle.
    # Since G has no triangle, complement has no independent set of size 3? No.
    # Wait, if G has no triangle, complement might have triangle.
    # If complement has no triangle, then G has no independent set of size 3.
    # Turan's theorem: If G has no independent set of size 3, m >= n^2/4.
    # If m < n^2/4, then independent set of size 3 exists.
    # If m >= n^2/4, then by Turan, G is close to complete bipartite.
    # In a complete bipartite graph, vertices in the same part have no edges.
    # If a part has size >= 3, we have our triple.
    # If both parts have size <= 2, then n <= 4.
    # For n=4, K_{2,2} has m=4. We need to check if m < 4 or parts are larger.
    # Actually, the condition deg[v] <= n-3 is sufficient.
    # If deg[v] <= n-3, then v has at least 2 non-neighbors.
    # Let u, w be non-neighbors of v. If u, w are non-adjacent, {v, u, w} is the triple.
    # If u, w are adjacent, we continue.
    # We need to find such a triple efficiently.
    
    # Find a vertex with degree <= n-3
    start_node = -1
    for i in range(1, n + 1):
        if deg[i] <= n - 3:
            start_node = i
            break
    
    if start_node != -1:
        v = start_node
        # Find non-neighbors of v
        non_neighbors = [j for j in range(1, n + 1) if j != v and not adj[v][j]]
        # Try all pairs of non-neighbors
        for p in range(len(non_neighbors)):
            u = non_neighbors[p]
            for q in range(p + 1, len(non_neighbors)):
                w = non_neighbors[q]
                if not adj[u][w]:
                    res = sorted([v, u, w])
                    print(res[0], res[1], res[2])
                    return
    
    # If control reaches here, it implies all degrees are >= n-2.
    # This means the graph is almost complete.
    # Since G has no triangle (checked earlier), and degrees are high,
    # the only possibility is n=4 and G is K_{2,2} (degrees are 2, n-2=2).
    # Or n=3, but n>=3. If n=3, degrees are 0, 1, or 2.
    # If n=3 and no triangle, max degree is 1 (path P3). deg <= 0 = n-3. Handled above.
    # So n must be 4.
    # In K_{2,2}, degrees are 2. n-3 = 1. deg >= 2 > 1.
    # So this block handles the K_{2,2} case.
    # In K_{2,2}, vertices are {1,2} and {3,4}. No edges within parts.
    # Any two vertices in the same part form a valid triple with any other vertex?
    # No, {1, 2, 3}: 1-2 no edge, 1-3 edge, 2-3 edge. Valid.
    # We just need to find two vertices u, v with no edge between them.
    # Then pick any third vertex w.
    # The triple {u, v, w} will have only edges (u,w) and (v,w) (or none).
    # Since u-v is not an edge, it's a valid certificate.
    
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if not adj[u][v]:
                # Found non-adjacent pair u, v
                # Pick the smallest w != u, v
                for w in range(1, n + 1):
                    if w != u and w != v:
                        res = sorted([u, v, w])
                        print(res[0], res[1], res[2])
                        return
    
if __name__ == '__main__':
    solve()