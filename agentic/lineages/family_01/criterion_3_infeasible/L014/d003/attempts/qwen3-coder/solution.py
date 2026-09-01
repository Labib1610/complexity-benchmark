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
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
    
    # Sort edges to help with finding the lexicographically smallest triangle
    edges.sort()
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We want to find the lexicographically smallest triangle
    # Iterate through all combinations of 3 nodes in increasing order
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b not in adj[a]:
                continue
            for c in range(b + 1, n + 1):
                if c not in adj[a]:
                    continue
                if c not in adj[b]:
                    continue
                # Found a triangle (a,b,c)
                print(a, b, c)
                return

if __name__ == "__main__":
    main()