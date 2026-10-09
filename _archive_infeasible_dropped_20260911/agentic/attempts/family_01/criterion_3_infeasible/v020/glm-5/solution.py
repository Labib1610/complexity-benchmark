import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    edges.sort()
    for u, v in edges:
        if u > v:
            continue
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        for w in adj[u]:
            if w in adj[v]:
                a, b, c = u, v, w
                if a > b:
                    a, b = b, a
                if b > c:
                    b, c = c, b
                if a > b:
                    a, b = b, a
                print(a, b, c)
                return
    print(-1)

solve()