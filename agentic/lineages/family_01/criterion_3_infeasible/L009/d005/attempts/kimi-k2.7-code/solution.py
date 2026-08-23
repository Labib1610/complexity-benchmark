import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for lst in neigh:
        lst.sort()

    all_mask = (1 << n) - 1
    suffix = [0] * n
    for b in range(n):
        suffix[b] = all_mask ^ ((1 << (b + 1)) - 1)

    for a in range(n):
        amask = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = amask & adj[b] & suffix[b]
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}")
                return

solve()