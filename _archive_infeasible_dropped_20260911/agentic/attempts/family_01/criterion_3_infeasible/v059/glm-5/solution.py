import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    
    for u, v in edges:
        au = adj[u]
        av = adj[v]
        if len(au) > len(av):
            au, av = av, au
        for w in au:
            if w in av:
                a, b, c = u, v, w
                if a > b:
                    a, b = b, a
                if b > c:
                    b, c = c, b
                    if a > b:
                        a, b = b, a
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
    
    print(best[0], best[1], best[2])

solve()