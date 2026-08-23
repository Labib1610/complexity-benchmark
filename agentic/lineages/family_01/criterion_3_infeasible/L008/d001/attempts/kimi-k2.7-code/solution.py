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

    suffix = [0] * (n + 1)
    for i in range(n + 1):
        suffix[i] = ~((1 << (i + 1)) - 1)

    for a in range(1, n - 1):
        mask_b = adj[a] & suffix[a]
        while mask_b:
            low_b = mask_b & -mask_b
            b = low_b.bit_length() - 1
            common = adj[a] & adj[b]
            cmask = common & suffix[b]
            if cmask:
                c = (cmask & -cmask).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return
            mask_b ^= low_b

if __name__ == "__main__":
    solve()