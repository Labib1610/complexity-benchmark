import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Root the tree at any target node
    root = next(iter(targets))
    
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
    
    # Now compute for each node if its subtree contains a target
    has_target = [False]*(n+1)
    for node in targets:
        has_target[node] = True
    
    total_cost = 0
    # Process nodes in reverse order (post-order)
    for u in reversed(order):
        if u != root:
            if has_target[u]:
                total_cost += parent_w[u]
                # propagate up
                p = parent[u]
                has_target[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()