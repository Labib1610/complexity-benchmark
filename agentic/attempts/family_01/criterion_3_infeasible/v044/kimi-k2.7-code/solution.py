import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        if u > v:
            u, v = v, u
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edges.append((u, v))
    edges.sort()
    for a, b in edges:
        inter = adj[a] & adj[b]
        if inter:
            shifted = inter >> b
            if shifted:
                c = b + 1 + ((shifted & -shifted).bit_length() - 1)
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()