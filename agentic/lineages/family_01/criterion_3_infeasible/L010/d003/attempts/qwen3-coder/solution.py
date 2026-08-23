import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list and edge set for O(1) lookup
    adj = defaultdict(set)
    edges = set()
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.add((u, v))
    
    # Convert adjacency lists to sorted lists for deterministic iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # Iterate through all possible triplets (a,b,c) with a<b<c
    # We'll iterate a from 1 to n, b from neighbors of a, c from common neighbors of a and b
    found = False
    result = None
    
    for a in range(1, n+1):
        if a not in adj:
            continue
        for b in adj[a]:
            if b <= a:
                continue
            # Find common neighbors of a and b for candidate c
            if a in adj and b in adj:
                for c in adj[a]:
                    if c <= b:
                        continue
                    # Check if b-c is an edge and a-c is an edge
                    if c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    main()