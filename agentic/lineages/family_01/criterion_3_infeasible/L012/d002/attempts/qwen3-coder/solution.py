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
    
    # For each edge (u,v), we look for a node w such that:
    # w is connected to both u and v
    # This forms a triangle: u-v-w-u
    
    # We'll iterate through all edges and for each edge (u,v)
    # we'll find common neighbors of u and v
    
    # To ensure lexicographical order, we'll process edges in a sorted way
    # But since we want the lexicographically smallest triple, 
    # we'll generate all triangles and pick the smallest
    
    triangles = []
    
    for u in range(1, n + 1):
        neighbors = list(adj[u])
        neighbors.sort()
        # For each pair of neighbors of u
        for i in range(len(neighbors)):
            v = neighbors[i]
            if v <= u:
                continue
            for j in range(i + 1, len(neighbors)):
                w = neighbors[j]
                if w <= u:
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    # Found triangle u-v-w
                    triple = tuple(sorted([u, v, w]))
                    triangles.append(triple)
    
    # Sort triangles lexicographically
    triangles.sort()
    
    # Output the first (lexicographically smallest)
    result = triangles[0]
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()