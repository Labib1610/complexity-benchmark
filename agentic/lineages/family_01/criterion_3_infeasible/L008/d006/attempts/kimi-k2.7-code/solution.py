import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    masks = [0] * n
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)
    for lst in adj:
        lst.sort()
    for a in range(n):
        ma = masks[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ma & masks[b]
            cand = common >> (b + 1)
            if cand:
                c = (cand & -cand).bit_length() - 1 + b + 1
                print(a + 1, b + 1, c + 1)
                return

solve()