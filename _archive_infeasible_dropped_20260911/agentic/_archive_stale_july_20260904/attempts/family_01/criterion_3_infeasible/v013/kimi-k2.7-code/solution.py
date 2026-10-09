import sys
import bisect

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    for i in range(1, n + 1):
        adj[i].sort()

    for a in range(1, n + 1):
        ma = masks[a]
        lst = adj[a]
        idx = bisect.bisect_right(lst, a)
        for i in range(idx, len(lst)):
            b = lst[i]
            common = ma & masks[b]
            shifted = common >> b
            if shifted:
                low = shifted & -shifted
                c = b + low.bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()