import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # We need to find a triangle in the complement graph
    # That means finding three nodes u,v,w such that none of (u,v), (u,w), (v,w) are edges
    # But we want the lexicographically smallest such triple
    
    # Instead, we can think of it as: find three nodes that form a triangle in the original graph
    # No, wait. The problem says that any two in the subset cannot share enclosure.
    # So for a subset {a,b,c}, all three pairs (a,b), (a,c), (b,c) must be in the forbidden list.
    # That means we're looking for a triangle in the original graph.
    
    # Let's re-read:
    # "a subset of exactly three species that inherently requires at least three enclosures"
    # "the veterinary list explicitly forbids sharing an enclosure for every possible pair"
    # So for species a,b,c, all pairs (a,b), (a,c), (b,c) must be forbidden.
    # I.e., we're looking for a triangle in the forbidden graph.
    
    # Create a set of edges for fast lookup
    edge_set = set()
    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # We want the lexicographically smallest triangle
    # Try all triples (i,j,k) with i<j<k in lexicographical order
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if (i, j) not in edge_set:
                continue
            for k in range(j+1, n+1):
                if (i, k) in edge_set and (j, k) in edge_set:
                    print(i, j, k)
                    return

if __name__ == "__main__":
    main()