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
    
    # We need to find a triangle where the product of degrees in the triangle is 8
    # In a triangle, each node has degree 2 within the triangle
    # So the product is 2*2*2 = 8
    # So we just need to find any triangle
    
    # Build adjacency list with sorted neighbors for consistent processing
    adj_list = {}
    for u in adj:
        adj_list[u] = sorted(list(adj[u]))
    
    # For each edge (u,v), look for a common neighbor w to form triangle u-v-w
    # We want the lexicographically smallest triangle
    best = None
    
    # Sort edges to process in order that helps find lex smallest triangle
    sorted_edges = sorted(edges)
    
    for u, v in sorted_edges:
        if u > v:
            u, v = v, u
        # Find common neighbors of u and v
        if u in adj_list and v in adj_list:
            neighbors_u = set(adj_list[u])
            neighbors_v = set(adj_list[v])
            common = neighbors_u & neighbors_v
            
            candidates = []
            for w in common:
                # Form the triple
                triple = tuple(sorted([u, v, w]))
                candidates.append(triple)
            
            # Sort candidates to get the lex smallest for this edge
            candidates.sort()
            
            for triple in candidates:
                if best is None or triple < best:
                    best = triple
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()