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
        a_adj = adj[a]
        for b in range(a + 1, n):
            if not (a_adj >> b) & 1:   # edge a-b absent
                continue
            common = a_adj & adj[b]    # vertices adjacent to both a and b
            # clear bits <= b
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= mask
            if common:
                # least significant 1-bit
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()