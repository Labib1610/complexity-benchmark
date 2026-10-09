import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    targets = [int(next(it)) for _ in range(t)]
    is_target = [False] * (n + 1)
    for x in targets:
        is_target[x] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Iterative DFS to compute subtree target counts and identify edges in the Steiner tree
    # We root the tree at 1 (or any node)
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0 and v != parent[1]:
                # Actually need to be careful with root
                pass
    # Let's redo the iterative DFS properly
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    visited = [False] * (n + 1)
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        if is_target[i]:
            count[i] = 1
    
    # Process in reverse order (post-order)
    for u in reversed(order):
        p = parent[u]
        if p != -1:
            count[p] += count[u]
    
    total_cost = 0
    for u in range(2, n + 1):
        c = count[u]
        if 0 < c < t:
            total_cost += parent_edge_weight[u]
    
    print(total_cost)

solve()