import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    LOG = 20
    depth = [0]*(n+1)
    parent = [[0]*(n+1) for _ in range(LOG)]
    dist_from_root = [0]*(n+1)
    tin = [0]*(n+1)
    tout = [0]*(n+1)
    timer = 0
    
    # iterative DFS to fill parent[0], depth, dist, tin/tout
    stack = [(1, 0, 0)]  # node, parent, edge weight to parent
    parent[0][1] = 1
    while stack:
        u, p, w = stack.pop()
        if u != 1:
            depth[u] = depth[p] + 1
            dist_from_root[u] = dist_from_root[p] + w
            parent[0][u] = p
        tin[u] = timer
        timer += 1
        for v, wt in adj[u]:
            if v != p:
                stack.append((v, u, wt))
        tout[u] = timer
    
    # build up table
    for k in range(1, LOG):
        for v in range(1, n+1):
            parent[k][v] = parent[k-1][parent[k-1][v]]
    
    def is_ancestor(u, v):
        return tin[u] <= tin[v] and tout[v] <= tout[u]
    
    def lca(u, v):
        if is_ancestor(u, v):
            return u
        if is_ancestor(v, u):
            return v
        for k in range(LOG-1, -1, -1):
            if not is_ancestor(parent[k][u], v):
                u = parent[k][u]
        return parent[0][u]
    
    def distance(u, v):
        w = lca(u, v)
        return dist_from_root[u] + dist_from_root[v] - 2*dist_from_root[w]
    
    terminals.sort(key=lambda x: tin[x])
    total = 0
    for i in range(t):
        u = terminals[i]
        v = terminals[(i+1)%t]
        total += distance(u, v)
    
    print(total // 2)

if __name__ == "__main__":
    solve()