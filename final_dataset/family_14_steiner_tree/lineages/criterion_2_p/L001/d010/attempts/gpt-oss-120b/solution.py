import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1, not used separately
    t = int(next(it))

    is_term = [False] * (n + 1)
    for _ in range(t):
        v = int(next(it))
        is_term[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
    order = []

    # iterative DFS to avoid recursion depth problems
    stack = [1]
    parent[1] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if to != parent[v]:
                parent[to] = v
                pw[to] = w
                stack.append(to)

    cnt = [0] * (n + 1)
    ans = 0
    # process in reverse order (post‑order)
    for v in reversed(order):
        c = 1 if is_term[v] else 0
        for to, _ in adj[v]:
            if parent[to] == v:          # child
                c += cnt[to]
        cnt[v] = c
        if v != 1:                       # has a parent edge
            if 0 < c < t:
                ans += pw[v]

    print(ans)


if __name__ == "__main__":
    solve()