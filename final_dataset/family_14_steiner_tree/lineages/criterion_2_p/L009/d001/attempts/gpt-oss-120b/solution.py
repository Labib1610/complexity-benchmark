import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); E = int(next(it)); F = int(next(it))
    specials = set(int(next(it)) for _ in range(F))
    adj = [[] for _ in range(N + 1)]
    edges = []
    for _ in range(E):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    if F <= 1:
        print(0)
        return

    parent = [0] * (N + 1)
    pw = [0] * (N + 1)          # weight to parent
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            pw[v] = w
            stack.append(v)

    sub_cnt = [0] * (N + 1)
    for u in reversed(order):
        cnt = 1 if u in specials else 0
        for v, _ in adj[u]:
            if parent[v] == u:
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt

    total = 0
    for v in range(2, N + 1):
        cnt = sub_cnt[v]
        if 0 < cnt < F:
            total += pw[v]
    print(total)

if __name__ == "__main__":
    solve()