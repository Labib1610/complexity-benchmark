import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        if u < v:
            edges[u].append(v)
        else:
            edges[v].append(u)
    for a in range(n):
        edges[a].sort()
        for b in edges[a]:
            mask = adj[a] & adj[b] & ~((1 << (b + 1)) - 1)
            if mask:
                c = (mask & -mask).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}\n")
                return

solve()