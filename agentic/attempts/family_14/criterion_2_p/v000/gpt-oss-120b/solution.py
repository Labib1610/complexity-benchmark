import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)          # = n-1, not used separately
    t = next(it)

    required = [0] * (n + 1)
    for _ in range(t):
        required[next(it)] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    root = 1
    parent = [0] * (n + 1)
    order = []
    stack = [(root, 0)]
    while stack:
        v, p = stack.pop()
        parent[v] = p
        order.append(v)
        for to, w in adj[v]:
            if to != p:
                stack.append((to, v))

    cnt = [0] * (n + 1)
    answer = 0
    for v in reversed(order):
        cnt[v] = required[v]
        for to, w in adj[v]:
            if parent[to] == v:          # to is child
                cnt[v] += cnt[to]
                if 0 < cnt[to] < t:      # edge v‑to is needed
                    answer += w

    print(answer)


if __name__ == "__main__":
    solve()