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
    
    # We need to find a triangle (three nodes all connected to each other)
    # We want the lexicographically smallest such triplet
    
    # Let's iterate through all edges and for each edge (u,v), check for a common neighbor
    # That would form a triangle u-v-w
    
    # To get the lex smallest, we'll process nodes in order
    # For each node u, look at its neighbors v > u
    # For each such v, look for a neighbor w of u such that w > v and w is also a neighbor of v
    
    # First, let's sort adjacency lists for consistent processing
    for i in range(1, n+1):
        adj[i] = sorted(adj[i])
    
    best = None
    
    # Iterate over all nodes u
    for u in range(1, n - 1):
        # For each neighbor v of u where v > u
        for i, v in enumerate(adj[u]):
            if v <= u:
                continue
            # Now look for a node w > v that is a neighbor of both u and v
            # To do this efficiently, we intersect the neighbors of u and v that are > v
            # Since adj lists are sorted, we can use two pointers or convert to sets
            # But since we want efficiency, let's just check neighbors of v that are > v
            # and see if they're also in adj[u]
            
            # Neighbors of u that are > v
            neigh_u = set(w for w in adj[u] if w > v)
            # Neighbors of v that are > v
            neigh_v = set(w for w in adj[v] if w > v)
            
            # Common neighbors > v
            common = neigh_u & neigh_v
            if common:
                w = min(common)
                candidate = (u, v, w)
                if best is None or candidate < best:
                    best = candidate
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()