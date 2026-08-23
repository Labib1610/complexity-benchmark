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

    for a in range(1, n + 1):
        cand = adj[a] & ~((1 << (a + 1)) - 1)  # neighbors of a with index > a
        temp = cand
        while temp:
            lsb = temp & -temp
            b = lsb.bit_length() - 1
            temp ^= lsb
            x = adj[b] & cand & ~((1 << (b + 1)) - 1)
            if x:
                c = (x & -x).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()