import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # equals n-1
    t = int(next(it))
    crit = set(int(next(it)) - 1 for _ in range(t))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [-1] * n
    pw = [0] * n          # weight to parent
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            pw[v] = w
            stack.append(v)

    cnt = [0] * n
    for i in range(n):
        if i in crit:
            cnt[i] = 1

    ans = 0
    for u in reversed(order):
        if u == 0:
            continue
        if cnt[u] > 0 and cnt[u] < t:
            ans += pw[u]
        cnt[parent[u]] += cnt[u]

    print(ans)

if __name__ == "__main__":
    solve()