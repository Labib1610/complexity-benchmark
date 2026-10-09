import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    core = set(map(int, input().split()))
    
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    
    parent = [0]*(n+1)
    weight = [0]*(n+1)
    depth = [0]*(n+1)
    
    # DFS to set parent and depth
    stack = [(next(iter(core)), 0, 0)]  # (node, parent, weight)
    visited = [False]*(n+1)
    visited[stack[0][0]] = True
    while stack:
        u, p, w = stack.pop()
        parent[u] = p
        weight[u] = w
        for v, wgt in g[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                stack.append((v, u, wgt))
    
    # Mark nodes that are in the minimal subtree
    has_core = [False]*(n+1)
    # We'll do a post-order traversal
    order = []
    stack = [next(iter(core))]
    visited = [False]*(n+1)
    visited[stack[0]] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, _ in g[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    for u in reversed(order):
        if u in core:
            has_core[u] = True
        for v, _ in g[u]:
            if parent[v] == u and has_core[v]:
                has_core[u] = True
    
    ans = 0
    for u in range(1, n+1):
        if has_core[u] and parent[u] != 0 and has_core[parent[u]]:
            ans += weight[u]
    
    print(ans)

if __name__ == "__main__":
    solve()