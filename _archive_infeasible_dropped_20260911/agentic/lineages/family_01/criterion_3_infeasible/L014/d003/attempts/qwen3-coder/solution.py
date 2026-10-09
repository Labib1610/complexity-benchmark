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
    
    # We need to find a triangle (three nodes all connected to each other)
    # We'll iterate through all edges and for each edge (u,v), we look for a node w
    # such that w is connected to both u and v
    
    # To optimize, we can iterate through edges and check for common neighbors
    # But to ensure we get the lexicographically smallest triplet,
    # we should process nodes in order.
    
    # Let's create a list of neighbors for each node as a set for fast lookup
    # Then, for each node u, we look at its neighbors v where v > u
    # For each such v, we look for neighbors w of u such that w > v and w is also a neighbor of v
    
    # First, let's sort adjacency lists for deterministic iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    best = None
    
    # Iterate through all nodes u
    for u in range(1, n+1):
        if u not in adj:
            continue
        # For each neighbor v of u where v > u
        for i, v in enumerate(adj[u]):
            if v <= u:
                continue
            # Now look for w in adj[u] such that w > v and w in adj[v]
            # Since adj[u] is sorted, we can start from index i+1
            for w in adj[u][i+1:]:
                if w <= v:
                    continue
                # Check if w is also a neighbor of v
                if w in adj[v]:
                    # Found a triangle: u, v, w
                    candidate = (u, v, w)
                    if best is None or candidate < best:
                        best = candidate
                    break  # Since we want the smallest w for this (u,v), and adj[u] is sorted
            if best is not None and best[0] < u:
                break
        if best is not None and best[0] < u:
            break
                
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()