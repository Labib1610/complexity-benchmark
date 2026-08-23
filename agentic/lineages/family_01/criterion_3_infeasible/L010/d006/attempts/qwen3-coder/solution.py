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
        u, v = min(u, v), max(u, v)
        edges.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert adjacency lists to sorted lists for deterministic iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # Iterate through all possible triplets (a, b, c) with a < b < c
    for a in range(1, n+1):
        if a not in adj:
            continue
        for i, b in enumerate(adj[a]):
            if b <= a:
                continue
            for c in adj[a]:
                if c <= b:
                    continue
                # Check if all three edges exist: (a,b), (a,c), (b,c)
                if (b, c) in edges:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()