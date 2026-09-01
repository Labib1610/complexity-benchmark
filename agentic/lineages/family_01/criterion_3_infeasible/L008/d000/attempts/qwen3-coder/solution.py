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
    
    # Convert edges to a set for O(1) lookup
    edge_set = set(edges)
    
    # We'll iterate through all edges and for each edge (u,v), 
    # we'll look for a node w such that (u,w) and (v,w) also exist
    found = False
    result = None
    
    # To get lexicographically smallest, we can iterate through 
    # nodes in order and check triangles
    
    # Create adjacency list as list of sets for fast intersection
    neighbors = [set() for _ in range(n+1)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # For each node, check pairs of its neighbors
    for a in range(1, n+1):
        if len(neighbors[a]) < 2:
            continue
        neigh_list = list(neighbors[a])
        neigh_list.sort()
        for i in range(len(neigh_list)):
            b = neigh_list[i]
            for j in range(i+1, len(neigh_list)):
                c = neigh_list[j]
                # Check if b and c are connected
                if c in neighbors[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()