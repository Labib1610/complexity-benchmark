import sys
from bisect import bisect_left

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    # mask_up_to[k] has bits 0..k-1 set
    mask_up_to = [(1 << k) - 1 for k in range(n + 1)]

    for a in range(1, n + 1):
        adj_a = adj[a]
        lst = neigh[a]
        idx = bisect_left(lst, a + 1)
        for k in range(idx, len(lst)):
            b = lst[k]
            common = adj_a & adj[b]
            if common:
                cand = common & ~mask_up_to[b]
                if cand:
                    c = (cand & -cand).bit_length()
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    solve()