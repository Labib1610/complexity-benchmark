import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1
    t = int(next(it))
    mandatory = [int(next(it)) - 1 for _ in range(t)]

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [-1] * n
    pw = [0] * n          # weight to parent
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if parent[to] == -1:
                parent[to] = v
                pw[to] = w
                stack.append(to)

    cnt = [0] * n
    for v in mandatory:
        cnt[v] = 1

    ans = 0
    for v in reversed(order):
        if v == 0:
            continue
        p = parent[v]
        if 0 < cnt[v] < t:
            ans += pw[v]
        cnt[p] += cnt[v]

    print(ans)

if __name__ == "__main__":
    solve()