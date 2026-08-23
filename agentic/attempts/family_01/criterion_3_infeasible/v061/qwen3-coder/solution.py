import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    edge_set = set()
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with lexicographical order
    edges.sort()
    
    # For each edge (u,v), look for a node w such that (u,w) and (v,w) also exist
    found = False
    best = (n, n, n)  # placeholder for lexicographically smallest triplet
    
    # We'll iterate through all edges and try to find a triangle
    for u in range(1, n+1):
        if found:
            break
        neighbors = list(adj[u])
        neighbors.sort()
        for i in range(len(neighbors)):
            if found:
                break
            v = neighbors[i]
            if v <= u:
                continue
            for j in range(i+1, len(neighbors)):
                w = neighbors[j]
                if w <= v:
                    continue
                # Check if v and w are connected
                if (v, w) in edge_set or (w, v) in edge_set:
                    triplet = tuple(sorted([u, v, w]))
                    if triplet < best:
                        best = triplet
                        found = True
                        break
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()