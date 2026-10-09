import sys
import bisect

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
    for a in range(1, n + 1):
        ba = adj[a]
        lst = neigh[a]
        idx = bisect.bisect_right(lst, a)
        for b in lst[idx:]:
            common = ba & adj[b]
            t = common >> b
            if t:
                lsb = t & -t
                c = lsb.bit_length() + b
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()