import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << n) - 1
    for a in range(n):
        a_mask = adj[a]
        for b in range(a + 1, n):
            if (a_mask >> b) & 1 == 0:
                continue
            common = a_mask & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= mask
            if common:
                low_bit = common & -common
                c = low_bit.bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()