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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for consistent iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # Iterate through all edges to find a triangle (deadlock triplet)
    found = False
    result = None
    
    # Sort edges to ensure we process in a consistent order
    edges.sort()
    
    for u, v in edges:
        if found:
            break
        # Get common neighbors of u and v
        if len(adj[u]) > len(adj[v]):
            u, v = v, u  # Swap to iterate over the smaller list
        
        for w in adj[u]:
            if w in adj[v]:
                # Found a triangle: u-v, u-w, v-w
                triplet = sorted([u, v, w])
                if not found or triplet < result:
                    result = triplet
                    found = True
                    break
    
    if result:
        print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()