import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # mask[v]: bitset of neighbours w with w > v
    mask = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        # now u < v
        mask[u] |= 1 << v

    for a in range(1, n + 1):
        bits = mask[a]
        while bits:
            lsb = bits & -bits
            b = lsb.bit_length() - 1   # neighbour > a
            bits ^= lsb

            common = mask[a] & mask[b]   # vertices > b adjacent to both
            if common:
                lsb2 = common & -common
                c = lsb2.bit_length() - 1
                # a < b < c automatically
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()