import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    edge_set = set()
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort edges for consistent processing
    edges.sort()
    
    # We need to find a triangle (three nodes a,b,c) such that all three edges (a,b), (b,c), (a,c) exist
    # This ensures each node appears exactly twice (even count)
    
    # To find the lexicographically smallest triangle:
    # Iterate through all combinations of 3 nodes, check if they form a triangle, and keep the smallest
    
    # However, iterating through all combinations of nodes is O(n^3) which might be too slow for n=2000
    # Instead, iterate through each edge and for each edge (u,v), look for a common neighbor
    
    best = None
    
    # For each edge, check its endpoints' neighbors for a common node
    for u, v in edges:
        # Get neighbors of u and v
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        
        # Find common neighbors
        common = neighbors_u & neighbors_v
        
        for w in common:
            # We have a triangle u-v-w
            # Ensure all edges exist (they should since w is a common neighbor)
            # But we need to make sure we have the right ordering
            a, b, c = sorted([u, v, w])
            if (a, b) in edge_set and (b, c) in edge_set and (a, c) in edge_set:
                candidate = (a, b, c)
                if best is None or candidate < best:
                    best = candidate
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()