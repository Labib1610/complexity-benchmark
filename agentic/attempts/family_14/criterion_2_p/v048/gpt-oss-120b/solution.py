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

    if t <= 1:
        print(0)
        return

    parent = [-1] * n
    pw = [0] * n          # weight to parent
    order = []            # traversal order
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                pw[v] = w
                stack.append(v)

    cnt = [0] * n
    for i in range(n):
        if i in terminals:
            cnt[i] = 1

    total = 0
    for u in reversed(order):
        if u == 0:
            continue
        c = cnt[u]
        if 0 < c < t:
            total += pw[u]
        cnt[parent[u]] += c

    print(total)

if __name__ == "__main__":
    solve()