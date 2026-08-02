import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)  # 1-indexed
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (adj[a] >> (b - 1)) & 1:
                inter = adj[a] & adj[b]
                mask = inter >> b  # consider nodes > b
                if mask:
                    lsb = mask & -mask
                    idx = lsb.bit_length() - 1
                    c = idx + b + 1
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()