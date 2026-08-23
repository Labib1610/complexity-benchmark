import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for consistent iteration
    for node in adj:
        adj[node] = sorted(adj[node])
    
    min_trace = float('inf')
    result = None
    
    # Check all combinations of 3 nodes
    # Instead of checking all combinations, we look for triangles in the graph
    # A triangle is a set of 3 nodes where each pair is connected
    
    # To find triangles efficiently, we iterate through all edges and check for common neighbors
    # This is more efficient than checking all triplets
    
    # We'll store edges in a set for fast lookup
    edge_set = set()
    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # Now for each node, check pairs of its neighbors
    for node in sorted(adj.keys()):
        neighbors = adj[node]
        k = len(neighbors)
        for i in range(k):
            for j in range(i+1, k):
                u = neighbors[i]
                v = neighbors[j]
                # Check if u and v are connected (forming a triangle with 'node')
                if u > v:
                    u, v = v, u
                if (u, v) in edge_set:
                    # Found a triangle: u, v, node
                    a, b, c = sorted([u, v, node])
                    trace = a * 10**8 + b * 10**4 + c
                    if trace < min_trace:
                        min_trace = trace
                        result = (a, b, c)
    
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()