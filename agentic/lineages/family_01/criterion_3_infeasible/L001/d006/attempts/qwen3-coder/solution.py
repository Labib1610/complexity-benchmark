import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    index = 2
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each edge (u,v), we look for a third node w such that 
    # w is connected to both u and v, forming a triangle.
    # We want the lexicographically smallest such triple.
    
    # To find it efficiently, we'll iterate through potential triples
    # in lexicographical order.
    
    # First, sort adjacency lists for consistent processing
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # Try all combinations (u, v, w) where u < v < w
    # Since we want the lexicographically smallest, we iterate u from 1 to n,
    # for each u, v from neighbors of u greater than u,
    # for each v, w from neighbors of both u and v greater than v.
    
    for u in range(1, n+1):
        if u not in adj:
            continue
        for v in adj[u]:
            if v <= u:
                continue
            # Now find w such that w > v and w is neighbor of both u and v
            for w in adj[v]:
                if w <= v:
                    continue
                if w in adj[u]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()