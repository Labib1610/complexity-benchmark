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
    
    # We need to find a triangle (3-clique) in the graph
    # We'll iterate through all edges and for each edge (u,v), 
    # we'll check for a common neighbor w, which would form a triangle u-v-w
    
    # To ensure lexicographical order, we'll process nodes in sorted order
    # and also ensure u < v < w
    
    # Convert adjacency lists to sorted lists for consistent iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # Iterate through all edges
    for u, v in sorted(edges):
        if u > v:
            u, v = v, u
        # Now u < v
        # We look for a node w such that w > v and w is connected to both u and v
        # To do this efficiently, we iterate through the neighbors of u and check if they are also neighbors of v
        # and if they are greater than v
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()