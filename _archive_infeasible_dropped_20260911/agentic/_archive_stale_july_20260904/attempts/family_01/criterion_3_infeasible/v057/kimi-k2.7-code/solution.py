import sys
import bisect

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
    for i in range(n):
        neigh[i].sort()
    suffix = [(-1 << (i + 1)) for i in range(n)]
    out = sys.stdout
    for a in range(n):
        nb = neigh[a]
        idx = bisect.bisect_right(nb, a)
        for j in range(idx, len(nb)):
            b = nb[j]
            t = adj[a] & adj[b] & suffix[b]
            if t:
                c = (t & -t).bit_length() - 1
                out.write(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == "__main__":
    solve()