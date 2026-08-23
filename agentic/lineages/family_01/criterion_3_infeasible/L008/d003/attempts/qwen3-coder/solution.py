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
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a third node w such that (u,w) and (v,w) exist
    best = None
    best_score = float('inf')
    
    for u, v in edges:
        if u >= n:
            continue
        # Find common neighbors of u and v
        common = adj[u] & adj[v]
        for w in common:
            if w <= u or w <= v:
                continue
            # Calculate hazard score
            score = u * (10**8) + v * (10**4) + w
            if score < best_score:
                best_score = score
                best = (u, v, w)
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()