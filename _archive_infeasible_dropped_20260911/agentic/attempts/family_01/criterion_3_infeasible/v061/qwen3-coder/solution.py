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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle in the graph (three nodes all connected to each other)
    # That means we need three nodes a, b, c such that (a,b), (a,c), and (b,c) are all edges
    
    # To find the lexicographically smallest triangle:
    # We can iterate through all edges (u,v) with u < v
    # For each such edge, we look for a node w such that:
    # w is connected to both u and v
    # and u < v < w to maintain order
    
    # To make it efficient, for each edge (u,v), we iterate through the neighbors of u
    # and check if they are also neighbors of v and greater than v
    
    # First, let's sort the adjacency lists to help with ordering
    for node in adj:
        adj[node] = sorted(adj[node])
    
    best = None
    
    # Iterate through all edges
    for u in range(1, n+1):
        if u not in adj:
            continue
        for v in adj[u]:
            if v <= u:
                continue
            # Now we look for w such that w is connected to both u and v, and w > v
            # To do this efficiently, we iterate through neighbors of u that are > v
            # and check if they are also neighbors of v
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    candidate = (u, v, w)
                    if best is None or candidate < best:
                        best = candidate
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()