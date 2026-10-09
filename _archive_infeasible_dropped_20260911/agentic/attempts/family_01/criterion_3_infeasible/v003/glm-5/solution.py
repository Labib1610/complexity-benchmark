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
        adj_a = adj[a]
        if len(adj_a) < 2:
            continue
        for b in adj_a:
            if b < a:
                continue
            adj_b = adj[b]
            for c in adj_a:
                if c <= b:
                    continue
                if c in adj_b:
                    print(a, b, c)
                    return

solve()