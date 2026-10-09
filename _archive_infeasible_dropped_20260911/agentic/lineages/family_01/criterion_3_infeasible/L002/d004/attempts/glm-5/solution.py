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
    
    # Convert to sorted lists for ordered iteration
    adj_list = [sorted(s) for s in adj]
    
    best = None
    
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # Pruning: if best is found and a >= best[0], we can stop
        # because any subsequent triad will have first element >= best[0]
        if best is not None and a >= best[0]:
            break
        
        neighbors_a = adj_list[a]
        # Iterate b in neighbors of a where b > a
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Pruning: if best exists and (a, b) is already lexicographically >= best
            if best is not None:
                if a > best[0]:
                    continue
                if a == best[0] and b >= best[1]:
                    continue
            
            # Iterate c in neighbors of b where c > b
            neighbors_b = adj_list[b]
            for c in neighbors_b:
                if c <= b:
                    continue
                
                # Pruning: if best exists and (a, b, c) >= best
                if best is not None:
                    if a > best[0]:
                        continue
                    if a == best[0] and b > best[1]:
                        continue
                    if a == best[0] and b == best[1] and c >= best[2]:
                        continue
                
                # Check if c is connected to a
                if c in adj[a]:
                    best = (a, b, c)
                    # Since we iterate in order, this is the best for current (a, b)
                    # We can break to move to next b
                    break
    
    if best:
        print(f"{best[0]} {best[1]} {best[2]}")

if __name__ == "__main__":
    solve()