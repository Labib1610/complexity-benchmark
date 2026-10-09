import sys

def solve():
    data = sys.stdin.buffer.read().split()
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
    for a in range(1, n + 1):
        la = adj[a]
        if len(la) < 2:
            continue
        for b in la:
            if b <= a:
                continue
            lb = adj[b]
            common = la & lb
            for c in common:
                if c > b:
                    print(a, b, c)
                    return
    # guaranteed to exist
    print(-1, -1, -1)

solve()