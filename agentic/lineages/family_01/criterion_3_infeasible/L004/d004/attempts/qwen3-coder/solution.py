import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = set()
    adj = [[] for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to find a triangle in the complement graph.
    # That is, three nodes such that none of the three edges between them exist in the original graph.
    # But actually, we want three nodes such that ALL three edges exist in the original graph.
    # Because if all three edges exist, then no matter how you color the three nodes with two colors,
    # at least two nodes will have the same color, and that edge will cause a conflict.
    
    # So we need to find a triangle in the original graph.
    
    # Let's iterate through all combinations of 3 nodes and check if all three edges exist.
    # To optimize, let's build adjacency sets.
    adj_set = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for neighbor in adj[i]:
            adj_set[i].add(neighbor)
    
    best = None
    
    # Instead of checking all combinations, let's check triangles more efficiently.
    # For each edge (u,v), check for a common neighbor w.
    for u in range(1, n + 1):
        for v in adj_set[u]:
            if v <= u:
                continue
            # Check for common neighbors of u and v that are > v to avoid duplicates
            for w in adj_set[u]:
                if w <= v:
                    continue
                if w in adj_set[v]:
                    candidate = tuple(sorted([u, v, w]))
                    if best is None or candidate < best:
                        best = candidate
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()