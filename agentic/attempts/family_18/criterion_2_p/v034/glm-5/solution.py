import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # BFS to find a centroid: a vertex whose removal leaves no subtree > n/2
    parent = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    root = 1
    visited[root] = True
    q = deque([root])
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    size = [1] * (n + 1)
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            size[p] += size[u]

    centroid = root
    for u in range(1, n + 1):
        max_part = n - size[u]
        for v in adj[u]:
            if v != parent[u]:
                if size[v] > max_part:
                    max_part = size[v]
        if max_part <= n // 2:
            centroid = u
            break

    # Re-root BFS tree at centroid
    parent = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    visited[centroid] = True
    q = deque([centroid])
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    children = [[] for _ in range(n + 1)]
    for u in order:
        p = parent[u]
        if p != 0:
            children[p].append(u)

    # Post-order traversal
    post = []
    stack = [(centroid, False)]
    while stack:
        u, processed = stack.pop()
        if processed:
            post.append(u)
        else:
            stack.append((u, True))
            for v in reversed(children[u]):
                stack.append((v, False))

    # Greedy slot assignment: centroid gets slot 1, subtrees occupy contiguous blocks
    slot = [0] * (n + 1)
    slot[centroid] = 1
    nxt = 2
    for u in post:
        if u == centroid:
            continue
        slot[u] = nxt
        nxt += 1

    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total += abs(slot[u] - slot[v])

    if total <= B:
        out = ["YES"]
        out.append(" ".join(str(slot[i]) for i in range(1, n + 1)))
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()