import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    p = 2
    for _ in range(m):
        u = int(data[p])
        v = int(data[p + 1])
        p += 2
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        bits = adj[a] & ~((1 << a) - 1)
        while bits:
            lsb = bits & -bits
            b = lsb.bit_length()
            common = adj[a] & adj[b]
            common &= ~((1 << b) - 1)
            if common:
                c = (common & -common).bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()