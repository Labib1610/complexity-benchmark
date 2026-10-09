import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration order
    adj_list = [sorted(s) for s in adj]
    
    # Sort vertices by degree (heuristic for finding triangles faster)
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: len(adj[x]))
    
    for u in vertices:
        neighbors_u = adj_list[u]
        # We need to find v and w such that u < v < w and both are neighbors of u
        # and v and w are connected.
        # Iterate through pairs of neighbors (v, w) where v < w and both > u
        len_u = len(neighbors_u)
        for i in range(len_u):
            v = neighbors_u[i]
            if v <= u:
                continue
            for j in range(i + 1, len_u):
                w = neighbors_u[j]
                if w <= u:
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    solve()