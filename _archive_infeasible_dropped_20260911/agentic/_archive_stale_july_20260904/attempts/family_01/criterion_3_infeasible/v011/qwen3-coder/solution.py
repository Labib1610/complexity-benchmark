import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (three nodes all connected to each other)
    # We'll iterate through all edges and for each edge (u,v), we look for a node w
    # such that (u,w) and (v,w) are also edges.
    # To make it efficient, for each edge (u,v), we check nodes w such that w > max(u,v)
    # This helps in getting the lexicographically smallest triple.
    
    # Let's store edges in a set for fast lookup
    edge_set = set()
    for u, v in edges:
        edge_set.add((u, v))
        edge_set.add((v, u))
    
    # Now, for each node u, sort its neighbors
    neighbors = [sorted(list(adj[i])) for i in range(n)]
    
    found = False
    for u in range(n):
        if found:
            break
        for idx in range(len(neighbors[u])):
            v = neighbors[u][idx]
            if v <= u:
                continue
            # Now look for w in neighbors[v] such that w > v and (u,w) exists
            for k in range(idx+1, len(neighbors[u])):
                w = neighbors[u][k]
                if w <= v:
                    continue
                if w in adj[v]:
                    # Found triangle u < v < w
                    print(u+1, v+1, w+1)
                    found = True
                    break
            if found:
                break

if __name__ == "__main__":
    main()