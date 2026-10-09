import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    specials = set()
    for _ in range(t):
        specials.add(int(next(it)) - 1)   # zero‑based
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w, len(edges)))
        adj[v].append((u, w, len(edges)))
        edges.append((u, v, w))

    parent = [-1] * n
    pw = [0] * n          # weight of edge to parent
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        v = stack.pop()
        order.append(v)
        for to, w, _ in adj[v]:
            if parent[to] == -1:
                parent[to] = v
                pw[to] = w
                stack.append(to)

    sub_special = [0] * n
    for v in reversed(order):
        cnt = 1 if v in specials else 0
        for to, _, _ in adj[v]:
            if parent[to] == v:
                cnt += sub_special[to]
        sub_special[v] = cnt

    total = 0
    for v in range(1, n):
        cnt = sub_special[v]
        if 0 < cnt < t:
            total += pw[v]

    print(total)

if __name__ == "__main__":
    solve()