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

    for a in range(n):
        mask_a = adj[a] & (-1 << (a + 1))
        t = mask_a
        while t:
            lsb = t & -t
            b = lsb.bit_length() - 1
            cand = mask_a & adj[b] & (-1 << (b + 1))
            if cand:
                c = (cand & -cand).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}\n")
                return

if __name__ == "__main__":
    solve()