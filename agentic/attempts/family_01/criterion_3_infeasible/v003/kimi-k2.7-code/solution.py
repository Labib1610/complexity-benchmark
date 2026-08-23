import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u > v:
            u, v = v, u
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))
    edges.sort()
    all_one = (1 << n) - 1
    for u, v in edges:
        mask = all_one & ~((1 << (v + 1)) - 1)
        common = adj[u] & adj[v] & mask
        if common:
            c = (common & -common).bit_length() - 1
            sys.stdout.write(f"{u + 1} {v + 1} {c + 1}")
            return

if __name__ == "__main__":
    solve()