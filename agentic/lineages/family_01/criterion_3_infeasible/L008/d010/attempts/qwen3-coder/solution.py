import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    degree = [0] * (n + 1)
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        degree[u] += 1
        degree[v] += 1
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triplet (a,b,c) such that S + U = m + 3
    # S = degree[a] + degree[b] + degree[c]
    # U = number of edges that have neither a, b, nor c
    # U = m - (edges incident to a or b or c)
    # By inclusion-exclusion:
    # edges incident to a or b or c = degree[a] + degree[b] + degree[c] 
    #                                - |E(a,b)| - |E(a,c)| - |E(b,c)|
    # Since the graph is simple, |E(a,b)| is 1 if (a,b) is an edge, 0 otherwise.
    # So, U = m - (degree[a] + degree[b] + degree[c]) + number of edges between them
    # Then, S + U = (degree[a] + degree[b] + degree[c]) + U
    #              = (degree[a] + degree[b] + degree[c]) + m - (degree[a] + degree[b] + degree[c]) + num_edges_between
    #              = m + num_edges_between
    # We want S + U = m + 3 => num_edges_between = 3
    # That means, the subgraph induced by {a,b,c} must have exactly 3 edges => it must be a triangle.
    
    # So we just need to find a triangle (a,b,c) with a < b < c that is lexicographically smallest.
    
    # Let's collect all edges in a set for fast lookup
    edge_set = set()
    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # Iterate through all triangles
    best = None
    # For each edge (u,v), look for a third node w such that (u,w) and (v,w) are also edges
    for u in range(1, n+1):
        for v in adj[u]:
            if v <= u:
                continue
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    # Found triangle u-v-w
                    if best is None or (u, v, w) < best:
                        best = (u, v, w)
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()