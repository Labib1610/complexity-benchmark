import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Store edges in an adjacency list and a set for O(1) lookups
    adj = [set() for _ in range(n + 1)]
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        if u > v:
            u, v = v, u
        
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to help find the lexicographically smallest triple.
    # A triple (a, b, c) with a < b < c exists if (a, b) is an edge, 
    # (a, c) is an edge, and (b, c) is an edge.
    # To minimize (a, b, c) lexicographically:
    # 1. Iterate through a from 1 to n-2
    # 2. Iterate through b in sorted order of neighbors of a such that b > a
    # 3. Check if there exists c such that c > b and c is in adj[a] and adj[b]
    
    for a in range(1, n + 1):
        neighbors_a = sorted([v for v in adj[a] if v > a])
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now find the smallest c > b such that c is in both adj[a] and adj[b]
            # Intersection of adj[a] and adj[b]
            candidates = sorted(list(adj[a].intersection(adj[b])))
            for c in candidates:
                if c > b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()