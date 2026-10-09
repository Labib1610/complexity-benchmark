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
    
    if t <= 1:
        print(0)
        return
    
    # Root at any target
    root = next(iter(targets))
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    order = [root]
    parent[root] = -1
    stack = [root]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
                order.append(v)
    
    # Count targets in subtree
    cnt = [0]*(n+1)
    for v in targets:
        cnt[v] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        p = parent[u]
        if cnt[u] > 0 and t - cnt[u] > 0:
            total_cost += parent_w[u]
        cnt[p] += cnt[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()