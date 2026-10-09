import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        adj_a = adj[a]
        if len(adj_a) < 2:
            continue
        
        if best is not None:
            min_b = best[1]
            candidates = [b for b in adj_a if b > a and b >= min_b]
        else:
            candidates = [b for b in adj_a if b > a]
        
        candidates.sort()
        
        for b in candidates:
            if best is not None and b >= best[1]:
                break
            adj_b = adj[b]
            for c in adj_a:
                if c > b and c in adj_b:
                    best = (a, b, c)
                    break
            if best is not None and best[0] == a and best[1] == b:
                break
        
        if best is not None and best[0] == a:
            break
    
    print(best[0], best[1], best[2])

solve()