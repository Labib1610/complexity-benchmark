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
    
    # We need to find a triangle (cycle of length 3) in the graph
    # Iterate through all edges and check for a common neighbor
    
    # Sort edges to help with finding lexicographically smallest
    edges.sort()
    
    best = None
    
    for u, v in edges:
        # Find common neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        common = neighbors_u & neighbors_v
        
        candidates = []
        for w in common:
            # Ensure all are distinct and form a triangle
            triple = tuple(sorted([u, v, w]))
            candidates.append(triple)
        
        # Sort candidates to find the lexicographically smallest
        candidates.sort()
        
        if candidates:
            candidate = candidates[0]
            if best is None or candidate < best:
                best = candidate
    
    # Since we're guaranteed a solution exists, best will not be None
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()