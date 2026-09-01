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
    
    # Convert edges to a set for O(1) lookup
    edge_set = set(edges)
    
    # We need to find a triangle where all three edges exist
    # That means we need three nodes a < b < c such that (a,b), (a,c), and (b,c) are all edges
    
    # To ensure lexicographical order, we iterate through all pairs (a,b) with a < b
    # and check if there exists a c > b such that (a,c) and (b,c) are also edges
    
    found = False
    result = None
    
    # Create a list of nodes for consistent ordering
    nodes = sorted(adj.keys())
    
    for a in nodes:
        neighbors_a = sorted(list(adj[a]))
        # For each neighbor b of a where b > a
        for b in neighbors_a:
            if b <= a:
                continue
            # Now look for c such that c > b and c is a neighbor of both a and b
            neighbors_b = adj[b]
            # Iterate through neighbors of a that are greater than b
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in neighbors_b:
                    # Found a triangle a-b-c with a < b < c
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()