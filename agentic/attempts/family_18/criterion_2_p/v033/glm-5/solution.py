import sys
sys.setrecursionlimit(2000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to find one endpoint of the diameter
    def bfs_farthest(start):
        dist = [-1] * (n + 1)
        q = [start]
        dist[start] = 0
        head = 0
        farthest = start
        while head < len(q):
            u = q[head]
            head += 1
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > dist[farthest]:
                        farthest = v
        return farthest
    
    # Find diameter endpoints
    u1 = bfs_farthest(1)
    u2 = bfs_farthest(u1)
    
    # BFS to get parent pointers for tree rooted at u2
    parent = [0] * (n + 1)
    order = []
    q = [u2]
    parent[u2] = -1
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                q.append(v)
    
    # Compute subtree sizes
    size = [1] * (n + 1)
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    # Compute total length for star graph (optimal arrangement)
    # Sort sizes in descending order and assign positions 1, 2, ..., n
    sizes = [size[u] for u in range(1, n + 1)]
    sizes.sort(reverse=True)
    total = 0
    for i, s in enumerate(sizes):
        total += s * i
    
    if total > B:
        print("NO")
        return
    
    print("YES")
    # Assign positions: unit with size s gets position (s's rank in descending order)
    # Use stable sorting to handle ties
    indexed_sizes = [(size[u], u) for u in range(1, n + 1)]
    indexed_sizes.sort(key=lambda x: -x[0])
    pos = [0] * (n + 1)
    for i, (_, u) in enumerate(indexed_sizes):
        pos[u] = i + 1
    print(' '.join(map(str, pos[1:])))

solve()