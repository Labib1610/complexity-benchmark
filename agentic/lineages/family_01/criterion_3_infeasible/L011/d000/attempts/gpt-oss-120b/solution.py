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
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    edges.sort()                # lexicographic order

    for a, b in edges:
        common = adj[a] & adj[b]
        cand = common >> b       # keep only vertices > b
        if cand:
            lsb = cand & -cand
            offset = lsb.bit_length() - 1
            c = b + offset + 1
            # a < b < c holds automatically
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()