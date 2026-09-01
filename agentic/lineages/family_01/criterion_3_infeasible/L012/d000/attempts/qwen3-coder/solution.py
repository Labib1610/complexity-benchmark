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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle in the graph (three nodes all connected to each other)
    # That represents three sensors pairwise constrained => impossible to assign to two phases
    
    # To get the lexicographically smallest, we iterate through all triplets (i,j,k) with i<j<k
    # But doing that naively is too slow. Instead, for each edge (u,v), we look for a node w
    # such that (u,w) and (v,w) are also edges, forming a triangle.
    
    # To optimize, we can sort adjacency lists and use two pointers or intersection,
    # but since n <= 2000, a reasonably optimized O(m*sqrt(m)) or similar approach works.
    
    # Let's build a list of neighbors for each node as sorted lists for easier intersection
    for i in range(1, n+1):
        adj[i] = list(adj[i])
        adj[i].sort()
    
    best = None
    
    # For each edge (u,v), find common neighbor w
    for u, v in edges:
        if u > v:
            continue  # Ensure we process each edge only once in a consistent direction
        
        # Find intersection of adj[u] and adj[v]
        # Since lists are sorted, we can do this efficiently
        i, j = 0, 0
        while i < len(adj[u]) and j < len(adj[v]):
            if adj[u][i] == adj[v][j]:
                w = adj[u][i]
                # Found triangle u-v-w
                # Check if it's better than current best
                a, b, c = sorted([u, v, w])
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
                i += 1
                j += 1
            elif adj[u][i] < adj[v][j]:
                i += 1
            else:
                j += 1
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()