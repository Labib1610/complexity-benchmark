import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # neighbours[i] : bitset of vertices adjacent to i (bits 0..n-1)
    neighbours = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits (v-1) and (u-1)
        neighbours[u] |= 1 << (v - 1)
        neighbours[v] |= 1 << (u - 1)

    for x in range(1, n - 1):
        bx = neighbours[x]
        for y in range(x + 1, n):
            # check edge (x, y)
            if not ((bx >> (y - 1)) & 1):
                continue
            common = bx & neighbours[y]
            mask = common >> y          # keep only vertices > y
            if mask:
                # position of lowest set bit
                tz = (mask & -mask).bit_length() - 1
                z = y + tz + 1
                sys.stdout.write(f"{x} {y} {z}")
                return

if __name__ == "__main__":
    solve()