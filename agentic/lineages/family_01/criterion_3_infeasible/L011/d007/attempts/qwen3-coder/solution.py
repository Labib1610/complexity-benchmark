import sys
from itertools import combinations

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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Build edge set for O(1) lookup
    edge_set = set(edges)
    
    # Generate all triangles (3-cliques) by checking all combinations of 3 nodes
    # But more efficiently: for each edge, check its neighbors
    triangles = []
    for i in range(1, n + 1):
        neighbors = list(adj[i])
        for j in range(len(neighbors)):
            for k in range(j + 1, len(neighbors)):
                u, v = neighbors[j], neighbors[k]
                if v in adj[u]:
                    # Found triangle i, u, v
                    a, b, c = sorted([i, u, v])
                    triangles.append((a, b, c))
    
    # Remove duplicates by converting to set
    triangles = list(set(triangles))
    triangles.sort()
    
    # For each triangle, count relaxed states
    for a, b, c in triangles:
        # Count how many edges among a,b,c
        e_ab = 1 if b in adj[a] else 0
        e_ac = 1 if c in adj[a] else 0
        e_bc = 1 if c in adj[b] else 0
        edge_count = e_ab + e_ac + e_bc
        
        # Now, for each of the 27 assignments, compute tension
        relaxed_count = 0
        for x in range(1, 4):
            for y in range(1, 4):
                for z in range(1, 4):
                    tension = 0
                    if e_ab:
                        tension += abs(x - y)
                    if e_ac:
                        tension += abs(x - z)
                    if e_bc:
                        tension += abs(y - z)
                    if tension == 2:
                        relaxed_count += 1
        if relaxed_count == 12:
            print(a, b, c)
            return

if __name__ == "__main__":
    main()