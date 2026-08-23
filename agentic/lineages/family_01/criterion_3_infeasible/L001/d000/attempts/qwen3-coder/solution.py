import sys
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a third node w such that (u,w) and (v,w) are also edges
    # We want the lexicographically smallest triad
    
    for u, v in edges:
        if u >= v:
            continue
        # Get common neighbors of u and v
        common = adj[u] & adj[v]
        if common:
            # Find the smallest w such that w > v to maintain a < b < c
            for w in sorted(common):
                if w > v:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()