import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n - 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            common &= ~((1 << (b + 1)) - 1)
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

solve()