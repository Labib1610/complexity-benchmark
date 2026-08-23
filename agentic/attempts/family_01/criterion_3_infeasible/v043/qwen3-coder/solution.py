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
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert edges to a set for fast lookup
    edge_set = set(edges)
    
    # We need to find a triangle in the graph, i.e., three nodes a, b, c such that
    # (a,b), (b,c), and (a,c) are all edges.
    
    # To find the lexicographically smallest triangle, we'll iterate through
    # all edges (a,b) with a < b, and for each such edge, we'll look for a node
    # c > b such that (a,c) and (b,c) are also edges.
    
    # Sort adjacency lists to help with ordering
    for u in adj:
        adj[u] = sorted(adj[u])
    
    found = False
    result = None
    
    # Iterate through all edges (a, b) with a < b
    for a in range(1, n+1):
        if a not in adj:
            continue
        for b in adj[a]:
            if b <= a:
                continue
            # Now look for c > b such that both (a,c) and (b,c) exist
            # To optimize, iterate through the neighbors of b that are > b
            for c in adj[b]:
                if c <= b:
                    continue
                # Check if (a, c) is also an edge
                if c in adj[a]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()