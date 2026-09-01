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
    
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
        edges.append((u, v))
    
    # Sort edges to iterate in lexicographical order (u < v)
    sorted_edges = []
    for u, v in edges:
        if u > v:
            u, v = v, u
        sorted_edges.append((u, v))
    sorted_edges.sort()
    
    # Threshold for choosing algorithm
    # If m is large, we use O(m sqrt(m)) algorithm
    # If m is small, we use O(m^2) algorithm
    # The threshold is chosen based on constraints n <= 2000, m <= 2e5
    # sqrt(2e5) approx 447
    # We set threshold to 450
    threshold = 450
    
    if m > threshold:
        # O(m sqrt(m)) algorithm
        # Identify heavy nodes (degree > sqrt(m))
        limit = int(m**0.5)
        is_heavy = [False] * (n + 1)
        for i in range(1, n + 1):
            if deg[i] > limit:
                is_heavy[i] = True
        
        # Check for triangles involving at least one light node
        # Iterate edges in sorted order
        for u, v in sorted_edges:
            # We check if there exists w such that u-w and v-w exist
            # We iterate through neighbors of the light node
            if not is_heavy[u]:
                # u is light, iterate neighbors of u
                for w in range(1, n + 1):
                    if adj[u][w]:
                        if w != v and adj[v][w]:
                            # Found triangle u, v, w
                            res = sorted([u, v, w])
                            print(res[0], res[1], res[2])
                            return
            elif not is_heavy[v]:
                # v is light, iterate neighbors of v
                for w in range(1, n + 1):
                    if adj[v][w]:
                        if w != u and adj[u][w]:
                            # Found triangle u, v, w
                            res = sorted([u, v, w])
                            print(res[0], res[1], res[2])
                            return
            # If both u and v are heavy, we skip for now
        
        # If no triangle found with light node, check heavy-heavy-heavy triangles
        # Since we iterated all edges with at least one light endpoint,
        # any remaining triangle must be heavy-heavy-heavy.
        # We iterate edges again, checking only heavy-heavy edges.
        for u, v in sorted_edges:
            if is_heavy[u] and is_heavy[v]:
                # Both heavy, find common neighbor w
                # w must also be heavy (otherwise found earlier)
                # Iterate through heavy nodes only
                # Number of heavy nodes is at most 2*m / sqrt(m) = 2*sqrt(m)
                # So this is O(m * sqrt(m))
                for w in range(1, n + 1):
                    if is_heavy[w] and w != u and w != v:
                        if adj[u][w] and adj[v][w]:
                            res = sorted([u, v, w])
                            print(res[0], res[1], res[2])
                            return
    else:
        # O(m^2) algorithm
        # Iterate edges in sorted order
        for u, v in sorted_edges:
            # Find w such that u-w and v-w
            for w in range(1, n + 1):
                if w != u and w != v:
                    if adj[u][w] and adj[v][w]:
                        res = sorted([u, v, w])
                        print(res[0], res[1], res[2])
                        return

if __name__ == '__main__':
    solve()