import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * n
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set bits
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        if u < v:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)

    # ensure neighbours are sorted (they already are because we added in input order,
    # but sorting guarantees correctness)
    for lst in adj_list:
        lst.sort()

    for a in range(n):
        bits_a = adj_bits[a]
        for b in adj_list[a]:          # b > a
            # intersection of neighbours of a and b
            common = bits_a & adj_bits[b]
            # keep only vertices > b
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length() - 1
                # output in 1‑based, already a<b<c
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()