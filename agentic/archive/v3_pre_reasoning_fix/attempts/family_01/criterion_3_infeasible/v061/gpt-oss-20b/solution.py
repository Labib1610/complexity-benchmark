import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    for a in range(n):
        mask_a = adj[a] >> (a + 1)  # neighbors with index > a
        while mask_a:
            lsb = mask_a & -mask_a
            b_rel = lsb.bit_length() - 1
            b = a + 1 + b_rel  # 0‑index of b
            # intersection of neighbors of a and b
            mask_ab = adj[a] & adj[b]
            mask_ab_shift = mask_ab >> (b + 1)  # keep c > b
            if mask_ab_shift:
                lsb2 = mask_ab_shift & -mask_ab_shift
                c_rel = lsb2.bit_length() - 1
                c = b + 1 + c_rel  # 0‑index of c
                print(a + 1, b + 1, c + 1)
                return
            mask_a -= lsb

if __name__ == "__main__":
    solve()