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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with early termination
    edges.sort()
    
    # We'll iterate through all edges (u,v) and look for a common neighbor w
    # such that (u,w) and (v,w) are also edges.
    
    # To make it efficient, we'll process nodes in sorted order and only check
    # neighbors that come after in sorted order to avoid duplicates
    
    # Convert adjacency lists to sorted lists for ordered iteration
    adj_list = {}
    for node in adj:
        adj_list[node] = sorted(adj[node])
    
    best = None
    
    # For each edge (u,v), find a node w such that w is connected to both u and v
    # and u < v < w to maintain a < b < c
    for u in sorted(adj_list.keys()):
        neighbors_u = adj_list[u]
        for i in range(len(neighbors_u)):
            v = neighbors_u[i]
            if v <= u:
                continue
            # Now we want w such that w > v and w in adj[v]
            neighbors_v = set(adj_list[v])
            for j in range(i+1, len(neighbors_u)):
                w = neighbors_u[j]
                if w > v and w in neighbors_v:
                    candidate = (u, v, w)
                    if best is None or candidate < best:
                        best = candidate
                    break  # Since we're looking for lex smallest and lists are sorted
            if best is not None:
                # Early exit if we found a triangle starting with current u
                # and since we're processing in order, any better solution would have been found
                pass
    
    if best is not None:
        print(best[0], best[1], best[2])
    else:
        # Fallback - should not happen due to problem guarantee
        # But let's do a general search just in case
        edge_set = set(edges)
        found = False
        for i in range(len(edges)):
            u1, v1 = edges[i]
            for j in range(i+1, len(edges)):
                u2, v2 = edges[j]
                # Check if they share a node
                shared = None
                third_edge = None
                if u1 == u2:
                    shared = u1
                    a, b, c = shared, v1, v2
                    if a > b: a,b = b,a
                    if a > c: a,c = c,a
                    if b > c: b,c = c,b
                    third_edge = (b, c)
                elif u1 == v2:
                    shared = u1
                    a, b, c = shared, v1, u2
                    if a > b: a,b = b,a
                    if a > c: a,c = c,a
                    if b > c: b,c = c,b
                    third_edge = (b, c)
                elif v1 == u2:
                    shared = v1
                    a, b, c = shared, u1, v2
                    if a > b: a,b = b,a
                    if a > c: a,c = c,a
                    if b > c: b,c = c,b
                    third_edge = (b, c)
                elif v1 == v2:
                    shared = v1
                    a, b, c = shared, u1, u2
                    if a > b: a,b = b,a
                    if a > c: a,c = c,a
                    if b > c: b,c = c,b
                    third_edge = (b, c)
                else:
                    continue
                
                if third_edge in edge_set:
                    if not found or (a,b,c) < (best[0],best[1],best[2]):
                        best = (a,b,c)
                        found = True
        
        if found:
            print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()