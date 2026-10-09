import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)   # equals n-1, not used
    t = next(it)

    is_crit = [False] * (n + 1)
    for _ in range(t):
        v = next(it)
        is_crit[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it); w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    wpar = [0] * (n + 1)          # weight to parent
    order = []
    stack = [1]
    parent[1] = -1                # mark root as visited

    while stack:
        v = stack.pop()
        order.append(v)
        for to, w in adj[v]:
            if parent[to] == 0:
                parent[to] = v
                wpar[to] = w
                stack.append(to)

    sub = [0] * (n + 1)
    total = 0
    for v in reversed(order):
        cnt = 1 if is_crit[v] else 0
        for to, w in adj[v]:
            if parent[to] == v:          # to is a child of v
                child_cnt = sub[to]
                if 0 < child_cnt < t:
                    total += w
                cnt += child_cnt
        sub[v] = cnt

    print(total)

if __name__ == "__main__":
    solve()