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
    
    # Root at any critical node
    root = next(iter(critical))
    
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_w[v] = w
            stack.append(v)
    
    has_critical = [False]*(n+1)
    for node in critical:
        has_critical[node] = True
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if has_critical[u]:
            total_cost += parent_w[u]
            has_critical[parent[u]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()