import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))          # = n-1, not used separately
    t = int(next(it))

    required = [False] * (n + 1)
    for _ in range(t):
        required[int(next(it))] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    w_to_parent = [0] * (n + 1)
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
                w_to_parent[to] = w
                stack.append(to)

    cnt = [0] * (n + 1)
    ans = 0
    for v in reversed(order):
        cnt[v] = 1 if required[v] else 0
        for to, _ in adj[v]:
            if parent[to] == v:          # child
                cnt[v] += cnt[to]
        if v != 1 and 0 < cnt[v] < t:
            ans += w_to_parent[v]

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()