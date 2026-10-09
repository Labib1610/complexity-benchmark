import sys
from sys import setrecursionlimit
input = sys.stdin.readline

def solve():
    n, m, B = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Find centroid
    size = [0]*(n+1)
    def dfs_size(u, p):
        size[u] = 1
        for v in adj[u]:
            if v != p:
                dfs_size(v, u)
                size[u] += size[v]
    
    dfs_size(1, 0)
    
    def find_centroid(u, p):
        for v in adj[u]:
            if v != p and size[v] > n//2:
                return find_centroid(v, u)
        return u
    
    centroid = find_centroid(1, 0)
    
    # Recompute sizes from centroid
    dfs_size(centroid, 0)
    
    # Compute minimum cost
    total = 0
    def dfs_cost(u, p):
        nonlocal total
        for v in adj[u]:
            if v != p:
                s = size[v]
                total += min(s, n - s)
                dfs_cost(v, u)
    
    dfs_cost(centroid, 0)
    
    if total > B:
        print("NO")
        return
    
    # Build arrangement using DFS from centroid
    # Place centroid at center, distribute subtrees
    order = []
    stack = [centroid]
    visited = [False]*(n+1)
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                stack.append(v)
    
    # Assign pads: place in order but center the centroid
    # Simple approach: assign pads 1..n in DFS order
    pos = [0]*(n+1)
    for i, u in enumerate(order):
        pos[u] = i + 1
    
    print("YES")
    print(' '.join(str(pos[i]) for i in range(1, n+1)))

solve()