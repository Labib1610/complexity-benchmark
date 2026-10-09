import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # Build tree (it's connected, acyclic)
    parent = [-1]*n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    
    # Compute subtree sizes
    size = [1]*n
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    min_sum = 0
    for u in range(1, n):
        min_sum += size[u]
    
    if min_sum > B:
        print("NO")
        return
    
    # Produce DFS order
    pos = [0]*n
    order_dfs = []
    visited = [False]*n
    def dfs(u):
        visited[u] = True
        order_dfs.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    dfs(0)
    
    for idx, node in enumerate(order_dfs):
        pos[node] = idx + 1
    
    print("YES")
    print(" ".join(str(pos[i]) for i in range(n)))

if __name__ == "__main__":
    solve()