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
    
    # We need to find a triangle (mutually incompatible triad)
    # We'll iterate through all edges and for each edge (u,v), 
    # we look for a node w such that (u,w) and (v,w) are also edges.
    
    # To make it efficient and find the lexicographically smallest,
    # we'll process nodes in order and build adjacency sets.
    
    # Let's restructure: for each node, keep a set of neighbors
    # Then for each edge (u,v), check intersection of neighbors
    
    # To ensure lexicographical order, we'll iterate u from 1 to n,
    # for each u, iterate v > u, and for each such edge,
    # look for w > v such that (u,w) and (v,w) exist.
    
    # But to make it faster, for each edge (u,v), we look for common neighbors.
    # Since we want the lex smallest, we should process in order.
    
    # Let's sort the edges to help with ordering
    # Actually, let's just iterate through all edges and for each (u,v),
    # look for a common neighbor w such that u<v<w and (u,w),(v,w) exist.
    
    # To optimize, for each node, maintain sorted list of neighbors.
    # But since n <= 2000, a simpler approach might suffice.
    
    # Let's do: for each edge (u,v) with u<v, 
    # look for w in adj[u] intersect adj[v] such that w > v.
    
    # First, convert adjacency sets to sorted lists for easier intersection
    adj_list = [None] * (n + 1)
    for i in range(1, n + 1):
        adj_list[i] = sorted(adj[i])
    
    # Now iterate over all edges
    for u in range(1, n + 1):
        for v in adj_list[u]:
            if v <= u:
                continue
            # Now look for w in adj_list[u] and adj_list[v] with w > v
            # Since lists are sorted, we can do a merge-like intersection
            i, j = 0, 0
            while i < len(adj_list[u]) and j < len(adj_list[v]):
                nu = adj_list[u][i]
                nv = adj_list[v][j]
                if nu == nv:
                    w = nu
                    if w > v:
                        print(u, v, w)
                        return
                    i += 1
                    j += 1
                elif nu < nv:
                    i += 1
                else:
                    j += 1

if __name__ == "__main__":
    main()