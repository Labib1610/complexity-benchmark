import sys
from collections import defaultdict

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
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We'll iterate through all combinations (a,b,c) with a < b < c
    # To optimize, we can sort the adjacency lists and use pointers
    
    # First, sort adjacency list for consistent iteration
    for i in range(1, n+1):
        adj[i] = sorted(adj[i])
    
    # Try all triplets (a,b,c) in lexicographical order
    for a in range(1, n-1):
        for b in range(a+1, n):
            if b not in adj[a]:
                continue
            for c in range(b+1, n+1):
                if c not in adj[a]:
                    continue
                if c not in adj[b]:
                    continue
                # Found a triangle: a-b, a-c, b-c
                print(a, b, c)
                return

if __name__ == "__main__":
    main()