import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1]); B = int(data[2])
    adj = [[] for _ in range(n+1)]
    idx = 3
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)

    # Find root: the unique node with degree != 1 (or n==1)
    root = 1
    if n > 1:
        for i in range(1, n+1):
            if len(adj[i]) != 1:
                root = i
                break

    # Build rooted tree
    children = [[] for _ in range(n+1)]
    parent = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                children[u].append(v)
                stack.append(v)

    # Post-order
    post = []
    stack = [(root, False)]
    while stack:
        u, processed = stack.pop()
        if processed:
            post.append(u)
        else:
            stack.append((u, True))
            for v in reversed(children[u]):
                stack.append((v, False))

    # Compute subtree sizes
    size = [1]*(n+1)
    for u in post:
        for v in children[u]:
            size[u] += size[v]

    # Assign slots via DFS: root gets 1, children get contiguous blocks
    slot = [0]*(n+1)
    start = [0]*(n+1)
    start[root] = 1
    stack = [root]
    while stack:
        u = stack.pop()
        slot[u] = start[u]
        cur = start[u] + 1
        for v in children[u]:
            start[v] = cur
            cur += size[v]
            stack.append(v)

    # Compute total cost
    total = 0
    for u in range(1, n+1):
        for v in children[u]:
            total += abs(slot[u] - slot[v])

    if total <= B:
        out = ['YES']
        out.append(' '.join(str(slot[i]) for i in range(1, n+1)))
        sys.stdout.write('\n'.join(out) + '\n')
    else:
        sys.stdout.write('NO\n')

solve()