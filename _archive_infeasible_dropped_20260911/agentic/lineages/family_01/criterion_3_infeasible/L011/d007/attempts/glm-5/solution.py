import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Try to find a triangle
    for u in range(1, n + 1):
        neighbors = list(adj[u])
        deg_u = len(neighbors)
        for i in range(deg_u):
            v = neighbors[i]
            if v < u:
                continue
            for j in range(i + 1, deg_u):
                w = neighbors[j]
                if w < v:
                    continue
                if w in adj[v]:
                    print(u, v, w)
                    return
    
    # No triangle found, find a path u-v-w where u-w is not an edge
    # We need to find u < v < w such that (u,v) and (v,w) are edges, but (u,w) is not.
    # Since we want lexicographically smallest, we iterate u, then v, then w.
    # We need to check if (u,w) is NOT an edge.
    # We can iterate through edges (u,v) and then check neighbors of v.
    
    # Sort edges to process in order
    edges.sort()
    
    for u, v in edges:
        # We want u < v. The edge list is sorted.
        # We want to find w such that v < w, (v,w) is an edge, and (u,w) is not an edge.
        # To ensure we find the lexicographically smallest, we iterate w in increasing order.
        # We can iterate through neighbors of v that are > v.
        # Since we want u < v < w, and we are iterating edges (u,v) sorted by u then v,
        # we just need to find the smallest valid w for each (u,v).
        
        # Iterate neighbors of v
        for w in adj[v]:
            if w > v:
                # Check if (u,w) is NOT an edge
                if w not in adj[u]:
                    print(u, v, w)
                    return
    
    # The problem guarantees a solution exists.

if __name__ == '__main__':
    solve()