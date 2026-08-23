import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration order
    adj_lists = [sorted(s) for s in adj]
    
    best = None
    
    for a in range(1, n + 1):
        # Early termination: if best is found and a >= best[0], no need to continue
        if best is not None and a >= best[0]:
            break
            
        neighbors_a = adj_lists[a]
        
        # Try to find b and c such that a < b < c and (a,b), (a,c), (b,c) are edges
        # Iterate through pairs of neighbors of a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            if best is not None and b >= best[1]:
                break
                
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c <= b:
                    continue
                if best is not None and c >= best[2]:
                    continue
                
                # Check if b and c are connected
                if c in adj[b]:
                    best = (a, b, c)
                    # Since we iterate in sorted order, this is the best for current a
                    # Break inner loops to try next a
                    break
            if best is not None and best[0] == a and best[1] == b:
                break
    
    print(f"{best[0]} {best[1]} {best[2]}")

if __name__ == "__main__":
    solve()