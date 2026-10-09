import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, build adjacency list
    # We'll check for triangles by iterating over all triplets
    
    # To optimize, we can iterate over all combinations of 3 nodes
    # But since n <= 2000, C(2000,3) is too large
    # Instead, we use the edge list and for each edge (u,v), 
    # we look for a third node w such that (u,w) and (v,w) also exist
    
    # First, let's store all edges in a set for O(1) lookup
    edge_set = set()
    for u, v in edges:
        edge_set.add((u, v))
        edge_set.add((v, u))
    
    found_triangles = []
    
    # Iterate through all edges
    for u, v in edges:
        if u > v:
            continue  # To avoid duplicate checks
        # Now look for a node w such that both (u,w) and (v,w) exist
        # We'll iterate through neighbors of u
        for w in adj[u]:
            if w == v:
                continue
            # Ensure we don't count same triangle multiple times
            if u < v < w or u < w < v or v < u < w or v < w < u or w < u < v or w < v < u:
                key = tuple(sorted([u, v, w]))
                if key not in found_triangles:
                    # Check if it forms a triangle
                    if (v, w) in edge_set or (w, v) in edge_set:
                        found_triangles.append(key)
    
    # More efficient approach:
    # For each triplet (i,j,k) with i<j<k, check if all three edges exist
    # But we need to do it smartly
    
    # Let's create a neighbor dictionary for fast access
    neighbors = [set() for _ in range(n+1)]
    for u,v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # Convert to lists for faster iteration
    neighbor_list = [list(neighbors[i]) for i in range(n+1)]
    neighbor_set = [set(neighbors[i]) for i in range(n+1)]
    
    min_triangle = None
    
    # For each pair (i,j) where i<j, find common neighbors k such that k>j
    for i in range(1, n+1):
        for j_index in range(len(neighbor_list[i])):
            j = neighbor_list[i][j_index]
            if j <= i:
                continue
            # Now find common neighbors of i and j that are > j
            ni = neighbor_set[i]
            nj = neighbor_set[j]
            # Iterate through the smaller set for efficiency
            if len(ni) > len(nj):
                ni, nj = nj, ni
            for k in ni:
                if k > j and k in nj:
                    triangle = (i, j, k)
                    if min_triangle is None or triangle < min_triangle:
                        min_triangle = triangle
    
    if min_triangle:
        print(min_triangle[0], min_triangle[1], min_triangle[2])

if __name__ == "__main__":
    main()