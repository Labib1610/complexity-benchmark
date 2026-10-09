import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    bits = [0] * (n + 1)          # 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bits[u] |= 1 << (v - 1)
        bits[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        bits_a = bits[a]
        for b in range(a + 1, n):
            # edge a‑b must exist
            if not ((bits_a >> (b - 1)) & 1):
                continue
            common = bits_a & bits[b]
            # keep only vertices > b
            mask = common >> b
            if mask:
                low = mask & -mask               # lowest set bit
                c = b + low.bit_length() - 1
                # output in ascending order (already a<b<c)
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()