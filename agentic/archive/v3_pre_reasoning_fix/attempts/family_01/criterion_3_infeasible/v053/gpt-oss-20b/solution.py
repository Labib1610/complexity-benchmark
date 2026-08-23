import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    mask = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        mask[u] |= 1 << (v - 1)
        mask[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        mask_a = mask[a]
        for b in range(a + 1, n):
            if mask_a & (1 << (b - 1)):
                common = mask_a & mask[b]
                # keep only neighbors with index > b
                common &= ~((1 << b) - 1)
                if common:
                    lowbit = common & -common
                    c = lowbit.bit_length()  # vertex number
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()