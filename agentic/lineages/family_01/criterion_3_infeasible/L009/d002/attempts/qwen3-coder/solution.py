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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, sort its adjacency list
    for node in adj:
        adj[node] = sorted(adj[node])
    
    # We want to find the lexicographically smallest triangle
    # So we iterate through all edges and for each edge (u,v) with u<v,
    # we look for a third node w such that w is connected to both u and v
    # and u < v < w
    
    min_trio = None
    
    # Iterate through all edges
    for u in range(1, n+1):
        if u not in adj:
            continue
        for v in adj[u]:
            if v <= u:
                continue  # Ensure u < v
            # Now we need to find w such that w is connected to both u and v, and w > v
            # To do this efficiently, we can iterate through the neighbors of u and v
            # and find common neighbors greater than v
            
            # Get neighbors of u and v that are greater than v
            neigh_u = set(x for x in adj[u] if x > v)
            neigh_v = set(x for x in adj[v] if x > v)
            
            # Find common neighbors
            common = neigh_u & neigh_v
            if common:
                w = min(common)
                trio = (u, v, w)
                if min_trio is None or trio < min_trio:
                    min_trio = trio
    
    if min_trio:
        print(min_trio[0], min_trio[1], min_trio[2])

if __name__ == "__main__":
    main()