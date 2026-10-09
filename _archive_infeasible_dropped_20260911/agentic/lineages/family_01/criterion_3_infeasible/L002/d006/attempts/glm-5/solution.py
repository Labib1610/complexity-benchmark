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

    best = None

    for u in range(1, n + 1):
        if best is not None and u >= best[0]:
            break
        neighbors = sorted(adj[u])
        for v in neighbors:
            if v <= u:
                continue
            if best is not None:
                if u > best[0]:
                    continue
                if u == best[0] and v >= best[1]:
                    continue
            for w in neighbors:
                if w <= v:
                    continue
                if w in adj[v]:
                    cand = (u, v, w)
                    if best is None or cand < best:
                        best = cand
                        break

    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()