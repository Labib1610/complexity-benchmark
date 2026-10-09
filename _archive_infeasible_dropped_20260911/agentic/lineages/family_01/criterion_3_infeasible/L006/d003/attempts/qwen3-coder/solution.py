import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    edge_set = set()
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
    
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle: three nodes a,b,c such that all three edges exist
    # That means we look for triangles in the graph
    
    # To get the lexicographically smallest, we iterate through all triplets (a,b,c) with a<b<c
    # But that's too slow. Instead, for each edge (a,b), we look for a node c such that (a,c) and (b,c) also exist
    
    # Let's sort the edges to help with ordering
    edges.sort()
    
    best = None
    
    # For each edge (a,b), check for common neighbors
    for a in range(1, n+1):
        if len(adj[a]) < 2:
            continue
        neighbors_a = list(adj[a])
        neighbors_a.sort()
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            for j in range(i+1, len(neighbors_a)):
                c = neighbors_a[j]
                if c <= b:
                    continue
                # Check if edge (b,c) exists
                if (b, c) in edge_set:
                    return print(a, b, c)
    
    # Fallback - should not happen due to problem guarantee
    return print(1, 2, 3)

if __name__ == "__main__":
    main()