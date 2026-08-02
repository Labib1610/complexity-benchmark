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
        for b in range(a + 1, n):
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                mask = common >> (b + 1)          # bits for nodes > b
                if mask:
                    lsb = mask & -mask
                    pos = lsb.bit_length() - 1
                    c = pos + b + 1
                    sys.stdout.write(f"{a+1} {b+1} {c}\n")
                    return

if __name__ == "__main__":
    solve()