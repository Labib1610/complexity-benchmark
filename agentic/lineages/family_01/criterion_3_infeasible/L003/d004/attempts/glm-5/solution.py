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
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)

    best = None
    for a in range(1, n - 1):
        if best is not None and a >= best[0]:
            break
        adj_a = adj[a]
        if len(adj_a) < 2:
            continue
        sorted_b = sorted(adj_a)
        for b in sorted_b:
            if best is not None and (a > best[0] or (a == best[0] and b >= best[1])):
                break
            if b <= a:
                continue
            adj_b = adj[b]
            for c in sorted_b:
                if c <= b:
                    continue
                if best is not None and (a > best[0] or (a == best[0] and b > best[1]) or (a == best[0] and b == best[1] and c >= best[2])):
                    break
                if c in adj_b:
                    best = (a, b, c)
                    break

    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}")

solve()