import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (a,b,c) such that each pair is connected (i.e., each pair is in conflict)
    # That means we want a triangle in the graph: a-b, b-c, a-c all exist
    # And we want the lexicographically smallest such triple
    
    # To do this efficiently, we can iterate through all edges and for each edge (u,v),
    # look for a common neighbor w such that u-v-w forms a triangle
    # To maintain order and ensure lexicographical minimality, we sort the edges appropriately
    
    # First, let's sort the adjacency lists so we process neighbors in order
    for i in range(1, n+1):
        adj[i] = sorted(adj[i])
    
    best = None
    
    # For each node u, check all pairs of its neighbors (v, w) where v < w
    # If v and w are also connected, then (u,v,w) forms a triangle
    # We want the lexicographically smallest such triple
    for u in range(1, n+1):
        neighbors = adj[u]
        # For each pair of neighbors of u
        for i in range(len(neighbors)):
            v = neighbors[i]
            if v <= u:
                continue
            for j in range(i+1, len(neighbors)):
                w = neighbors[j]
                if w <= u:
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    candidate = tuple(sorted([u, v, w]))
                    if best is None or candidate < best:
                        best = candidate
    
    if best:
        print(best[0], best[1], best[2])
    else:
        # Should not happen according to problem statement
        pass

if __name__ == "__main__":
    main()