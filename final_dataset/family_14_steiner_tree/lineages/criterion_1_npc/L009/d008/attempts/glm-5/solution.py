import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    priority = [int(next(it)) for _ in range(t)]
    
    if t <= 1:
        print(0)
        return
    
    # Build graph and find minimum spanning tree
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    edges.sort()
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    adj = [[] for _ in range(n + 1)]
    total_cost = 0
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))
            total_cost += w
    
    # BFS from first priority to build parent pointers
    root = priority[0]
    par = [0] * (n + 1)
    parw = [0] * (n + 1)
    visited = [False] * (n + 1)
    visited[root] = True
    queue = [root]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                par[v] = u
                parw[v] = w
                queue.append(v)
    
    # Mark edges on paths from root to each priority node
    on_path = [False] * (n + 1)
    for p in priority[1:]:
        cur = p
        while cur != root and not on_path[cur]:
            on_path[cur] = True
            cur = par[cur]
    
    # Sum weights of marked edges
    answer = 0
    for i in range(1, n + 1):
        if on_path[i]:
            answer += parw[i]
    
    print(answer)

solve()