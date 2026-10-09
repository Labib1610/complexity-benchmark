import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Root at any critical node
    root = next(iter(critical))
    
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    visited = [False]*(n+1)
    
    stack = [root]
    visited[root] = True
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
    
    has_critical = [False]*(n+1)
    for u in order[::-1]:
        if u in critical:
            has_critical[u] = True
        for v, w in adj[u]:
            if v != parent[u] and has_critical[v]:
                has_critical[u] = True
    
    total_cost = 0
    for u in range(1, n+1):
        if u != root and has_critical[u]:
            total_cost += parent_w[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()