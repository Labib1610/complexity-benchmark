import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    hubs = set()
    for _ in range(t):
        hubs.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # BFS to find parent and depth for each node
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    depth[1] = 0
    
    front = 0
    while front < len(order):
        u = order[front]
        front += 1
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                order.append(v)
    
    # Process nodes from leaves to root
    # cnt[v] = number of hubs in subtree of v (when v is processed)
    cnt = [0] * (n + 1)
    for v in hubs:
        cnt[v] = 1
    
    total = 0
    # Process in reverse BFS order (leaves first)
    for i in range(len(order) - 1, 0, -1):
        v = order[i]
        p = parent[v]
        if p != 0:
            if cnt[v] > 0 and cnt[v] < t:
                total += parent_weight[v]
            cnt[p] += cnt[v]
    
    print(total)

if __name__ == "__main__":
    solve()