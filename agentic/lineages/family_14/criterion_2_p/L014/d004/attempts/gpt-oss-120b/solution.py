import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)          # equals n-1, not used separately
    t = next(it)

    specials = [0] * (n + 1)
    for _ in range(t):
        v = next(it)
        specials[v] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it); w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    root = 1
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
    order = []                  # preorder list

    stack = [(root, 0, 0)]
    while stack:
        node, par, w = stack.pop()
        parent[node] = par
        pw[node] = w
        order.append(node)
        for nb, wt in adj[node]:
            if nb != par:
                stack.append((nb, node, wt))

    cnt = [0] * (n + 1)
    for node in reversed(order):
        c = specials[node]
        for nb, _ in adj[node]:
            if nb != parent[node]:
                c += cnt[nb]
        cnt[node] = c

    total = 0
    for v in range(2, n + 1):          # all except root
        if 0 < cnt[v] < t:
            total += pw[v]

    print(total)

if __name__ == "__main__":
    solve()