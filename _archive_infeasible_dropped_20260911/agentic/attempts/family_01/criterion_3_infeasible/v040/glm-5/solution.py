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
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        la = adj[a]
        if len(la) < 2:
            continue
        sorted_la = sorted(la)
        for i in range(len(sorted_la)):
            b = sorted_la[i]
            if best is not None and b >= best[1]:
                break
            lb = adj[b]
            for j in range(i + 1, len(sorted_la)):
                c = sorted_la[j]
                if c in lb:
                    if best is None or (a, b, c) < best:
                        best = (a, b, c)
                        break
            if best is not None and best[0] == a and best[1] == b:
                break
        if best is not None and best[0] == a:
            break

    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()