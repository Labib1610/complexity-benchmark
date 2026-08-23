import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list and edge set for O(1) lookup
    adj = defaultdict(set)
    edge_set = set()
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edge_set.add((u, v))
    
    # Convert adjacency lists to sorted lists for consistent iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    best = None
    min_score = float('inf')
    
    # Iterate through all nodes
    for a in range(1, n+1):
        if a not in adj:
            continue
        # For each neighbor b of a where b > a
        for b in adj[a]:
            if b <= a:
                continue
            # For each neighbor c of a where c > b
            for c in adj[a]:
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    # Found a triangle (a,b,c)
                    score = a * (10**8) + b * (10**4) + c
                    if score < min_score:
                        min_score = score
                        best = (a, b, c)
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()