import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # find a leaf to use as root
    root = 1
    for i in range(1, n + 1):
        if len(adj[i]) == 1:
            root = i
            break

    # iterative DFS to get order of first visits
    order = []
    stack = [(root, 0)]          # (node, parent)
    visited = [False] * (n + 1)
    while stack:
        u, p = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for v in adj[u][::-1]:   # reverse to keep natural order
            if v != p:
                stack.append((v, u))

    pos = [0] * (n + 1)
    for idx, node in enumerate(order, start=1):
        pos[node] = idx

    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:  # each edge once
                total += abs(pos[u] - pos[v])

    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()