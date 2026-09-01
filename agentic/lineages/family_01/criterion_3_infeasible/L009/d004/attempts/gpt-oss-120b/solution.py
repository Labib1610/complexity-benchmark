import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    mask = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        mask[u] |= 1 << v
        mask[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for a in range(1, n - 1):
        # keep neighbours sorted for lexicographic order
        neigh = sorted(v for v in adj[a] if v > a)
        for b in neigh:
            common = mask[a] & mask[b]
            # discard vertices <= b
            shifted = common >> (b + 1)
            if shifted:
                low = shifted & -shifted          # lowest set bit
                c = (low.bit_length() - 1) + (b + 1)
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()