import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # neighbours[i] is a bitset (int) of vertices adjacent to i (0‑based)
    neighbours = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbours[u] |= 1 << v
        neighbours[v] |= 1 << u

    for a in range(n):
        na = neighbours[a]
        for b in range(a + 1, n):
            # check edge a–b
            if (na >> b) & 1:
                common = na & neighbours[b]          # vertices adjacent to both
                # keep only vertices > b
                mask = common >> (b + 1)
                if mask:
                    low = mask & -mask               # lowest set bit
                    idx = low.bit_length() - 1      # position inside mask
                    c = b + 1 + idx
                    # output 1‑based indices
                    sys.stdout.write(f"{a+1} {b+1} {c+1}")
                    return

if __name__ == "__main__":
    solve()