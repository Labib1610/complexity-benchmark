import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    t = int(data[2])

    idx = 3
    critical = [int(x) for x in data[idx : idx + t]]
    idx += t

    is_crit = [0] * (n + 1)
    for c in critical:
        is_crit[c] = 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    weight_to_parent = [0] * (n + 1)
    order = [1]
    visited = [False] * (n + 1)
    visited[1] = True

    head = 0
    while head < len(order):
        u = order[head]
        head += 1
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                weight_to_parent[v] = w
                order.append(v)

    c_cnt = list(is_crit)
    total_cost = 0

    for u in reversed(order):
        if 0 < c_cnt[u] < t:
            total_cost += weight_to_parent[u]
        p = parent[u]
        if p != 0:
            c_cnt[p] += c_cnt[u]

    print(total_cost)


if __name__ == "__main__":
    solve()