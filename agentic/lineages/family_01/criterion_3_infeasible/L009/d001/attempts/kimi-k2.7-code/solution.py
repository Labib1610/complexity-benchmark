import sys
import bisect

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)
    for i in range(n):
        neigh[i].sort()
    full = (1 << n) - 1
    suffix = [0] * n
    for b in range(n):
        suffix[b] = full ^ ((1 << (b + 1)) - 1)
    for a in range(n):
        lst = neigh[a]
        idx = bisect.bisect_right(lst, a)
        for b in lst[idx:]:
            common = adj[a] & adj[b] & suffix[b]
            if common:
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()