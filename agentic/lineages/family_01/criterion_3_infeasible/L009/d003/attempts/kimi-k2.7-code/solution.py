import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)
    for i in range(1, n + 1):
        neigh[i].sort()
    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            common >>= b
            if common:
                offset = (common & -common).bit_length() - 1
                c = b + offset + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()