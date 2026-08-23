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
    
    # For each edge (u,v), we look for a third node w such that
    # u-w and v-w are also edges. That forms a triangle.
    # We want the lexicographically smallest such triangle.
    
    # To make it efficient, for each edge, we'll check the neighbors
    # of the node with smaller degree.
    
    # First, sort the edges so we process them in a consistent order
    # But actually, we want the lexicographically smallest triangle (a,b,c) with a<b<c
    # So we can iterate through all nodes a < b < c and check if all three edges exist.
    # But that's O(n^3) which might be too slow.
    
    # Better approach:
    # For each edge (u,v), find all common neighbors of u and v.
    # That will give us all triangles containing that edge.
    # We want the lexicographically smallest triangle.
    
    # Let's sort the adjacency lists for deterministic behavior
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    best = None
    
    # Iterate over all edges
    for u, v in edges:
        if u > v:
            u, v = v, u
        # Find common neighbors of u and v
        # Iterate through the adjacency list of the node with smaller degree
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        # Now adj[u] is the smaller list
        neighbors_u = set(adj[u])
        for w in adj[v]:
            if w in neighbors_u and u < v and v < w:
                triangle = (u, v, w)
                if best is None or triangle < best:
                    best = triangle
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()