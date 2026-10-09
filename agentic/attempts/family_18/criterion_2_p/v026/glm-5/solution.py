import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # Find root: the node with degree 1 (or n==1)
    root = 1
    if n > 1:
        for i in range(1, n + 1):
            if len(adj[i]) == 1:
                root = i
                break

    # BFS to build parent array and children list
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = []
    visited = [False] * (n + 1)
    q = deque([root])
    visited[root] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                q.append(v)

    # Compute subtree sizes
    size = [1] * (n + 1)
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            size[p] += size[u]

    # Assign slots using DFS: root gets interval [1, n], children get contiguous subintervals
    slot = [0] * (n + 1)
    counter = [0] * (n + 1)  # tracks current offset for each node's interval

    # Initialize root's interval
    counter[root] = 1

    stack = [root]
    while stack:
        u = stack.pop()
        start = counter[u]
        slot[u] = start
        next_start = start + 1
        for v in children[u]:
            sz = size[v]
            counter[v] = next_start
            next_start += sz
            stack.append(v)

    # Compute total cost
    total = 0
    for u in range(1, n + 1):
        p = parent[u]
        if p != 0:
            total += abs(slot[u] - slot[p])

    if total <= B:
        print("YES")
        print(' '.join(str(slot[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()