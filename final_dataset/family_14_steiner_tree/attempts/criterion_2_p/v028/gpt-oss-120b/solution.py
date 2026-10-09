import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))  # = n-1
    t = int(next(it))
    terminals = [0] * (n + 1)
    for _ in range(t):
        terminals[int(next(it))] = 1

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

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

    sub = terminals[:]          # copy counts
    ans = 0
    total_term = t
    for u in reversed(order):
        if parent[u] == -1:
            continue
        cnt = sub[u]
        if cnt > 0 and total_term - cnt > 0:
            ans += pw[u]
        sub[parent[u]] += cnt

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()