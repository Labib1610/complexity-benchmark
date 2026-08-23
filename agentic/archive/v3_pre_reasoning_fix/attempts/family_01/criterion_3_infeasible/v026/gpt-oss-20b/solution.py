import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    bitset = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bitset[u] |= 1 << (v - 1)
        bitset[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (bitset[a] >> (b - 1)) & 1:
                inter = bitset[a] & bitset[b]
                mask = inter >> b  # drop bits <= b-1
                if mask:
                    lsb = mask & -mask
                    offset = lsb.bit_length() - 1
                    c = b + 1 + offset
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()