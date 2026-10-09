import sys
from sys import setrecursionlimit

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
    
    # Build rooted tree
    parent = [0] * (n + 1)
    order = []
    root = 1
    for i in range(1, n + 1):
        if adj[i]:
            root = i
            break
    
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
    
    # Compute subtree sizes
    size = [1] * (n + 1)
    for u in reversed(order):
        if parent[u] > 0:
            size[parent[u]] += size[u]
    
    # Compute cost of each edge
    cost = [0] * (n + 1)
    for u in order:
        if parent[u] > 0:
            p = parent[u]
            s = size[u]
            cost[u] = s * (n - s)
    
    # Greedy assignment
    assign = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        if parent[u] > 0:
            children[parent[u]].append(u)
    
    # Sort children by cost descending
    for u in range(1, n + 1):
        children[u].sort(key=lambda x: cost[x], reverse=True)
    
    counter = 1
    stack = [root]
    while stack:
        u = stack.pop()
        assign[u] = counter
        counter += 1
        for v in reversed(children[u]):
            stack.append(v)
    
    # Compute total friction
    total = 0
    for u in range(2, n + 1):
        total += abs(assign[u] - assign[parent[u]])
    
    if total <= B:
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()