import sys

def solve():
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

    mask_gt = [0] * n
    for i in range(n - 1):
        mask_gt[i] = ((1 << (n - 1 - i)) - 1) << (i + 1)

    for a in range(n):
        cand = adj[a] & mask_gt[a]
        while cand:
            lsb = cand & -cand
            b = lsb.bit_length() - 1
            common = adj[a] & adj[b] & mask_gt[b]
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}\n")
                return
            cand ^= lsb

if __name__ == "__main__":
    solve()