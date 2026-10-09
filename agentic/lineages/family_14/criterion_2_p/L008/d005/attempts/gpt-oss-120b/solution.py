import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    R = int(next(it))
    S = int(next(it))  # = R-1
    P = int(next(it))
    terminals = set(int(next(it)) for _ in range(P))

    adj = [[] for _ in range(R + 1)]
    edges = []
    for _ in range(S):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    if P == 1:
        print(0)
        return

    parent = [0] * (R + 1)
    pw = [0] * (R + 1)          # weight to parent
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

    sub_cnt = [0] * (R + 1)
    for u in reversed(order):
        cnt = 1 if u in terminals else 0
        for v, _ in adj[u]:
            if parent[v] == u:
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt

    total = 0
    for v in range(2, R + 1):
        cnt = sub_cnt[v]
        if 0 < cnt < P:
            total += pw[v]

    print(total)

if __name__ == "__main__":
    solve()