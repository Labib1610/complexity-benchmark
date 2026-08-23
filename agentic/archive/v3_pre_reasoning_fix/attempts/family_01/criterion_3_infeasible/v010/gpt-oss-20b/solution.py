import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adjacency_bits = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adjacency_bits[u] |= 1 << (v - 1)
        adjacency_bits[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        bits_a = adjacency_bits[a]
        tmp = bits_a
        while tmp:
            lsb = tmp & -tmp
            b_idx = lsb.bit_length() - 1  # 0‑based index
            b = b_idx + 1
            if b > a:
                common = bits_a & adjacency_bits[b]
                shifted = common >> b
                if shifted:
                    lsb_c = shifted & -shifted
                    c_idx = lsb_c.bit_length() - 1
                    c = b + c_idx + 1
                    print(a, b, c)
                    return
            tmp -= lsb

if __name__ == "__main__":
    solve()