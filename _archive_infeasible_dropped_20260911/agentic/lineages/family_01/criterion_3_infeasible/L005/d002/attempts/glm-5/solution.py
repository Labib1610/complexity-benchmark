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
    
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[a]:
                if c <= b:
                    continue
                if c in adj[b]:
                    print(a, b, c)
                    return
    
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[a]:
                if c <= b:
                    continue
                if c not in adj[b]:
                    print(a, b, c)
                    return

solve()