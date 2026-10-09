import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    adj = [0]*(n+1)
    idx = 3
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    if k == 0:
        print("YES")
        print()
        return
    
    # Greedy: repeatedly pick the vertex with minimum degree in the remaining graph
    remaining = (1 << (n+1)) - 2  # bits 1..n set
    chosen = []
    for _ in range(k):
        best = -1
        best_deg = n+1
        best_remaining = 0
        r = remaining
        while r:
            v = (r & -r).bit_length() - 1
            r &= r - 1
            cnt = bin(adj[v] & remaining).count('1')
            if cnt < best_deg:
                best_deg = cnt
                best = v
                best_remaining = remaining & ~adj[v] & ~(1 << v)
        if best == -1:
            print("NO")
            return
        chosen.append(best)
        remaining = best_remaining
    
    print("YES")
    print(' '.join(map(str, chosen)))

solve()