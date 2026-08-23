import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bits = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neighbors[u].append(v)
        neighbors[v].append(u)

    for lst in neighbors:
        lst.sort()

    all_ones = (1 << n) - 1

    for a in range(1, n - 1):
        for b in neighbors[a]:
            if b <= a:
                continue
            mask_high_b = all_ones ^ ((1 << b) - 1)
            common = adj_bits[a] & adj_bits[b] & mask_high_b
            if common:
                c_bit = common & -common
                c = c_bit.bit_length()  # 1-based index
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()