import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [0] * (n + 1)  # 1-indexed
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        neigh_a = adj[a]
        mask_a = ~((1 << a) - 1)  # keep bits >= a
        cand_b = neigh_a & mask_a
        while cand_b:
            lowest_b = (cand_b & -cand_b).bit_length() - 1
            b = lowest_b + 1
            common = neigh_a & adj[b]
            mask_b = ~((1 << b) - 1)  # keep bits > b-1 => bits >= b
            common_masked = common & mask_b
            if common_masked:
                lowest_c = (common_masked & -common_masked).bit_length() - 1
                c = lowest_c + 1
                print(a, b, c)
                return
            cand_b &= cand_b - 1

if __name__ == "__main__":
    solve()