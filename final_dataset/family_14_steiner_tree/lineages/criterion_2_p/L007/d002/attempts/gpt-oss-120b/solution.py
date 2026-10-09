import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)          # number of racks
    m = next(it)          # = n-1
    t = next(it)          # number of rented racks

    specials = [next(it) for _ in range(t)]

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    root = 1
    parent = [0] * (n + 1)   # parent[node]
    pw = [0] * (n + 1)        # weight to parent
    order = []                # preorder

    stack = [root]
    parent[root] = -1        # mark root
    while stack:
        node = stack.pop()
        order.append(node)
        for nb, w in adj[node]:
            if nb != parent[node]:
                parent[nb] = node
                pw[nb] = w
                stack.append(nb)

    cnt = [0] * (n + 1)
    for s in specials:
        cnt[s] = 1

    ans = 0
    for node in reversed(order):
        if node == root:
            continue
        c = cnt[node]
        if 0 < c < t:
            ans += pw[node]
        cnt[parent[node]] += c

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()