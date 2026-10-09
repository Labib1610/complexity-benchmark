import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with finding triangles efficiently
    edges.sort()
    
    # For each node, sort its neighbors
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    # We'll iterate through each edge (u,v) and look for a common neighbor w
    # such that u < v < w and (u,w) and (v,w) are also edges
    best = None
    
    # To optimize, we'll go through each edge and find triangles
    for u in range(1, n + 1):
        neighbors = adj[u]
        # For each pair of neighbors of u
        for i in range(len(neighbors)):
            v = neighbors[i]
            if v <= u:
                continue
            # Now check for a common neighbor greater than v
            for j in range(i + 1, len(neighbors)):
                w = neighbors[j]
                if w <= v:
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    # Found a triangle u < v < w
                    candidate = (u, v, w)
                    if best is None or candidate < best:
                        best = candidate
                    break  # Since we want the lex smallest and neighbors are sorted
            if best is not None and (u, neighbors[i], neighbors[-1]) >= best:
                break  # Early termination optimization
    
    if best is None:
        # Fallback: check all edges
        for i in range(m):
            u, v = edges[i]
            if u >= v:
                continue
            # Get common neighbors of u and v that are > v
            common = []
            # Use two pointers to find common neighbors
            nu = adj[u]
            nv = adj[v]
            iu, iv = 0, 0
            while iu < len(nu) and iv < len(nv):
                if nu[iu] == nv[iv]:
                    if nu[iu] > v:
                        w = nu[iu]
                        candidate = (u, v, w)
                        if best is None or candidate < best:
                            best = candidate
                        break
                    iu += 1
                    iv += 1
                elif nu[iu] < nv[iv]:
                    iu += 1
                else:
                    iv += 1
            if best is not None:
                # Early exit if we found something and future edges can't improve
                if i + 1 < m:
                    next_u, next_v = edges[i + 1]
                    if (next_u, next_v, n) >= best:
                        break
                        
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()