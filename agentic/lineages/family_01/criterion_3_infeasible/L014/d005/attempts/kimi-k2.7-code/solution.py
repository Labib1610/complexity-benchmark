import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)
    for i in range(1, n + 1):
        neighbors[i].sort()
    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in neighbors[a]:
            if b <= a:
                continue
            common = mask_a & adj[b]
            shifted = common >> (b + 1)
            if shifted:
                c = ((shifted & -shifted).bit_length() - 1) + b + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()