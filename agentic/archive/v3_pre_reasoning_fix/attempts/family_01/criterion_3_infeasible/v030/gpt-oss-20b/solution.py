import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    mask = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        mask[u] |= 1 << (v - 1)
        mask[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        ma = mask[a]
        for b in range(a + 1, n + 1):
            if (ma >> (b - 1)) & 1:
                intersection = ma & mask[b]
                # remove vertices <= b
                mask2 = intersection >> b
                if mask2:
                    lsb = mask2 & -mask2
                    pos = lsb.bit_length() - 1
                    c = pos + b + 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()