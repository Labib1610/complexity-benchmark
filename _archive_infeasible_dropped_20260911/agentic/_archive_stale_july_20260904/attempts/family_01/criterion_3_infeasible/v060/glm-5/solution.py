import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)

    best = None

    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        neighbors_a = adj[a]
        if len(neighbors_a) < 2:
            continue
        sorted_neighbors = sorted(neighbors_a)
        limit_b = best[1] if best is not None else n + 1
        for i in range(len(sorted_neighbors)):
            b = sorted_neighbors[i]
            if b <= a:
                continue
            if best is not None and b >= limit_b:
                break
            common = adj[b] & neighbors_a
            if not common:
                continue
            c = min(common)
            if c > b:
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
                    limit_b = best[1]

    if best is not None:
        sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()