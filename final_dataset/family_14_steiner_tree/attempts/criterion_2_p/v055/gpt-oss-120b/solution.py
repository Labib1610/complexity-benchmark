import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1, not used separately
    t = int(next(it))

    special = [False] * (n + 1)
    for _ in range(t):
        v = int(next(it))
        special[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    # iterative DFS to obtain parent, edge weight to parent, and order
    parent = [0] * (n + 1)
    w_parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1  # root marker
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to != parent[v]:
                parent[to] = v
                w_parent[to] = w
                stack.append(to)

    cnt = [0] * (n + 1)
    ans = 0
    # process in reverse order = postorder
    for v in reversed(order):
        c = 1 if special[v] else 0
        # accumulate children's counts
        for to, _ in adj[v]:
            if parent[to] == v:          # to is child
                c += cnt[to]
                if 0 < cnt[to] < t:      # edge (v,to) is necessary
                    ans += w_parent[to]
        cnt[v] = c

    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 25)
    solve()