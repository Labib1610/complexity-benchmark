import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = set()
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for deterministic iteration
    for u in range(1, n+1):
        adj[u] = sorted(adj[u])
    
    # Iterate through all triplets (a,b,c) with a < b < c
    # Since we want the lexicographically smallest, iterate in order
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a, b) not in edges:
                continue
            for c in range(b+1, n+1):
                if (a, c) in edges and (b, c) in edges:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()