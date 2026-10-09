import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    E = int(next(it))  # equals N-1
    F = int(next(it))
    critical = [0] * (N + 1)
    for _ in range(F):
        critical[int(next(it))] = 1

    adj = [[] for _ in range(N + 1)]
    edges = []
    for _ in range(E):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w, len(edges)))
        adj[v].append((u, w, len(edges)))
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
        node = stack.pop()
        order.append(node)
        for nb, w, _ in adj[node]:
            if nb == parent[node]:
                continue
            parent[nb] = node
            pw[nb] = w
            stack.append(nb)

    cnt = [0] * (N + 1)
    for i in range(1, N + 1):
        cnt[i] = critical[i]

    total = 0
    for node in reversed(order):
        if node == 1:
            continue
        if 0 < cnt[node] < F:
            total += pw[node]
        cnt[parent[node]] += cnt[node]

    print(total)

if __name__ == "__main__":
    solve()