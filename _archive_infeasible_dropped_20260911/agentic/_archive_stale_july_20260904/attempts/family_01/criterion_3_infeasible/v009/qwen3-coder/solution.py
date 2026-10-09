import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list representation of the graph
    adj = defaultdict(set)
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices by their ID to ensure we check in lexicographical order
    vertices = list(range(1, n+1))
    
    # For each vertex a, check its neighbors b and c to see if there's an edge between b and c
    for a in vertices:
        neighbors = sorted(list(adj[a]))
        # Check all pairs of neighbors of a
        for i in range(len(neighbors)):
            b = neighbors[i]
            for j in range(i+1, len(neighbors)):
                c = neighbors[j]
                # If b and c are connected, we found our triangle
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()