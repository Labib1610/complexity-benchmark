import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    bits = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        bits[u] |= 1 << v
        bits[v] |= 1 << u
    
    for i in range(1, n + 1):
        adj[i].sort()
    
    for a in range(1, n + 1):
        na = adj[a]
        k = len(na)
        for i in range(k):
            b = na[i]
            if b <= a:
                continue
            for j in range(i + 1, k):
                c = na[j]
                if bits[b] & (1 << c):
                    print(a, b, c)
                    return

solve()