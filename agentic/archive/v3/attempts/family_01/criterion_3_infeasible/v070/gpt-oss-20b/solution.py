import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        a_mask = adj[a]
        for b in range(a + 1, n):
            if (a_mask >> (b - 1)) & 1:
                inter = a_mask & adj[b]
                if inter:
                    # mask bits > b
                    if n - b == 0:
                        mask = 0
                    else:
                        mask = ((1 << (n - b)) - 1) << b
                    inter_masked = inter & mask
                    if inter_masked:
                        lowbit = inter_masked & -inter_masked
                        c = lowbit.bit_length()  # lowbit = 1 << (c-1)
                        print(a, b, c)
                        return

if __name__ == "__main__":
    solve()