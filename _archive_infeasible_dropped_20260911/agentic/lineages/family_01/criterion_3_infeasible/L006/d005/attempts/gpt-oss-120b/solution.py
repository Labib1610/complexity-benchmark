import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    masks = [0] * n          # neighbour bitsets
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u

    for a in range(n):
        mask_a = masks[a]
        for b in range(a + 1, n):
            # edge a-b ?
            if (mask_a >> b) & 1:
                inter = mask_a & masks[b]          # common neighbours
                shifted = inter >> (b + 1)         # keep only > b
                if shifted:
                    # least set bit -> smallest c
                    lsb = shifted & -shifted
                    offset = lsb.bit_length() - 1
                    c = b + 1 + offset
                    # output 1‑based indices
                    sys.stdout.write(f"{a+1} {b+1} {c+1}")
                    return

if __name__ == "__main__":
    solve()