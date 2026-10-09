import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
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
    
    # Sort edges to help with ordering
    edge_set = set(edges)
    
    # We want the lexicographically smallest triplet (a,b,c) with a<b<c and all three edges present
    # That means we look for triangles in the graph
    
    # For each node, sort its neighbors and check for triangles
    for a in range(1, n+1):
        neighbors = sorted(list(adj[a]))
        # Check all pairs of neighbors of a
        for i in range(len(neighbors)):
            b = neighbors[i]
            if b <= a:
                continue
            for j in range(i+1, len(neighbors)):
                c = neighbors[j]
                if c <= b:
                    continue
                # Now check if b and c are connected
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()