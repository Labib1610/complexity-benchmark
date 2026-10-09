import sys
from sys import setrecursionlimit

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    critical = [False] * (n + 1)
    for _ in range(t):
        c = int(data[idx]); idx += 1
        critical[c] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    setrecursionlimit(1 << 25)

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)

    cnt = [1 if critical[i] else 0 for i in range(n + 1)]

    for u in reversed(order):
        if u != 1:
            p = parent[u]
            cnt[p] += cnt[u]

    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0:
            total += parent_weight[u]

    print(total)

if __name__ == "__main__":
    main()