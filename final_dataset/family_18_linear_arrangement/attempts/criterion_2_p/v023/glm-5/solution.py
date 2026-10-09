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

    # BFS to find a centroid: a vertex whose removal leaves no subtree > n/2
    parent = [0]*(n+1)
    order = []
    root = 1
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for w in adj[u]:
            if parent[w] == 0:
                parent[w] = u
                stack.append(w)

    size = [1]*(n+1)
    for u in reversed(order):
        if parent[u] > 0:
            size[parent[u]] += size[u]

    centroid = root
    for u in range(1, n+1):
        max_part = n - size[u]
        for w in adj[u]:
            if w != parent[u]:
                if size[w] > max_part:
                    max_part = size[w]
        if max_part <= n // 2:
            centroid = u
            break

    # BFS from centroid to compute distances
    dist = [0]*(n+1)
    visited = [False]*(n+1)
    visited[centroid] = True
    queue = [centroid]
    head = 0
    while head < len(queue):
        u = queue[head]; head += 1
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True
                dist[w] = dist[u] + 1
                queue.append(w)

    # Assign windows: centroid gets 1, others get dist+1
    assign = [0]*(n+1)
    for u in range(1, n+1):
        assign[u] = dist[u] + 1

    total = 0
    for u in range(1, n+1):
        for w in adj[u]:
            if w > u:
                total += abs(assign[u] - assign[w])

    if total <= B:
        out = ["YES"]
        out.append(" ".join(str(assign[u]) for u in range(1, n+1)))
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()