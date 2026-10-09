import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Find centroid
    parent = [-1] * n
    size = [0] * n
    
    def dfs(u, p):
        size[u] = 1
        for v in adj[u]:
            if v != p:
                parent[v] = u
                dfs(v, u)
                size[u] += size[v]
    
    dfs(0, -1)
    
    centroid = 0
    found = True
    while found:
        found = False
        for v in adj[centroid]:
            if v != parent[centroid] and size[v] > n // 2:
                centroid = v
                found = True
                break
    
    # Rebuild tree with centroid as root
    parent = [-1] * n
    order = []
    stack = [centroid]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
    
    size = [1] * n
    for u in reversed(order):
        if parent[u] != -1:
            size[parent[u]] += size[u]
    
    # Greedy assignment
    slot = [0] * n
    current_slot = 1
    stack = [(centroid, -1)]
    while stack:
        u, p = stack.pop()
        slot[u] = current_slot
        current_slot += 1
        children = [(size[v], v) for v in adj[u] if v != p]
        children.sort(reverse=True)
        for _, v in children:
            stack.append((v, u))
    
    # Calculate total cable length
    total = 0
    for u, v in edges:
        total += abs(slot[u] - slot[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, slot)))
    else:
        print("NO")

solve()