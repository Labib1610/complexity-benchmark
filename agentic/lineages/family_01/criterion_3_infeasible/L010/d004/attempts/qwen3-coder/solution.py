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
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with finding lexicographically smallest
    edges.sort()
    
    # Create index for quick lookup
    edge_set = set(edges)
    
    # For each edge, look for a third node that forms a triangle
    for i in range(m):
        u, v = edges[i]
        # Check common neighbors of u and v
        for w in adj[u]:
            if w == v:
                continue
            # Check if (v, w) is also an edge
            a, b, c = sorted([u, v, w])
            if (min(v, w), max(v, w)) in edge_set:
                print(a, b, c)
                return

if __name__ == "__main__":
    main()