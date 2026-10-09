import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))   # = n-1, not used
    t = int(next(it))
    targets = [0] * (n + 1)
    for _ in range(t):
        targets[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    root = 1
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            pw[to] = w
            stack.append(to)

    sub = [0] * (n + 1)
    for v in reversed(order):
        cnt = targets[v]
        for to, _ in adj[v]:
            if parent[to] == v:   # child
                cnt += sub[to]
        sub[v] = cnt

    ans = 0
    for v in range(2, n + 1):
        cnt = sub[v]
        if 0 < cnt < t:
            ans += pw[v]

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()