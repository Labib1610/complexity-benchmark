import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list using sets for fast lookup
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        index += 2
    
    # We need to find a triangle: three nodes a-b, a-c, b-c
    # Iterate through all edges and check for a common neighbor
    found = False
    # To get lexicographically smallest, we should iterate through edges in order
    # But since we read them in arbitrary order, we'll sort them first
    edges.sort()
    
    for u, v in edges:
        if found:
            break
        # Check for a common neighbor
        common_neighbors = adj[u] & adj[v]
        for w in sorted(common_neighbors):
            if found:
                break
            # Ensure we output a < b < c
            a, b, c = sorted([u, v, w])
            print(a, b, c)
            found = True
            break

if __name__ == "__main__":
    main()