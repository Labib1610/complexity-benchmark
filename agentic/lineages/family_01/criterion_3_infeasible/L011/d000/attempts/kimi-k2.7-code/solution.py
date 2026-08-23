import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    m = data[1]
    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]
    p = 2
    for _ in range(m):
        u = data[p]
        v = data[p + 1]
        p += 2
        if u == v:
            continue
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)
    for lst in neigh:
        lst.sort()
    write = sys.stdout.write
    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common_gt = (adj[b] & mask_a) & -(1 << b)
            if common_gt:
                c = (common_gt & -common_gt).bit_length()
                write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()