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
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, sort its neighbors for consistent iteration
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    # Iterate through all edges to find triangles
    found = False
    result = None
    
    # Sort edges to process in order that helps with lexicographical ordering
    edges.sort()
    
    for u, v in edges:
        if found:
            break
        # Find common neighbors of u and v
        # Iterate through the smaller adjacency list for efficiency
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        
        for w in adj[u]:
            if w > v:  # To ensure a < b < c
                if w in adj[v]:
                    # Found triangle u, v, w
                    a, b, c = sorted([u, v, w])
                    if not found or (a, b, c) < result:
                        result = (a, b, c)
                        found = True
                        break
        if not found:
            # Continue searching for better triangles
            if len(adj[u]) > len(adj[v]):
                u, v = v, u
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    triple = tuple(sorted([u, v, w]))
                    if result is None or triple < result:
                        result = triple
    
    if result is None:
        # Fallback: brute-force search for small graphs or if above misses
        for a in range(1, n + 1):
            if found:
                break
            for b in adj[a]:
                if b <= a:
                    continue
                for c in adj[a]:
                    if c <= b:
                        continue
                    if c in adj[b]:
                        result = (a, b, c)
                        found = True
                        break
                if found:
                    break
    
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()