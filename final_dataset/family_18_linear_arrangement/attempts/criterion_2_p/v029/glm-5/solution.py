import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Find root (node with degree != 1, or single node)
    root = 1
    for i in range(1, n+1):
        if len(adj[i]) != 1:
            root = i
            break
    
    # BFS to get parent-child relationships
    parent = [0]*(n+1)
    children = [[] for _ in range(n+1)]
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
    
    # Compute subtree sizes
    size = [1]*(n+1)
    for u in reversed(order):
        for v in children[u]:
            size[u] += size[v]
    
    # Compute total length for optimal arrangement
    # For each edge (parent, child), contribution is 2 * size[child] * (n - size[child])
    total = 0
    for u in order:
        for v in children[u]:
            s = size[v]
            total += 2 * s * (n - s)
    
    if total > B:
        print("NO")
        return
    
    # Assign positions using DFS
    pos = [0]*(n+1)
    counter = 1
    
    def dfs(u):
        nonlocal counter
        pos[u] = counter
        counter += 1
        for v in children[u]:
            dfs(v)
    
    dfs(root)
    
    print("YES")
    print(' '.join(str(pos[i]) for i in range(1, n+1)))

solve()