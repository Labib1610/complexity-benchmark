import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    T = []
    for _ in range(t):
        T.append(int(data[idx]) - 1)
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    T_set = set(T)
    
    # Kruskal's MST
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
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
    
    edges.sort(key=lambda e: e[2])
    
    total = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
    
    # Now find the minimal subtree containing all T nodes
    # Reset DSU
    parent = list(range(n))
    rank = [0] * n
    
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        # Union by rank
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        elif rank[ru] > rank[rv]:
            parent[rv] = ru
        else:
            parent[rv] = ru
            rank[ru] += 1
    
    # Check if all T are connected
    root = find(T[0])
    all_connected = all(find(x) == root for x in T)
    
    if not all_connected:
        # This shouldn't happen per problem statement, but handle gracefully
        print(-1)
        return
    
    # Build adjacency list of MST
    adj = [[] for _ in range(n)]
    parent = list(range(n))
    rank = [0] * n
    
    mst_edges = []
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1
            mst_edges.append((u, v, w))
            adj[u].append((v, w))
            adj[v].append((u, w))
    
    # Find minimal subtree containing all T nodes using DFS
    # Mark nodes that are on paths between T nodes
    # Use iterative DFS to avoid recursion limit
    
    # First, build a rooted tree structure
    # Pick root = T[0]
    root = T[0]
    parent_arr = [-1] * n
    parent_weight = [0] * n
    order = []
    stack = [root]
    visited = [False] * n
    visited[root] = True
    
    while stack:
        node = stack.pop()
        order.append(node)
        for nb, w in adj[node]:
            if not visited[nb]:
                visited[nb] = True
                parent_arr[nb] = node
                parent_weight[nb] = w
                stack.append(nb)
    
    # Count how many T nodes are in each subtree
    cnt = [0] * n
    for x in T:
        cnt[x] = 1
    
    # Process in reverse order (bottom-up)
    for node in order:
        p = parent_arr[node]
        if p != -1:
            cnt[p] += cnt[node]
    
    # An edge is needed if cnt[child] > 0 and cnt[child] < t
    answer = 0
    for node in order:
        p = parent_arr[node]
        if p != -1:
            if 0 < cnt[node] < t:
                answer += parent_weight[node]
    
    print(answer)

solve()