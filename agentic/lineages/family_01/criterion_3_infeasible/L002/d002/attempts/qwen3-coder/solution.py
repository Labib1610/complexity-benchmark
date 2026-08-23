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
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for consistent iteration
    for key in adj:
        adj[key] = sorted(adj[key])
    
    # We'll iterate through all edges and for each edge (u,v), we'll look for a common neighbor
    # which would form a triangle u-v-w
    
    # To ensure lexicographical order, we'll iterate u from smallest to largest,
    # and for each u, iterate through its neighbors v where v > u,
    # and for each such v, iterate through common neighbors w where w > v
    
    # Convert edges to a set for O(1) lookup
    edge_set = set(edges)
    # Also add reversed edges for easy lookup
    rev_edge_set = set()
    for u, v in edges:
        rev_edge_set.add((v, u))
    edge_set_full = edge_set.union(rev_edge_set)
    
    # Iterate through all nodes u in increasing order
    for u in sorted(adj.keys()):
        # For each neighbor v of u, where v > u
        for i, v in enumerate(adj[u]):
            if v <= u:
                continue
            # Now find common neighbors w of both u and v, where w > v
            # Iterate through neighbors of u and check if they are also neighbors of v
            adj_u_list = adj[u]
            adj_v_list = adj[v]
            
            # Use two pointers to find common elements greater than v
            i_u = 0
            i_v = 0
            len_u = len(adj_u_list)
            len_v = len(adj_v_list)
            
            while i_u < len_u and i_v < len_v:
                w_u = adj_u_list[i_u]
                w_v = adj_v_list[i_v]
                
                if w_u < v:
                    i_u += 1
                    continue
                if w_v < v:
                    i_v += 1
                    continue
                
                if w_u == w_v:
                    # Found a triangle u, v, w_u
                    print(u, v, w_u)
                    return
                elif w_u < w_v:
                    i_u += 1
                else:
                    i_v += 1

if __name__ == "__main__":
    main()