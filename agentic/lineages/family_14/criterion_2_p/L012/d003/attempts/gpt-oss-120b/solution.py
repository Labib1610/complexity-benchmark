import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)          # = n-1, not used separately
    t = next(it)

    specials = [next(it) for _ in range(t)]
    is_special = [False] * (n + 1)
    for v in specials:
        is_special[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    # ---------- root the tree ----------
    parent = [0] * (n + 1)          # 0 = no parent (root)
    pw = [0] * (n + 1)              # weight to parent
    order = []                      # preorder list

    stack = [1]
    parent[1] = -1                  # mark root
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                pw[v] = w
                stack.append(v)

    # ---------- count specials in subtrees ----------
    cnt = [0] * (n + 1)
    for v in specials:
        cnt[v] = 1

    for u in reversed(order):
        p = parent[u]
        if p > 0:                   # ignore the root (parent = -1)
            cnt[p] += cnt[u]

    # ---------- sum needed edges ----------
    total = 0
    for v in range(2, n + 1):       # all vertices except the root
        if 0 < cnt[v] < t:
            total += pw[v]

    print(total)


if __name__ == "__main__":
    solve()