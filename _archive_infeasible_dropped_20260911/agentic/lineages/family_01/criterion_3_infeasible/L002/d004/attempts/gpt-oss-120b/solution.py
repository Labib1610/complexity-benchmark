import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # undirected adjacency as bit masks (0‑based indices)
    masks = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set edge in both directions
        masks[u] |= 1 << v
        masks[v] |= 1 << u

    full_mask = (1 << n) - 1

    for i in range(n):
        mi = masks[i]
        # iterate j > i where edge i‑j exists
        # extract bits > i
        j_bits = mi & ~((1 << (i + 1)) - 1)
        while j_bits:
            low = j_bits & -j_bits
            j = low.bit_length() - 1
            # common neighbors of i and j
            common = masks[i] & masks[j]
            # keep only k > j
            common &= ~((1 << (j + 1)) - 1)
            if common:
                lowk = common & -common
                k = lowk.bit_length() - 1
                # output 1‑based sorted triple
                print(i + 1, j + 1, k + 1)
                return
            # remove processed j
            j_bits ^= low

if __name__ == "__main__":
    solve()