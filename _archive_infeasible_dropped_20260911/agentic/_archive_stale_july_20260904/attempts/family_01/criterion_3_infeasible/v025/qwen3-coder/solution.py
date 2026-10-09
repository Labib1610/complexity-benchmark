import sys
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We'll iterate through all edges and for each edge (u,v), 
    # we look for a common neighbor w such that u-v-w forms a triangle.
    # To get the lexicographically smallest, we process edges in order.
    
    # First, sort the adjacency lists so we can efficiently find intersections
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    best = None
    
    # Iterate over all edges
    for u, v in edges:
        if u > v:
            u, v = v, u
        # Find common neighbors of u and v
        nu = adj[u]
        nv = adj[v]
        
        i, j = 0, 0
        candidates = []
        while i < len(nu) and j < len(nv):
            if nu[i] == nv[j]:
                w = nu[i]
                # Ensure all three are distinct and form u-v-w
                if w != u and w != v:
                    triple = tuple(sorted([u, v, w]))
                    candidates.append(triple)
                i += 1
                j += 1
            elif nu[i] < nv[j]:
                i += 1
            else:
                j += 1
        
        # Among all triangles formed with this edge, find the lex smallest
        for triple in candidates:
            if best is None or triple < best:
                best = triple
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()