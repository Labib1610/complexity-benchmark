import sys
from collections import defaultdict

def find_triangle(edges, neighbors):
    # For each node, check its neighbors
    for u in sorted(neighbors.keys()):
        # Get neighbors of u
        neigh_u = set(neighbors[u])
        # Check pairs of neighbors of u
        sorted_neigh_u = sorted(neighbors[u])
        for i in range(len(sorted_neigh_u)):
            v = sorted_neigh_u[i]
            if v <= u:
                continue
            for w in sorted_neigh_u[i+1:]:
                if w <= v:
                    continue
                # Check if v and w are connected
                if v in neighbors and w in neighbors[v]:
                    return (u, v, w)
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    
    edges = []
    neighbors = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        edges.append((u, v))
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # Convert sets to lists for consistent iteration
    for key in neighbors:
        neighbors[key] = list(neighbors[key])
        
    result = find_triangle(edges, neighbors)
    if result:
        print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()