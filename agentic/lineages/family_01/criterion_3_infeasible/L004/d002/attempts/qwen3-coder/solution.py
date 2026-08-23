import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        index += 2
    
    # For each node, get its neighbors
    # We'll look for a triangle by checking for each edge (u,v)
    # if there exists a common neighbor w
    
    # To ensure lexicographical order, we sort the edges
    # But actually, we can just iterate through all edges and for each,
    # check common neighbors, keeping track of the minimum triangle found
    
    min_triangle = None
    
    # Let's try a different approach for better performance:
    # For each vertex u, look at all pairs of its neighbors (v, w)
    # If v-w is also an edge, then u-v-w forms a triangle
    
    # To maintain lexicographical order, we process vertices in order
    # and for each vertex, we examine its neighbors in order
    
    for u in range(1, n + 1):
        neighbors = sorted(list(adj[u]))
        # Check all pairs of neighbors of u
        for i in range(len(neighbors)):
            v = neighbors[i]
            for j in range(i + 1, len(neighbors)):
                w = neighbors[j]
                # Since adj is a set, this check is O(1)
                if w in adj[v]:
                    triangle = tuple(sorted([u, v, w]))
                    if min_triangle is None or triangle < min_triangle:
                        min_triangle = triangle
    
    if min_triangle:
        print(min_triangle[0], min_triangle[1], min_triangle[2])

if __name__ == "__main__":
    main()