import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
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
    
    # Convert to sorted lists for consistent iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # We want to find a triangle (three nodes all connected to each other)
    # and among all such triangles, return the lexicographically smallest one
    
    # To optimize, we'll look for triangles by checking for each edge (u,v) 
    # if there exists a node w such that (u,w) and (v,w) are also edges.
    
    # Let's create a set of edges for O(1) lookup
    edge_set = set(edges)
    # Also add the reverse edges since the graph is undirected
    reversed_edges = [(v, u) for u, v in edges]
    edge_set.update(reversed_edges)
    
    best = None
    
    # Iterate through all edges
    for u, v in edges:
        if u > v:
            continue  # To avoid duplicate checks, only consider u < v
        # Now check for common neighbors of u and v
        # Iterate through neighbors of u
        for w in adj[u]:
            if w <= v:
                continue  # Ensure w is the largest to maintain order and avoid duplicates
            # Check if v and w are connected
            if (v, w) in edge_set:
                # Found a triangle: u, v, w
                candidate = tuple(sorted([u, v, w]))
                if best is None or candidate < best:
                    best = candidate
    
    if best is None:
        # Should not happen according to problem statement
        # But just in case, let's do a brute force approach for small graphs
        nodes = list(range(1, n+1))
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                for k in range(j+1, len(nodes)):
                    u, v, w = nodes[i], nodes[j], nodes[k]
                    if (u in adj[v] and u in adj[w] and v in adj[w]):
                        print(u, v, w)
                        return
    else:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()