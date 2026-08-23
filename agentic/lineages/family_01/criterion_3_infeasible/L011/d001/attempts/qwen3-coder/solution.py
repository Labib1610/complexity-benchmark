import sys
from itertools import combinations

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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    min_signature = float('inf')
    result = None
    
    for u, v in edges:
        if u >= v:
            continue
        # Find common neighbors of u and v
        common = adj[u] & adj[v]
        for w in common:
            if w > v:
                # Form triplet (u, v, w) with u < v < w
                sig = u * 10**8 + v * 10**4 + w
                if sig < min_signature:
                    min_signature = sig
                    result = (u, v, w)
    
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()