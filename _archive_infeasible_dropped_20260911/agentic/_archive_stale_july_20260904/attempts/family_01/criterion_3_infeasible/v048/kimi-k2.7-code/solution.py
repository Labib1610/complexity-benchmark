import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]
    p = 2
    for _ in range(m):
        u = int(data[p])
        v = int(data[p + 1])
        p += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)
    for i in range(1, n + 1):
        neigh[i].sort()
    for a in range(1, n + 1):
        ma = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = (ma & adj[b]) >> (b + 1)
            if common:
                low = common & -common
                c = low.bit_length() - 1 + b + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()