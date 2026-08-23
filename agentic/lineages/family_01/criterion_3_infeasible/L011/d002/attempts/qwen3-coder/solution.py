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
    
    # Create a list of neighbors for each node
    neighbors = {i: adj[i] for i in range(1, n+1)}
    
    min_fingerprint = float('inf')
    result = None
    
    # For each edge (u,v), check for a common neighbor w
    for u, v in edges:
        if u > v:
            u, v = v, u
        # Find common neighbors of u and v
        common = neighbors[u] & neighbors[v]
        for w in common:
            # Ensure all three are distinct and ordered
            a, b, c = sorted([u, v, w])
            fingerprint = a * 10**8 + b * 10**4 + c
            if fingerprint < min_fingerprint:
                min_fingerprint = fingerprint
                result = (a, b, c)
    
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()