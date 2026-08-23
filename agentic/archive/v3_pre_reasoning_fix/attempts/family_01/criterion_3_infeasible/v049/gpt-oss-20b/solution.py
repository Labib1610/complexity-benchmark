import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    masks = [0] * n  # 0-indexed nodes 0..n-1
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u

    for a in range(1, n + 1):          # a is 1-indexed
        ma = masks[a - 1]
        for b in range(a + 1, n + 1):  # b > a
            if (ma >> (b - 1)) & 1:    # edge exists
                inter = ma & masks[b - 1]
                inter2 = inter >> b   # shift to remove bits <= b
                if inter2:
                    lsb = inter2 & -inter2
                    c = b + lsb.bit_length()
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()