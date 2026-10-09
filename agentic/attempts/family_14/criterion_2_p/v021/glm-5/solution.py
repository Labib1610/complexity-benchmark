import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    murals = set()
    for _ in range(t):
        murals.add(int(data[idx])); idx += 1

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

    # We find the minimal subtree connecting all mural nodes.
    # This is equivalent to the Steiner tree on a tree, which can be found
    # by keeping only edges that lie on paths between mural nodes.
    # A standard way: root the tree, find LCA-based approach, or use the
    # "virtual tree" concept. Here we use a simpler approach:
    # The minimal connecting subtree consists of all edges that have at least
    # one mural node in both resulting components when the edge is removed.

    # We root the tree at a mural node and compute subtree mural counts.
    root = next(iter(murals))

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)

    mural_count = [0] * (n + 1)
    for x in murals:
        mural_count[x] = 1

    # Process in reverse order (children before parents)
    for u in reversed(order):
        if parent[u] != -1:
            mural_count[parent[u]] += mural_count[u]

    total = 0
    for u in range(1, n + 1):
        if parent[u] != -1 and 0 < mural_count[u] < t:
            total += parent_weight[u]

    print(total)

solve()