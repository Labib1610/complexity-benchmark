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
        if u > v:
            u, v = v, u
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edges.append((u, v))

    all_mask = (1 << n) - 1
    suffix = [0] * (n + 1)
    for x in range(n + 1):
        suffix[x] = all_mask & ~((1 << x) - 1)

    edges.sort()
    for a, b in edges:
        common = adj[a] & adj[b]
        cand = common & suffix[b]
        if cand:
            lsb = cand & -cand
            c = lsb.bit_length()
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()