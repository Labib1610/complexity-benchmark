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
        if u == v:
            continue
        if u > v:
            u, v = v, u
        # set bits
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edges.append((u, v))

    edges.sort()                 # lexicographic order

    for a, b in edges:
        common = adj[a] & adj[b]          # vertices adjacent to both
        # keep only vertices > b
        tmp = common >> b                  # drop bits 0..b-1 (indices)
        if tmp:
            # isolate lowest set bit
            lsb = tmp & -tmp
            pos = lsb.bit_length() - 1    # position inside tmp
            c = b + 1 + pos                # real vertex number
            # output
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()