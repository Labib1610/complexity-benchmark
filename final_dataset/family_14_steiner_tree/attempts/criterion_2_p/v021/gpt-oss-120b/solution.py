import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    terminals = set()
    for _ in range(t):
        terminals.add(int(next(it)) - 1)  # zero‑based
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [-1] * n
    pw = [0] * n          # weight of edge to parent
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
    ans = 0
    for v in reversed(order):
        if v in terminals:
            cnt[v] = 1
        for to, _ in adj[v]:
            if parent[to] == v:          # child
                cnt[v] += cnt[to]
        if v != 0:
            if 0 < cnt[v] < t:
                ans += pw[v]

    print(ans)

if __name__ == "__main__":
    solve()