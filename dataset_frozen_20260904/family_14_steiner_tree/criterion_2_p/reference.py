import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); t = int(data[idx + 2]); idx += 3
    terminals = [int(data[idx + i]) for i in range(t)]; idx += t
    is_term = [False] * (n + 1)
    for v in terminals:
        is_term[v] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); w = int(data[idx + 2]); idx += 3
        adj[u].append((v, w)); adj[v].append((u, w))

    # The cabling graph is a tree, so the minimum subtree connecting all required sites is unique: an
    # edge belongs to it iff removing the edge leaves at least one required site on EACH side. Root
    # the tree, count required sites in every subtree, and sum the weights of the qualifying edges.
    root = terminals[0]
    parent = [0] * (n + 1)
    pw = [0] * (n + 1)          # weight of the edge to the parent
    order = []
    visited = [False] * (n + 1)
    visited[root] = True
    q = deque([root])
    while q:
        u = q.popleft(); order.append(u)
        for (v, w) in adj[u]:
            if not visited[v]:
                visited[v] = True; parent[v] = u; pw[v] = w; q.append(v)

    cnt = [1 if is_term[v] else 0 for v in range(n + 1)]
    total = t
    cost = 0
    for v in reversed(order):          # post-order: children before parents
        if v == root:
            continue
        c = cnt[v]
        if 0 < c < total:              # required sites on both sides of the edge to parent
            cost += pw[v]
        cnt[parent[v]] += c

    sys.stdout.write(f"{cost}\n")


main()
