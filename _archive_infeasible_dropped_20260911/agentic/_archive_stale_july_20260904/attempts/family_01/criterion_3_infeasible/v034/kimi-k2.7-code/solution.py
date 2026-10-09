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
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)
    for i in range(n):
        neigh[i].sort()
    full = (1 << n) - 1
    high = [0] * n
    for i in range(n):
        high[i] = full ^ ((1 << (i + 1)) - 1)
    out = sys.stdout
    for a in range(n):
        row_a = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = row_a & adj[b] & high[b]
            if common:
                c = (common & -common).bit_length() - 1
                out.write(f"{a + 1} {b + 1} {c + 1}\n")
                return

if __name__ == "__main__":
    solve()