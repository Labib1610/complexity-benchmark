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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with lexicographical order
    edges.sort()
    
    # For each edge (a,b), look for a common neighbor c
    for a, b in edges:
        # We want a < b < c, so we look for c in adj[a] and adj[b] such that c > b
        for c in adj[a]:
            if c > b and c in adj[b]:
                print(a, b, c)
                return

if __name__ == "__main__":
    main()