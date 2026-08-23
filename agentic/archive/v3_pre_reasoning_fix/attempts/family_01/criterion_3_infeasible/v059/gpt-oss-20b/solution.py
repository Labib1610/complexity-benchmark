import sys

def solve() -> None:
    input = sys.stdin.readline
    n_m = input().split()
    while len(n_m) < 2:
        n_m += input().split()
    n, m = map(int, n_m)

    adjacency = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency[u] |= 1 << (v - 1)
        adjacency[v] |= 1 << (u - 1)

    full_mask = (1 << n) - 1
    mask_above = [0] * (n + 1)
    for b in range(n + 1):
        mask_above[b] = (~((1 << b) - 1)) & full_mask

    for a in range(1, n - 1):
        neigh = adjacency[a]
        bits = neigh >> a  # only consider neighbors > a
        while bits:
            lsb = bits & -bits
            b_idx = lsb.bit_length() - 1
            b = a + 1 + b_idx
            inter = adjacency[a] & adjacency[b]
            mask = inter & mask_above[b]
            if mask:
                lsb2 = mask & -mask
                c_idx = lsb2.bit_length() - 1
                c = c_idx + 1
                print(a, b, c)
                return
            bits ^= lsb

if __name__ == "__main__":
    solve()