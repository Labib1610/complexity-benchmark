import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    R = next(it)          # number of vertices
    S = next(it)          # always R-1
    P = next(it)          # number of special vertices

    special = [False] * (R + 1)
    for _ in range(P):
        special[next(it)] = True

    adj = [[] for _ in range(R + 1)]
    for _ in range(S):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    # ---------- iterative DFS to obtain parent, edge weight and order ----------
    parent = [0] * (R + 1)          # parent[1] stays 0 (root)
    parent_w = [0] * (R + 1)       # weight of edge to parent
    order = []                     # visitation order (preorder)
    stack = [1]
    parent[1] = -1                 # mark root

    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)

    # ---------- post‑order processing ----------
    cnt = [0] * (R + 1)            # temporary accumulator for children
    answer = 0

    for u in reversed(order):
        # total specials in the subtree rooted at u
        total = cnt[u] + (1 if special[u] else 0)

        if u != 1:                 # root has no edge to parent
            if 0 < total < P:
                answer += parent_w[u]
            cnt[parent[u]] += total

    print(answer)


if __name__ == "__main__":
    solve()