import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1

    terminals = [int(input_data[idx + i]) for i in range(t)]
    idx += t

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    if t <= 1:
        print(0)
        return

    is_terminal = [False] * (n + 1)
    for x in terminals:
        is_terminal[x] = True

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0 and v != parent[1]:
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                stack.append(v)

    cnt = [1 if is_terminal[u] else 0 for u in range(n + 1)]
    for u in reversed(order):
        if u != 1:
            cnt[parent[u]] += cnt[u]

    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_weight[u]

    print(total)

if __name__ == "__main__":
    solve()