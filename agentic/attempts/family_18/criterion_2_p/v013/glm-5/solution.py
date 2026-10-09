import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Find a leaf to root the tree
    root = 0
    for i in range(n):
        if len(adj[i]) == 1:
            root = i
            break
    
    # BFS to get order
    order = []
    parent = [-1] * n
    stack = [root]
    parent[root] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    
    # Compute subtree sizes
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if parent[v] == u:
                size[u] += size[v]
    
    # Compute minimum cable length
    min_cable = 0
    for u in range(n):
        for v in adj[u]:
            if parent[v] == u:
                min_cable += size[v] * (n - size[v])
    min_cable //= 2
    
    if min_cable > B:
        print("NO")
        return
    
    # Assign slots using DFS
    slots = [0] * n
    current_slot = 1
    
    def dfs(u):
        nonlocal current_slot
        slots[u] = current_slot
        current_slot += 1
        for v in adj[u]:
            if parent[v] == u:
                dfs(v)
    
    dfs(root)
    
    print("YES")
    print(' '.join(map(str, slots)))

solve()