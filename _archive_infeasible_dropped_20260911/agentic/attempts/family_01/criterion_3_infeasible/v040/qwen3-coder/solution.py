import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices by ID
    vertices = sorted(adj.keys())
    
    # For each edge, check if there's a common neighbor
    # We want the lexicographically smallest triple
    best = None
    
    # Try all edges, and for each edge (u,v), look for a vertex w
    # such that (u,w) and (v,w) are also edges
    for u in vertices:
        neighbors = sorted(list(adj[u]))
        # For each pair of neighbors of u
        for i in range(len(neighbors)):
            v = neighbors[i]
            if v <= u:
                continue
            for j in range(i+1, len(neighbors)):
                w = neighbors[j]
                if w <= v:
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    # Found triangle u-v-w
                    candidate = (u, v, w)
                    if best is None or candidate < best:
                        best = candidate
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()