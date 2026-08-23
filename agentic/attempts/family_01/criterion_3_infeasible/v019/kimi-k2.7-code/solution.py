import sys
from bisect import bisect_right

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    bits = [0] * n

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        bits[u] |= 1 << v
        bits[v] |= 1 << u

    for lst in adj:
        lst.sort()

    br = bisect_right
    for a in range(n):
        lista = adj[a]
        start = br(lista, a)
        ba = bits[a]
        for idx in range(start, len(lista)):
            b = lista[idx]
            common = ba & bits[b]
            shift = b + 1
            mask = common >> shift
            if mask:
                c = (mask & -mask).bit_length() - 1 + shift
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()