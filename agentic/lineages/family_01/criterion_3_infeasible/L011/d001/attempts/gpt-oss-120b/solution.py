import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n                     # bitset of neighbours
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << n) - 1

    for a in range(n):
        # neighbours larger than a
        bits = adj[a] >> (a + 1)
        while bits:
            lsb = bits & -bits
            b = (lsb.bit_length() - 1) + a + 1   # 0‑based index
            bits ^= lsb

            # vertices adjacent to both a and b, and larger than b
            common = adj[a] & adj[b]
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= mask

            if common:
                c = (common & -common).bit_length() - 1
                # output 1‑based indices
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()