import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * (n + 1)
    adj = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)
        adj[u].add(v)
        adj[v].add(u)

    adj_list = [None] * (n + 1)
    for i in range(1, n + 1):
        adj_list[i] = sorted(adj[i])

    for a in range(1, n + 1):
        ma = masks[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            cmask = (ma & masks[b]) & ~((1 << b) - 1)
            if cmask:
                c = (cmask & -cmask).bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return

solve()