import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    mask_gt = [0] * (n + 2)
    cur = 0
    for i in range(n, -1, -1):
        mask_gt[i] = cur
        cur |= 1 << i

    for a in range(1, n - 1):
        bits = adj[a] >> (a + 1)
        while bits:
            lsb = bits & -bits
            b = a + 1 + (lsb.bit_length() - 1)
            cand = adj[a] & adj[b] & mask_gt[b]
            if cand:
                lsb_c = cand & -cand
                c = lsb_c.bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}\n")
                return
            bits ^= lsb

if __name__ == "__main__":
    solve()