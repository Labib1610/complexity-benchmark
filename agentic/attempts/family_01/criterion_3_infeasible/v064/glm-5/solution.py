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
    for i in range(1, n + 1):
        adj[i] |= 1 << i
    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in range(a + 1, n + 1):
            if mask_a & (1 << b):
                common = mask_a & adj[b]
                if common >> (b + 1):
                    c = (common & -common).bit_length() - 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()