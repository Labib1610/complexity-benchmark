import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    T = set(map(int, input().split()))
    edges = []
    adj = [[] for _ in range(n+1)]
    total = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        total += w
    
    if t == 1:
        print(0)
        return
    
    # DFS to find edges that are part of Steiner tree
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    visited = [False]*(n+1)
    stack = [1]
    visited[1] = True
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
    
    has_priority = [False]*(n+1)
    for u in range(1, n+1):
        if u in T:
            has_priority[u] = True
    
    steiner_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == 1:
            continue
        if has_priority[u]:
            steiner_cost += parent_w[u]
            # propagate up
            p = parent[u]
            while p != 0 and not has_priority[p]:
                has_priority[p] = True
                steiner_cost += parent_w[p]
                p = parent[p]
    
    print(total - steiner_cost)

if __name__ == "__main__":
    solve()