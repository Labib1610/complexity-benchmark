import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_above_a = (-1) << a  # keep bits for nodes > a
        bits_above = adj[a] & mask_above_a
        while bits_above:
            b_bit = bits_above & -bits_above
            b = (b_bit.bit_length() - 1) + 1
            bits_above ^= b_bit

            mask_above_b = (-1) << b  # keep bits for nodes > b
            common = adj[a] & adj[b] & mask_above_b
            if common:
                c_bit = common & -common
                c = (c_bit.bit_length() - 1) + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()