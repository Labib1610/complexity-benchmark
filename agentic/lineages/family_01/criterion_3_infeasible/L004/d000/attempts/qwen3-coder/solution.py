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
    
    # For each node, sort its neighbors for consistent ordering
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    # We want the lexicographically smallest triangle
    # So we iterate through all edges and for each edge (u,v), we look for a node w
    # such that w is connected to both u and v, and u < v < w
    
    # To make it efficient, for each edge (u,v), we only consider nodes w > max(u,v)
    # and w in both adj[u] and adj[v]
    
    # Let's sort edges to process them in order that might help find lex smallest early
    edges.sort()
    
    best = None
    
    for u, v in edges:
        if u >= v:
            continue
        # Find common neighbors of u and v that are greater than both u and v
        # Since adj[u] and adj[v] are sorted, we can use two pointers or just iterate
        # But since we need w > max(u,v), let's iterate through the larger list
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        # Now adj[u] is the smaller list
        for w in adj[u]:
            if w <= v:
                continue
            if w in adj[v]:
                candidate = (u, v, w)
                if best is None or candidate < best:
                    best = candidate
                    break  # Since we want the first (lex smallest), and edges are sorted
        if best:
            # We could break outer loop too, but let's just finish
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()