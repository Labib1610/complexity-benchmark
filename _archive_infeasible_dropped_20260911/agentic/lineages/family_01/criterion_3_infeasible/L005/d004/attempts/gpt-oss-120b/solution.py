import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset of neighbours, 0‑based indices

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        # neighbours of a that are larger than a
        bits = adj[a] >> (a + 1)
        while bits:
            lsb = bits & -bits
            b_rel = lsb.bit_length() - 1          # position inside shifted bits
            b = a + 1 + b_rel

            # common neighbours of a and b
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = common >> (b + 1)
            if mask:
                lsb2 = mask & -mask
                c_rel = lsb2.bit_length() - 1
                c = b + 1 + c_rel
                # output 1‑based indices
                sys.stdout.write(f"{a+1} {b+1} {c+1}\n")
                return

            # remove processed b
            bits ^= lsb

if __name__ == "__main__":
    solve()