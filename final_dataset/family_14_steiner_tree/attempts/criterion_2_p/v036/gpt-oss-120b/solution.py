import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1, not used separately
    t = int(next(it))

    specials = [0] * (n + 1)
    for _ in range(t):
        v = int(next(it))
        specials[v] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight of edge to parent
    order = []

    stack = [1]
    parent[1] = -1              # mark root
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            pw[to] = w
            stack.append(to)

    cnt = [0] * (n + 1)
    for v in reversed(order):
        c = specials[v]
        for to, _ in adj[v]:
            if parent[to] == v:          # child
                c += cnt[to]
        cnt[v] = c

    total = 0
    for v in range(2, n + 1):            # skip root (1)
        if cnt[v] > 0 and t - cnt[v] > 0:
            total += pw[v]

    sys.stdout.write(str(total))

if __name__ == "__main__":
    solve()