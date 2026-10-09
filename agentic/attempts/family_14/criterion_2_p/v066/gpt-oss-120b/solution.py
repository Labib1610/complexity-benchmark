import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it)
    m = next(it)          # equals n-1, not used separately
    t = next(it)

    specials = [False] * (n + 1)
    for _ in range(t):
        v = next(it)
        specials[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    # iterative DFS to get parent, weight to parent and order
    parent = [0] * (n + 1)
    wpar = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1  # mark root

    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            wpar[to] = w
            stack.append(to)

    # post-order count of specials in each subtree
    sub = [0] * (n + 1)
    for v in reversed(order):
        cnt = 1 if specials[v] else 0
        for to, _ in adj[v]:
            if parent[to] == v:   # child
                cnt += sub[to]
        sub[v] = cnt

    # sum weights of edges that separate specials
    ans = 0
    if t > 1:   # otherwise answer is 0 automatically
        for v in range(2, n + 1):
            if 0 < sub[v] < t:
                ans += wpar[v]

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()