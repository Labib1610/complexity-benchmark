import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (3-clique) with smallest lexicographical order
    # Let's iterate through all edges and for each edge (u,v), check for a common neighbor w
    # such that u,v,w form a triangle
    
    triangles = []
    
    # To make it efficient, for each edge (u,v), we look for nodes w that are neighbors
    # of both u and v. To ensure we don't duplicate, we can assume u < v < w
    
    for u in range(1, n+1):
        neighbors = list(adj[u])
        neighbors.sort()
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
                    triangles.append((u, v, w))
    
    # Sort triangles lexicographically
    triangles.sort()
    
    # Output the first one
    res = triangles[0]
    print(res[0], res[1], res[2])

if __name__ == "__main__":
    main()