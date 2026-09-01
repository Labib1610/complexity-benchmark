import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))

    # Check for Type 1: Triangle (3 edges)
    for u, v in edges:
        # For each edge (u, v), check if there exists w such that
        # (u, w) and (v, w) are also edges.
        # Iterate over the smaller adjacency set for efficiency.
        if len(adj[u]) < len(adj[v]):
            common_neighbors = adj[u]
            node_u, node_v = u, v
        else:
            common_neighbors = adj[v]
            node_u, node_v = v, u
        
        for w in common_neighbors:
            if w != node_v and w in adj[node_v]:
                # Found triangle u, v, w
                # Sort to ensure a < b < c
                a, b, c = sorted((u, v, w))
                print(a, b, c)
                return

    # Check for Type 2: Star (0 edges)
    # We need a triplet {a, b, c} with no edges between them.
    # This means for any pair, e.g., (a, b), b is not in adj[a].
    # Strategy: Iterate 'a' from 1 to n. For each 'a', iterate 'b' > a.
    # If (a, b) is not an edge, find 'c' > b such that (a, c) and (b, c) are not edges.
    
    # To speed up checking, convert adjacency sets to sorted lists for binary search
    # or simply iterate. Since we stop at the first find, simple iteration is best.
    
    for a in range(1, n + 1):
        # We need b > a.
        # b is valid if b not in adj[a].
        # We can iterate b from a+1 to n.
        for b in range(a + 1, n + 1):
            if b in adj[a]:
                continue
            
            # (a, b) is a non-edge. Now find c > b.
            # c must not be in adj[a] AND not in adj[b].
            for c in range(b + 1, n + 1):
                if c not in adj[a] and c not in adj[b]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()