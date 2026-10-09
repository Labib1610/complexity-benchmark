import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edges.append((u, v))
        # set bits (0‑based)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    edges.sort()                # lexicographic order of (a,b)

    for a, b in edges:
        common = adj[a] & adj[b]
        # keep only vertices > b
        mask = common >> b
        if mask:
            lsb = mask & -mask
            idx = lsb.bit_length() - 1   # position after shift
            c = b + idx + 1
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()