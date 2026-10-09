import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    bits = [0] * (n + 1)          # adjacency bitsets
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits (0‑based inside the integer)
        bits[u] |= 1 << (v - 1)
        bits[v] |= 1 << (u - 1)
        adj[u].append(v)
        adj[v].append(u)

    for v in range(1, n + 1):
        adj[v].sort()

    out = []
    for a in range(1, n + 1):
        ba = bits[a]
        for b in adj[a]:
            if b <= a:
                continue            # need a < b
            common = ba & bits[b]   # N(a) ∩ N(b)
            shifted = common >> b   # discard vertices ≤ b
            if shifted:
                # index of least significant 1‑bit
                low = (shifted & -shifted).bit_length() - 1
                c = low + b + 1     # back to original vertex number
                out = [a, b, c]
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()