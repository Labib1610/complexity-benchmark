import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    essential = [0] * (n + 1)
    for _ in range(t):
        essential[int(next(it))] = 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight to parent
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

    sub_cnt = [0] * (n + 1)
    total = 0
    for u in reversed(order):
        cnt = essential[u]
        for v, _ in adj[u]:
            if parent[v] == u:
                cnt += sub_cnt[v]
        sub_cnt[u] = cnt
        if u != 1:
            # edge (parent[u], u) is needed if both sides contain essential nodes
            if 0 < sub_cnt[u] < t:
                total += pw[u]
    print(total)

if __name__ == "__main__":
    solve()