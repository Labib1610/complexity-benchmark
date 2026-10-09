import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = [set() for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), check for a common neighbor w such that u-v-w forms a triangle
    for u, v in edges:
        if u >= v:
            continue
        # Check intersection of neighbors of u and v
        neighbors_u = graph[u]
        neighbors_v = graph[v]
        
        # Iterate through the smaller set for efficiency
        if len(neighbors_u) > len(neighbors_v):
            neighbors_u, neighbors_v = neighbors_v, neighbors_u
            
        for w in neighbors_u:
            if w in neighbors_v:
                # Found a triangle: u, v, w
                # Ensure they are distinct and u < v < w
                trio = sorted([u, v, w])
                if trio[0] < trio[1] < trio[2]:
                    print(trio[0], trio[1], trio[2])
                    return

if __name__ == "__main__":
    main()