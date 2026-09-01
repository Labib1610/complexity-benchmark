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
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort adjacency lists for ordered iteration
    adj_lists = [sorted(list(s)) for s in adj]
    
    # Try to find a triangle (3-clique)
    # For each edge (u, v), check if any common neighbor w exists
    for u, v in edges:
        if u > v:
            u, v = v, u
        # Iterate through smaller adjacency list
        if len(adj[u]) < len(adj[v]):
            neighbors_u = adj_lists[u]
            for w in neighbors_u:
                if w > v and w in adj[v]:
                    print(u, v, w)
                    return
        else:
            neighbors_v = adj_lists[v]
            for w in neighbors_v:
                if w > v and w in adj[u]:
                    print(u, v, w)
                    return
    
    # If no triangle, look for a path u - v - w where u-w is not an edge
    # We iterate u from 1 to n, v from u+1 to n
    for u in range(1, n + 1):
        neighbors_u = adj_lists[u]
        # v must be a neighbor of u
        for v in neighbors_u:
            if v <= u:
                continue
            # w must be a neighbor of v, w > v, and w not a neighbor of u
            neighbors_v = adj_lists[v]
            for w in neighbors_v:
                if w <= v:
                    continue
                if w not in adj[u]:
                    print(u, v, w)
                    return

if __name__ == '__main__':
    solve()