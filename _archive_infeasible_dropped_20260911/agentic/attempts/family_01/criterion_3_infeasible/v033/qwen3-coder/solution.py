import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Create adjacency list as sets for fast lookup
    # We need to find a triangle in the graph
    
    # Iterate through all edges
    for u, v in edges:
        # For each edge, check for a common neighbor
        if u > v:
            u, v = v, u
        # Check neighbors of u
        for w in adj[u]:
            if w != v and w > v:
                # Check if v is also connected to w
                if w in adj[v]:
                    # Found a triangle: u, v, w
                    result = sorted([u, v, w])
                    print(result[0], result[1], result[2])
                    return

if __name__ == "__main__":
    main()