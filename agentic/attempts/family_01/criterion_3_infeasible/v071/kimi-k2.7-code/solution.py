import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    p = 2
    for _ in range(m):
        u = data[p]
        v = data[p + 1]
        p += 2
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    allbits = (1 << n) - 1
    for x in range(1, n + 1):
        ax = adj[x]
        for y in neigh[x]:
            if y <= x:
                continue
            common = ax & adj[y]
            if common:
                mask = allbits & ~((1 << y) - 1)
                cand = common & mask
                if cand:
                    z = (cand & -cand).bit_length()
                    sys.stdout.write(f"{x} {y} {z}\n")
                    return

if __name__ == "__main__":
    solve()