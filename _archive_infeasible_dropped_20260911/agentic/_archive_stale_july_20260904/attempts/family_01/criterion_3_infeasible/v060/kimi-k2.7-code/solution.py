import sys

def solve() -> None:
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
        for b in range(a + 1, n + 1):
            if not (adj[a] >> b) & 1:
                continue
            common = (adj[a] & adj[b]) >> (b + 1)
            if common:
                lsb = common & -common
                c = lsb.bit_length() + b
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()