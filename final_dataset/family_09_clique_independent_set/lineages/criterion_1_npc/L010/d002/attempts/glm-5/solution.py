import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    if k == 0:
        print("YES")
        print()
        return
    
    # Greedy: repeatedly pick the vertex with minimum degree in the remaining graph
    remaining = (1 << (n + 1)) - 2  # bits 1..n set
    chosen = []
    
    for _ in range(k):
        best_v = -1
        best_deg = n + 1
        for v in range(1, n + 1):
            if remaining & (1 << v):
                deg = bin(adj[v] & remaining).count('1')
                if deg < best_deg:
                    best_deg = deg
                    best_v = v
                    if deg == 0:
                        break
        
        if best_v == -1:
            print("NO")
            return
        
        chosen.append(best_v)
        remaining &= ~(1 << best_v)
        remaining &= ~adj[best_v]
    
    print("YES")
    print(' '.join(map(str, chosen)))

solve()