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
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)
    for i in range(1, n + 1):
        neigh[i].sort()
    for a in range(1, n + 1):
        ma = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            mask = ma & adj[b]
            t = mask >> b
            if t:
                c = b + (t & -t).bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()