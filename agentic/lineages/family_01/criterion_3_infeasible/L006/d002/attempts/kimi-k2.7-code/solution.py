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

    full = (1 << n) - 1
    gt = [0] * n
    for i in range(n - 1):
        gt[i] = full ^ ((1 << (i + 1)) - 1)

    for a in range(n):
        A = adj[a] & gt[a]
        while A:
            low = A & -A
            b = low.bit_length() - 1
            C = adj[b] & A & gt[b]
            if C:
                c = (C & -C).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}")
                return
            A ^= low

if __name__ == "__main__":
    solve()