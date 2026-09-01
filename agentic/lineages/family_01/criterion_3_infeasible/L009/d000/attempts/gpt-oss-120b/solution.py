import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)                # bitsets, 1‑based
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for v in range(1, n + 1):
        neigh[v].sort()

    for a in range(1, n - 1):
        for b in neigh[a]:
            if b <= a:
                continue
            # vertices adjacent to both a and b
            common = adj[a] & adj[b]
            # keep only vertices > b
            t = common >> (b + 1)
            if t:
                low = (t & -t).bit_length() - 1   # position of least set bit
                c = b + 1 + low
                # a<b<c holds automatically
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()