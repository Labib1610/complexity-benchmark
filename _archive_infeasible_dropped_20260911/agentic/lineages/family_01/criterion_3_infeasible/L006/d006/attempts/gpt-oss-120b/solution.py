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
        bits[u] |= 1 << v
        bits[v] |= 1 << u

    for a in range(1, n + 1):
        ba = bits[a]
        for b in range(a + 1, n + 1):
            if not (ba >> b) & 1:          # edge a‑b ?
                continue
            common = (ba & bits[b]) >> (b + 1)
            if common:
                low = common & -common
                c = low.bit_length() - 1 + (b + 1)
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()